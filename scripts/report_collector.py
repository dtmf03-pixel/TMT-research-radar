"""③ 회계법인 산업 리포트 수집.

config/sources.yml 에 등록된 회계법인 인사이트 페이지에서 발간물 링크를 긁어와,
제목에 산업/회계 키워드가 걸리는 항목을 data/reports.json 에 저장한다.

주의: 각 법인 사이트 구조가 바뀔 수 있어, 링크 텍스트 기반의 보수적 수집만 한다.
사이트 이용약관을 존중하고 과도한 요청을 피한다(요청 간 지연).
"""
from __future__ import annotations
import json
import sys
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from common import load_yaml, clean, DATA

# 우리 주제(TMT·미디어·엔터·게임·통신·회계)에 맞는 리포트만 (광범위한 "산업"은 제외)
TITLE_FILTER = [
    "미디어", "엔터", "콘텐츠", "게임", "TMT", "통신", "방송", "플랫폼",
    "회계", "IFRS", "무형자산", "수익인식", "리스", "결산", "K-콘텐츠", "OTT",
]

# 리포트가 아닌 노이즈(채용·소개·서비스·행사 페이지) 제외
TITLE_EXCLUDE = [
    "모집", "채용", "시험", "자격", "소개", "센터", "서비스", "구축",
    "About", "career", "문의", "협력", "행사", "세미나 신청", "발행하고",
    # 우리 주제와 무관한 산업 리포트 제외
    "항공우주", "방위", "우주", "국방", "조선", "자동차", "반도체", "바이오",
    "제약", "헬스케어", "금융", "은행", "보험", "건설", "화학", "에너지",
    "소비재", "유통", "물류", "부동산", "농업", "식품",
]
# 인사이트/리포트성 경로만 허용 (아니면 제외)
PATH_INCLUDE = ["/insight", "/insights", "/eri", "/our-thinking", "/thought", "issuemonitor", "issue-report"]
PATH_EXCLUDE = ["/career", "/about", "/services", "/service", "/events", "/digital-solutions", "/ai/"]

HEADERS = {"User-Agent": "audit-research-radar/1.0 (research; contact via GitHub)"}


def scrape(url: str) -> list[tuple[str, str]]:
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    out = []
    for a in soup.find_all("a", href=True):
        text = clean(a.get_text())
        raw = a["href"].strip()
        href = urljoin(url, raw)
        if len(text) < 8:
            continue
        # 페이지 내 앵커/스킵링크는 리포트가 아님
        if raw.startswith("#") or href.rstrip("/").endswith("#maincontent"):
            continue
        if href.split("#")[0].rstrip("/") == url.rstrip("/").split("#")[0]:
            continue  # 자기 자신(목록 페이지) 링크 제외
        if not any(k in text for k in TITLE_FILTER):
            continue
        if any(k in text for k in TITLE_EXCLUDE):
            continue
        low = href.lower()
        if any(p in low for p in PATH_EXCLUDE):
            continue
        if not any(p in low for p in PATH_INCLUDE):
            continue
        out.append((text, href))
    return out


def main() -> None:
    cfg = load_yaml("sources.yml")
    results = []
    seen: set[str] = set()
    for src in cfg.get("firms", []):
        if src.get("type") != "html":
            continue
        try:
            links = scrape(src["url"])
        except Exception as e:  # noqa: BLE001
            print(f"[warn] {src['firm']}: {e}", file=sys.stderr)
            continue
        for title, link in links:
            if link in seen:
                continue
            seen.add(link)
            results.append({
                "firm": src["firm"],
                "title": title,
                "url": link,
            })
        time.sleep(2)  # 예의상 지연

    DATA.mkdir(exist_ok=True)
    with open(DATA / "reports.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"리포트: {len(results)}건 저장")


if __name__ == "__main__":
    main()
