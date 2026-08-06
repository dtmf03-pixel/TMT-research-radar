"""수집 결과(data/*.json)를 README 대시보드로 렌더링.

README.md 의 <!--RADAR:START--> ~ <!--RADAR:END--> 구간을 자동 갱신한다.
GITHUB Actions 가 매주 실행 → 커밋하면, 커밋 히스토리 자체가 리서치 로그가 된다.
"""
from __future__ import annotations
import json
import os
from datetime import datetime, timezone, timedelta

from common import ROOT, DATA

KST = timezone(timedelta(hours=9))
START, END = "<!--RADAR:START-->", "<!--RADAR:END-->"


def load(name: str) -> list[dict]:
    p = DATA / name
    if not p.exists():
        return []
    with open(p, encoding="utf-8") as f:
        return json.load(f)


KIND_BADGE = {"정정": "🔴정정", "감사": "🟠감사", "정기보고서": "📘정기",
              "주요사항": "🟡주요사항", "회계이슈": "🔵이슈", "실적": "실적"}


PER_KIND_CAP = 10   # 한 종류가 표를 도배하지 않도록 제한


def section_dart(rows: list[dict]) -> str:
    if not rows:
        return "> DART 수집 결과 없음 (DART_API_KEY 설정 후 실행)\n"
    counts = {r["kind"]: 0 for r in rows}
    summary = " · ".join(f"{KIND_BADGE.get(k,k)} {v}"
                         for k, v in sorted(((k, sum(1 for r in rows if r['kind']==k))
                                             for k in {r['kind'] for r in rows})))
    out = [f"_종류별: {summary}_\n",
           "| 종류 | 업종 | 기업 | 일자 | 공시 |", "|---|---|---|---|---|"]
    shown = {}
    for r in rows:
        k = r["kind"]
        if shown.get(k, 0) >= PER_KIND_CAP:
            continue
        shown[k] = shown.get(k, 0) + 1
        badge = KIND_BADGE.get(k, k)
        out.append(f"| {badge} | {r['industry']} | {r['company']} | {r.get('date','')} | "
                   f"[{r['title'][:44]}]({r['url']}) |")
    return "\n".join(out) + "\n"


NEWS_BADGE = {"회계신호": "🔴회계신호", "회계이슈": "🔵회계이슈", "일반": "일반"}
NEWS_PER_KIND_CAP = {"회계신호": 30, "회계이슈": 20, "일반": 20}


def section_news(rows: list[dict]) -> str:
    if not rows:
        return "> 뉴스 수집 결과 없음 (news_monitor.py 실행 후 채워짐)\n"
    counts = {k: sum(1 for r in rows if r.get("kind") == k) for k in ["회계신호", "회계이슈", "일반"]}
    summary = " · ".join(f"{NEWS_BADGE[k]} {v}" for k, v in counts.items() if v)
    out = [f"_구분: {summary}_\n",
           "| 구분 | 업종 | 기업 | 기사 | 회계토픽 | 출처 |", "|---|---|---|---|---|---|"]
    shown = {}
    for r in rows:
        k = r.get("kind", "일반")
        if shown.get(k, 0) >= NEWS_PER_KIND_CAP.get(k, 20):
            continue
        shown[k] = shown.get(k, 0) + 1
        badge = NEWS_BADGE.get(k, k)
        topics = ", ".join(r.get("topics") or []) or "-"
        src = r.get("source", "")
        out.append(f"| {badge} | {r['industry']} | {r['company']} | "
                   f"[{r['title'][:42]}]({r['url']}) | {topics} | {src} |")
    return "\n".join(out) + "\n"


def section_reports(rows: list[dict]) -> str:
    if not rows:
        return "> 회계법인 리포트 수집 결과 없음\n"
    out = ["| 법인 | 리포트 |", "|---|---|"]
    for r in rows[:20]:
        out.append(f"| {r['firm']} | [{r['title'][:60]}]({r['url']}) |")
    return "\n".join(out) + "\n"


def main() -> None:
    dart, news, reports = load("dart.json"), load("news.json"), load("reports.json")
    now = datetime.now(KST).strftime("%Y-%m-%d %H:%M KST")

    body = [
        f"_최종 갱신: {now}_\n",
        f"**수집 현황** — DART 공시 {len(dart)} · 뉴스 {len(news)} · 회계법인 리포트 {len(reports)}\n",
        "### 📄 DART 공시 (회계 이슈 필터)", section_dart(dart),
        "### 📰 뉴스 모니터링 (🔴 = 감사·재무제표 신호)", section_news(news),
        "### 🏢 회계법인 산업 리포트", section_reports(reports),
    ]
    block = f"{START}\n" + "\n".join(body) + f"\n{END}"

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    if START in text and END in text:
        pre = text.split(START)[0]
        post = text.split(END)[1]
        readme.write_text(pre + block + post, encoding="utf-8")
    else:
        readme.write_text(text.rstrip() + "\n\n" + block + "\n", encoding="utf-8")
    print("README 대시보드 갱신 완료")


if __name__ == "__main__":
    main()
