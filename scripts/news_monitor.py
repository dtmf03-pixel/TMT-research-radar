"""② 뉴스 모니터링 — Google 뉴스 RSS (API 키 불필요).

회사별로 두 갈래로 수집한다.
  (A) 일반 주요 뉴스: '"회사명"' 최근 상위 기사 (회계 키워드가 없어도 수집)
  (B) 회계 이슈 뉴스: '"회사명" (회계 OR 감사 OR ...)' 로 회계 관련 기사 더 넓게
각 기사를 회계신호(🔴)/회계이슈(🔵)/일반 으로 태깅하고, 회계 관련을 상단 정렬.
키가 필요 없어 GitHub Actions에서 secret 없이 그대로 동작.
결과 → data/news.json
"""
from __future__ import annotations
import json
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET

import requests

from common import companies, match_topics, has_audit_signal, clean, DATA

RSS = "https://news.google.com/rss/search"
HEADERS = {"User-Agent": "Mozilla/5.0 (audit-research-radar)"}

ISSUE_OR = "회계 OR 감사 OR 재무제표 OR 무형자산 OR 수익인식 OR 손상 OR 리스 OR 영업권"
GENERAL_WINDOW = "when:30d"   # 일반 주요 뉴스: 최근 30일
ISSUE_WINDOW = "when:90d"     # 회계 이슈: 최근 90일(더 넓게)
GENERAL_MAX = 5               # 회사당 일반 주요 뉴스 상위 N
ISSUE_MAX = 8                 # 회사당 회계 이슈 최대


def fetch(query: str) -> list[dict]:
    q = urllib.parse.quote(query)
    url = f"{RSS}?q={q}&hl=ko&gl=KR&ceid=KR:ko"
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    out = []
    for it in root.findall(".//item"):
        title = clean(it.findtext("title"))
        link = it.findtext("link")
        if not (title and link):
            continue
        src = it.find("source")
        out.append({
            "title": title,
            "url": link,
            "date": it.findtext("pubDate") or "",
            "source": clean(src.text) if src is not None else "",
            "summary": clean(it.findtext("description")),
        })
    return out


def tag(blob: str) -> tuple[str, list[str], bool]:
    topics = match_topics(blob)
    signal = has_audit_signal(blob)
    if signal:
        return "회계신호", topics, True
    if topics:
        return "회계이슈", topics, False
    return "일반", topics, False


def main() -> None:
    seen: set[str] = set()
    results = []
    for c in companies():
        name = c["name"]
        # (A) 일반 주요 뉴스
        try:
            general = fetch(f'"{name}" {GENERAL_WINDOW}')[:GENERAL_MAX]
        except Exception as e:  # noqa: BLE001
            print(f"[warn] {name} general: {e}", file=sys.stderr)
            general = []
        time.sleep(0.8)
        # (B) 회계 이슈 뉴스
        try:
            issue = fetch(f'"{name}" ({ISSUE_OR}) {ISSUE_WINDOW}')
        except Exception as e:  # noqa: BLE001
            print(f"[warn] {name} issue: {e}", file=sys.stderr)
            issue = []
        time.sleep(0.8)

        # 회계 이슈 먼저(우선), 그다음 일반. 회계 이슈는 태그가 붙는 것만.
        issue_kept = 0
        for it in issue:
            if issue_kept >= ISSUE_MAX:
                break
            kind, topics, signal = tag(f"{it['title']} {it['summary']}")
            if kind == "일반":
                continue
            if it["url"] in seen:
                continue
            seen.add(it["url"]); issue_kept += 1
            results.append({**it, "company": name, "industry": c["industry_label"],
                            "kind": kind, "topics": topics, "audit_signal": signal})
        for it in general:
            if it["url"] in seen:
                continue
            kind, topics, signal = tag(f"{it['title']} {it['summary']}")
            seen.add(it["url"])
            results.append({**it, "company": name, "industry": c["industry_label"],
                            "kind": kind, "topics": topics, "audit_signal": signal})

    order = {"회계신호": 0, "회계이슈": 1, "일반": 2}
    results.sort(key=lambda x: order.get(x["kind"], 3))
    DATA.mkdir(exist_ok=True)
    with open(DATA / "news.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    counts = {k: sum(1 for r in results if r["kind"] == k) for k in order}
    print(f"뉴스: {len(results)}건 저장 ({counts})")


if __name__ == "__main__":
    main()
