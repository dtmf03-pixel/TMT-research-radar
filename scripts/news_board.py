"""④ 뉴스 보드 수집 — config/board.yml 의 상장기업별 최신 뉴스.

빅카인즈 '오늘의 이슈' 같은 카드형 화면에 쓸 데이터를 만든다.
news_monitor.py 와 달리 회계 필터를 걸지 않는다. 회사 관련 **전체 뉴스**를
최신순으로 담아 동향 파악용으로 쓴다.

소스는 Google 뉴스 RSS라 API 키가 필요 없다.  → data/news_board.json

환경변수로 조절:
  BOARD_WINDOW  수집 기간 (기본 2d — 매일 갱신 기준). 예: 1d, 7d
  BOARD_MAX     회사당 저장할 이슈 수 (기본 40). 메인 카드는 이 중 앞부분만 쓰고,
                회사 상세 페이지가 나머지를 전부 보여준다.
"""
from __future__ import annotations
import json
import os
import re
import sys
import time
import urllib.parse
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

from common import DATA, load_yaml
from news_monitor import fetch

KST = timezone(timedelta(hours=9))
WINDOW = os.environ.get("BOARD_WINDOW", "2d")
MAX_PER_COMPANY = int(os.environ.get("BOARD_MAX", "40"))
SLEEP = 0.8   # RSS 연속 호출 간격


def strip_source(title: str, source: str = "") -> str:
    """Google 뉴스 제목의 ' - 언론사' 꼬리를 뗀다.

    기사 제목 자체가 이미 '… - 조선비즈'로 끝나는데 Google 이 영문 소스명을 한 번
    더 붙이는 경우가 있어(' … - 조선비즈 - Chosunbiz') 두 단계로 처리한다.
    """
    t = title
    if source:
        t = re.sub(r"\s+-\s+" + re.escape(source) + r"\s*$", "", t)
    return re.sub(r"\s+-\s+[^-]{1,20}$", "", t).strip()


def bigrams(title: str) -> set[str]:
    """제목의 글자 2-gram 집합. 형태소 분석기 없이 한국어 제목을 비교하려는 것."""
    s = re.sub(r"[^0-9A-Za-z가-힣]", "", title).lower()
    return {s[i:i + 2] for i in range(len(s) - 1)}


def similarity(a: set[str], b: set[str]) -> float:
    """같은 사건을 다룬 기사끼리 묶는 데 쓰는 제목 유사도.

    자카드는 제목 길이가 크게 다르면(속보 한 줄 vs 해설 제목) 실제보다 낮게 나온다.
    그래서 짧은 쪽 기준 포함도(overlap)와 섞어 길이 차이에 덜 민감하게 만든다.
    """
    if not a or not b:
        return 0.0
    inter = len(a & b)
    jaccard = inter / len(a | b)
    overlap = inter / min(len(a), len(b))
    return max(jaccard, overlap * 0.85)


def to_iso(pubdate: str) -> str:
    """RSS pubDate(RFC-822) → KST ISO 문자열. 파싱 실패 시 빈 문자열."""
    if not pubdate:
        return ""
    try:
        return parsedate_to_datetime(pubdate).astimezone(KST).isoformat()
    except (TypeError, ValueError):
        return ""


def google_news_link(query: str, window: str) -> str:
    q = urllib.parse.quote(f"{query} when:{window}")
    return f"https://news.google.com/search?q={q}&hl=ko&gl=KR&ceid=KR:ko"


def alias_filter(aliases: list[str]) -> re.Pattern | None:
    """제목에 회사 별칭이 있는지 볼 정규식.

    앞에 한글·영숫자가 붙어 있으면 다른 회사 이름의 일부다 — '지엔씨에너지'의 엔씨,
    'SKT'의 KT. 그래서 왼쪽은 막는다.

    반대로 오른쪽 한글까지 막으면 안 된다. 조사가 붙는 게 한국어의 기본이라
    '엔씨소프트가', '엔씨소프트의' 가 전부 탈락해 버린다. 오른쪽은 영숫자만 막아
    'KTX' 가 KT 로 잡히는 것만 걸러낸다.

    '하이브'/'하이브리드'처럼 뒤에 한글이 붙어 다른 말이 되는 경우는 이 규칙으로
    거를 수 없다. 그건 회사별 exclude 로 처리한다.
    """
    if not aliases:
        return None
    parts = [rf"(?<![가-힣A-Za-z0-9]){re.escape(a)}(?![A-Za-z0-9])" for a in aliases]
    return re.compile("|".join(parts), re.I)


def is_major(source: str, majors: list[str]) -> bool:
    return any(m in source or source in m for m in majors if m)


def buzz(story: dict, now: datetime, rank_cfg: dict) -> int:
    """화제도 점수. 클릭수는 못 구하므로 보도량·매체·최신성·Google 순위로 대신한다."""
    w = rank_cfg["weights"]
    majors = rank_cfg.get("major_outlets", [])
    score = (len(story["outlets"]) - 1) * w["per_outlet"]
    if any(is_major(s, majors) for s in story["outlets"]):
        score += w["major_outlet"]
    if story["published"]:
        hours = (now - datetime.fromisoformat(story["published"])).total_seconds() / 3600
        if hours <= 24:
            score += w["within_24h"]
        elif hours <= 72:
            score += w["within_72h"]
    if story["rank"] < 10:
        score += w["google_top10"]
    elif story["rank"] < 30:
        score += w["google_top30"]
    return score


def collect(company: dict, now: datetime, rank_cfg: dict) -> dict:
    name = company["name"]
    query = company.get("query") or name
    exclude = company.get("exclude") or []
    must = alias_filter(company.get("aliases") or [])
    # 광고·미디어처럼 보도량이 얇은 회사는 기본 기간으로는 카드가 비어버린다.
    # 회사별로 더 긴 창을 줄 수 있게 한다.
    window = company.get("window") or WINDOW

    # query 를 직접 준 경우엔 적힌 그대로 쓴다(따옴표·OR 를 회사별로 조절하기 위함).
    # 따옴표 유무로 결과가 몇 배씩 갈리는 회사가 있어 자동으로 손대지 않는다.
    term = company.get("query") or f'"{name}"'
    try:
        raw = fetch(f"{term} when:{window}")
    except Exception as e:  # noqa: BLE001
        print(f"[warn] {name}: {e}", file=sys.stderr)
        raw = []

    # 같은 사건을 다룬 기사를 버리지 않고 묶는다. 묶인 언론사 수가 곧 화제도 신호.
    # rank 는 Google 뉴스가 내려준 순서(=자체 노출 순위)라 그대로 보존한다.
    thresh = rank_cfg["similarity_threshold"]
    min_hits = rank_cfg.get("min_matches", 2)
    stories: list[dict] = []
    kept = 0
    for rank, it in enumerate(raw):
        title = strip_source(it["title"], it["source"])
        if not title or any(x in title for x in exclude):
            continue
        if must and not must.search(title):
            continue        # 본문에만 회사가 스친 기사 — 제목에 없으면 그 회사 뉴스가 아니다
        kept += 1
        grams = bigrams(title)
        # 대표 제목 하나가 아니라 이미 묶인 기사 전부와 비교하되, 최소 min_hits 건과
        # 닮아야 합친다. 한 건만 스쳐도 붙이면 A~B, B~C 로 이어지며 다른 사건까지
        # 한 덩어리가 된다(실제로 '테이블 데이' 기사가 캠페인 묶음에 끌려 들어갔다).
        for st in stories:
            hits = sum(1 for g in st["_grams"] if similarity(grams, g) >= thresh)
            if hits >= min(min_hits, len(st["_grams"])):
                if it["source"] and it["source"] not in st["outlets"]:
                    st["outlets"].append(it["source"])
                st["_grams"].append(grams)
                break
        else:
            stories.append({
                "title": title,
                "url": it["url"],
                "source": it["source"],
                "published": to_iso(it["date"]),
                "rank": rank,
                "outlets": [it["source"]] if it["source"] else [],
                "_grams": [grams],
            })

    for st in stories:
        st["outlet_count"] = len(st["outlets"])
        st["score"] = buzz(st, now, rank_cfg)
        del st["_grams"], st["outlets"]

    # 화제도 높은 순. 동점이면 최신 기사 우선.
    stories.sort(key=lambda s: (s["score"], s["published"]), reverse=True)
    return {
        "name": name,
        "slug": company.get("slug", ""),
        "stock_code": company.get("stock_code", ""),
        "found": kept,                       # 기간 내 수집 기사 수(카드 배지)
        "story_count": len(stories),         # 중복 보도를 묶은 뒤의 사건 수
        "window": window,                    # 기본값과 다르면 화면에 표시한다
        "search_url": google_news_link(query, window),
        "articles": stories[:MAX_PER_COMPANY],
    }


def main() -> None:
    cfg = load_yaml("board.yml")
    rank_cfg = load_yaml("ranking.yml")
    now = datetime.now(KST)
    days = int(re.sub(r"\D", "", WINDOW) or 2)

    sectors = []
    total = 0
    for sector, meta in cfg.items():
        firms = []
        for c in meta.get("companies", []):
            row = collect(c, now, rank_cfg)
            total += row["found"]
            firms.append(row)
            print(f"  {row['name']:<10} {row['found']:>3}건 / 사건 {row['story_count']:>3}")
            time.sleep(SLEEP)
        # 뉴스가 많은 회사부터. 동률이면 최신 기사가 있는 쪽 우선.
        firms.sort(key=lambda f: (f["found"], f["articles"][0]["published"]
                                  if f["articles"] else ""), reverse=True)
        sectors.append({"name": sector, "color": meta.get("color", "#475569"),
                        "companies": firms})

    out = {
        "generated_at": now.isoformat(),
        "window": WINDOW,          # 기본 수집 기간. 회사별로 다르면 카드에 표시한다
        "window_days": days,
        "period_from": (now - timedelta(days=days)).strftime("%Y.%m.%d"),
        "period_to": now.strftime("%Y.%m.%d"),
        "total_articles": total,
        "company_count": sum(len(s["companies"]) for s in sectors),
        "sectors": sectors,
    }
    DATA.mkdir(exist_ok=True)
    with open(DATA / "news_board.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"뉴스 보드: {total}건 / {out['company_count']}개사 저장 (최근 {days}일)")


if __name__ == "__main__":
    main()
