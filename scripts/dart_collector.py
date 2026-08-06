"""① DART 공시 수집.

DART_API_KEY 환경변수 필요 (https://opendart.fss.or.kr 무료 발급).
대상 기업의 최근 공시를 받아, 회계 관점에서 의미 있는 건만 골라 종류를 분류해 data/dart.json 에 저장.

분류(kind): 정정 / 감사 / 정기보고서 / 주요사항 / 실적 / 회계이슈
회계이슈 심화(무형자산·수익인식 등)는 공시 '제목'보다 사업보고서 '주석' 본문에 있으므로,
이 수집기는 이슈가 담길 가능성이 높은 공시 유형(정정·감사·정기·주요사항)을 근거 링크로 모으는 역할.
"""
from __future__ import annotations
import json
import os
import sys
from datetime import datetime, timedelta

import requests

from common import companies, match_topics, DATA, clean

API = "https://opendart.fss.or.kr/api/list.json"


# 재무·회계에 영향이 있는 자본거래/보고서 관련 키워드 (정정 필터링용)
ACCOUNTING_RELEVANT = (
    "사업보고서", "반기보고서", "분기보고서", "감사", "재무", "실적",
    "전환사채", "신주인수권", "교환사채", "유상증자", "무상증자",
    "합병", "분할", "영업양수도", "자산양수도", "양수도", "손상",
    "증권신고서", "투자설명서", "출자", "배당", "회계",
)


def classify(title: str) -> str | None:
    """공시 제목으로 종류 분류. None 이면 수집 제외(회계와 무관한 공시)."""
    if "정정" in title:
        # 주식매수선택권·주주명부·최대주주변경·담보제공 등 회계 무관 정정은 제외
        return "정정" if any(k in title for k in ACCOUNTING_RELEVANT) else None
    if "감사보고서" in title or "감사의견" in title:
        return "감사"
    if any(k in title for k in ("사업보고서", "반기보고서", "분기보고서")):
        return "정기보고서"                # 주석에 회계이슈가 담기는 근거 문서
    if "주요사항보고서" in title:
        return "주요사항"                  # 전환사채·합병·손상 등
    if "실적" in title:
        return "실적"                      # 실적공시(참고용)
    if match_topics(title):
        return "회계이슈"                  # 제목에 회계토픽이 직접 등장(드묾)
    return None


# 대시보드 노출 우선순위
PRIORITY = {"정정": 0, "감사": 1, "정기보고서": 2, "주요사항": 3, "회계이슈": 4, "실적": 5}


def fetch_disclosures(corp_code: str, bgn: str, end: str, key: str) -> list[dict]:
    params = {"crtfc_key": key, "corp_code": corp_code,
              "bgn_de": bgn, "end_de": end, "page_count": 100}
    r = requests.get(API, params=params, timeout=20)
    r.raise_for_status()
    body = r.json()
    if body.get("status") != "000":
        return []
    return body.get("list", [])


def main(days: int = 90) -> None:
    key = os.environ.get("DART_API_KEY")
    if not key:
        print("DART_API_KEY 미설정 — DART 수집 건너뜀", file=sys.stderr)
        return

    end = datetime.now().strftime("%Y%m%d")
    bgn = (datetime.now() - timedelta(days=days)).strftime("%Y%m%d")

    results = []
    for c in companies():
        if not c.get("corp_code"):
            continue
        try:
            items = fetch_disclosures(c["corp_code"], bgn, end, key)
        except Exception as e:  # noqa: BLE001
            print(f"[warn] {c['name']}: {e}", file=sys.stderr)
            continue
        for it in items:
            title = clean(it.get("report_nm", ""))
            kind = classify(title)
            if kind is None:
                continue
            results.append({
                "company": c["name"],
                "industry": c["industry_label"],
                "date": it.get("rcept_dt"),
                "title": title,
                "kind": kind,
                "topics": match_topics(title),
                "url": f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo={it.get('rcept_no')}",
            })

    # 최신순 → 종류 우선순위 안정정렬(정정·감사·정기 먼저, 각 그룹 내 최신순)
    results.sort(key=lambda x: x["date"] or "", reverse=True)
    results.sort(key=lambda x: PRIORITY.get(x["kind"], 9))
    DATA.mkdir(exist_ok=True)
    with open(DATA / "dart.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    kinds = {}
    for r in results:
        kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
    print(f"DART: {len(results)}건 저장 ({kinds})")


if __name__ == "__main__":
    main()
