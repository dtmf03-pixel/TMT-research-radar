"""data/news_board.json → docs/ 정적 사이트.

  docs/index.html                메인 보드 (11개사 카드 + 검색 + 분야 탭)
  docs/company/<slug>.html       회사별 상세 — 수집한 이슈 전량과 보도 매체
  docs/archive/YYYY-MM-DD.html   그날의 보드 스냅샷
  docs/archive/index.html        스냅샷 목록
  docs/assets/site.{css,js}      공통 자산

빌드 때마다 오늘치 스냅샷 한 장을 추가하고 목록을 다시 만든다. 과거 스냅샷은
건드리지 않으므로 매일 돌려도 그날 파일만 늘어난다.
"""
from __future__ import annotations
import html
import json
import re
from datetime import datetime, timezone, timedelta

from common import ROOT, DATA
from site_assets import CSS, JS

KST = timezone(timedelta(hours=9))
DOCS = ROOT / "docs"
PREVIEW = 5          # 메인 카드에 펼쳐 보여줄 기사 수
CARD_MAX = 12        # 메인 카드가 담는 최대 기사 수 (나머지는 상세 페이지에서)
SITE = "TMT Research Radar"


# ────────────────────────────── 공통 ──────────────────────────────

def ago(iso: str, now: datetime) -> str:
    if not iso:
        return ""
    try:
        d = datetime.fromisoformat(iso)
    except ValueError:
        return ""
    sec = (now - d).total_seconds()
    if sec < 3600:
        return f"{max(int(sec // 60), 1)}분 전"
    if sec < 86400:
        return f"{int(sec // 3600)}시간 전"
    return f"{int(sec // 86400)}일 전"


def when_tag(iso: str, now: datetime) -> str:
    """열람 시점 기준으로 JS 가 다시 채우는 시각. 안의 값은 JS 없을 때의 대비책."""
    if not iso:
        return ""
    return f'<time class="ago" datetime="{html.escape(iso)}">{ago(iso, now)}</time>'


def initials(name: str) -> str:
    head = name.split()[0].rstrip(".")
    return head[:2] if any("가" <= ch <= "힣" for ch in head) else head[:6]


def page(title: str, body: str, root: str, nav: str = "") -> str:
    """모든 페이지 공통 뼈대. root 는 docs/ 까지의 상대 경로("" 또는 "../")."""
    e = html.escape
    return f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<link rel="stylesheet" href="{root}assets/site.css"></head><body>
<div class="topbar"><div class="inner">
  <a class="brand" href="{root}index.html">TMT <span>Research Radar</span></a>
  <nav class="nav">
    <a href="{root}index.html"{' aria-current="page"' if nav == 'board' else ''}>뉴스 보드</a>
    <a href="{root}archive/index.html"{' aria-current="page"' if nav == 'archive' else ''}>아카이브</a>
    <a href="https://github.com/dtmf03-pixel/TMT-research-radar" target="_blank"
       rel="noopener">저장소</a>
  </nav>
</div></div>
<div class="wrap">
{body}
<footer>Google 뉴스 RSS 기반 · 화제도 = 같은 사건을 보도한 언론사 수 + 매체 · 최신성 · Google 노출순위<br>
클릭수·반응수는 공개 데이터가 없어 위 대리 지표로 산출합니다 · {e(SITE)}</footer>
</div><script src="{root}assets/site.js"></script></body></html>"""


# ────────────────────────────── 카드 ──────────────────────────────

def thumb(firm: dict, color: str, root: str) -> str:
    """기사 사진. 실패하면 재시도 → 예비 후보 → 색 블록 순으로 물러난다."""
    e = html.escape
    grad = f"background:linear-gradient(135deg,{color},{color}99)"
    layers = [f'<span class="ph">{e(initials(firm["name"]))}</span>']
    images = firm.get("images") or ([{"image": firm["image"],
                                      "image_source": firm.get("image_source", ""),
                                      "image_alt": firm.get("image_alt", "")}]
                                    if firm.get("image") else [])
    if images:
        first, rest = images[0], images[1:]
        alts = json.dumps([{"url": i["image"], "source": i.get("image_source", "")}
                           for i in rest], ensure_ascii=False)
        layers.append(
            f'<img src="{e(first["image"])}" data-base="{e(first["image"])}" '
            # loading=lazy 는 쓰지 않는다 — 로드가 시작돼야 site.js 의 타임아웃 감시가
            # 성립한다. 페이지당 이미지가 열몇 장이라 즉시 받아도 부담이 없다.
            f'data-alts="{e(alts)}" alt="{e(first.get("image_alt", ""))}" '
            f'referrerpolicy="no-referrer">')
        layers.append(f'<span class="credit">{e(first.get("image_source", ""))}</span>')
    return f'<div class="thumb" style="{grad}">{"".join(layers)}</div>'


def article_li(a: dict, now: datetime, cls: str = "") -> str:
    e = html.escape
    n = a.get("outlet_count", 1)
    buzz = f'<span class="buzz">{n}개 언론사</span>' if n > 1 else ""
    when = when_tag(a["published"], now)
    src = "".join(x for x in (f'<span>{e(a["source"])}</span>' if a["source"] else "",
                              "<span>·</span>" if a["source"] and when else "",
                              when, buzz) if x)
    return (f'<li{cls} data-score="{a.get("score", 0)}" data-time="{e(a["published"])}">'
            f'<a href="{e(a["url"])}" target="_blank" rel="noopener">{e(a["title"])}</a>'
            f'<div class="src">{src}</div></li>')


def card(firm: dict, sector: dict, now: datetime, root: str, linked: bool = True) -> str:
    e = html.escape
    shown = firm["articles"][:CARD_MAX]
    items = [article_li(a, now, ' class="more"' if i >= PREVIEW else "")
             for i, a in enumerate(shown)]
    body = ('<ul class="list">' + "".join(items) + "</ul>") if items else \
           '<div class="empty">기간 내 수집된 기사가 없습니다.</div>'

    rest = len(shown) - PREVIEW
    more = (f'<button class="toggle" data-label="기사 {rest}건 더보기">기사 {rest}건 더보기</button>'
            if rest > 0 else '<button class="toggle" data-label="더보기" disabled>&nbsp;</button>')
    code = f'<span class="code">{e(firm["stock_code"])}</span>' if firm["stock_code"] else ""
    bits = [f'{firm["found"]}건']
    if firm.get("story_count"):
        bits.append(f'{firm["story_count"]}개 이슈')

    detail = f'{root}company/{firm["slug"]}.html' if firm.get("slug") else ""
    name = (f'<a href="{e(detail)}">{e(firm["name"])}</a>'
            if detail and linked else e(firm["name"]))
    left = (f'<a href="{e(detail)}">상세 보기</a>' if detail and linked
            else f'<a href="{e(firm["search_url"])}" target="_blank" rel="noopener">전체 뉴스보기</a>')

    return f"""<article class="card" data-sector="{e(sector['name'])}">
  <div class="card-head">
    <span class="chip">{e(sector['name'])}</span>
    <div class="name">{name}</div>
    <div class="count">{' · '.join(bits)}{code}</div>
  </div>
  {thumb(firm, sector['color'], root)}
  {body}
  <div class="foot">{left}{more}</div>
</article>"""


def board_body(d: dict, now: datetime, root: str, heading: str,
               linked: bool = True, search: bool = True) -> str:
    tabs = ['<button class="tab" data-sector="all" aria-pressed="true">전체</button>']
    cards = []
    for s in d["sectors"]:
        tabs.append(f'<button class="tab" data-sector="{html.escape(s["name"])}">'
                    f'{html.escape(s["name"])}</button>')
        cards += [(c["found"], card(c, s, now, root, linked)) for c in s["companies"]]
    cards.sort(key=lambda x: x[0], reverse=True)

    box = ('<input id="q" type="search" placeholder="회사·기사 제목 검색" '
           'autocomplete="off">') if search else ""
    return f"""<header><h1>{html.escape(heading)}</h1>
<div class="tabs">{''.join(tabs)}</div></header>
<div class="meta">
  <span>분석 대상 뉴스 <b>{d['total_articles']:,}건</b> / 대상 기업 <b>{d['company_count']}개사</b></span>
  {box}
  <span class="sort">기사 정렬
    <button data-mode="buzz" aria-pressed="true">화제도순</button>
    <button data-mode="time" aria-pressed="false">최신순</button>
  </span>
  <span class="right">분석기준 {d['period_from']} ~ {d['period_to']} · 갱신
    <time class="ago" datetime="{d['generated_at']}">{now.strftime('%m.%d %H:%M')}</time></span>
</div>
<div class="grid">{''.join(c for _, c in cards)}</div>"""


# ───────────────────────── 회사 상세 페이지 ─────────────────────────

def company_page(firm: dict, sector: dict, d: dict, now: datetime) -> str:
    e = html.escape
    arts = firm["articles"]
    top = max((a.get("outlet_count", 1) for a in arts), default=0)

    rows = []
    for i, a in enumerate(arts):
        outlets = a.get("outlet_count", 1)
        note = (f'<div class="outlets"><b>{outlets}개 언론사</b>가 같은 사건을 보도'
                f' · 화제도 {a.get("score", 0)}점</div>') if outlets > 1 else \
               f'<div class="outlets">단독 보도 · 화제도 {a.get("score", 0)}점</div>'
        rows.append(
            f'<li class="issue{" top" if i < 3 else ""}" data-score="{a.get("score", 0)}"'
            f' data-time="{e(a["published"])}">'
            f'<div class="rank">{i + 1}</div><div>'
            f'<h3><a href="{e(a["url"])}" target="_blank" rel="noopener">{e(a["title"])}</a></h3>'
            f'<div class="src"><span>{e(a["source"])}</span><span>·</span>'
            f'{when_tag(a["published"], now)}</div>{note}</div></li>')

    body = f"""<a class="back" href="../index.html">← 뉴스 보드</a>
<div class="hero">
  {thumb(firm, sector['color'], '../')}
  <div class="info">
    <span class="chip">{e(sector['name'])}</span>
    <h1>{e(firm['name'])}</h1>
    <div class="count">{e(firm['stock_code'])}</div>
    <div class="stats">
      <div class="stat"><b>{firm['found']}</b><span>수집 기사</span></div>
      <div class="stat"><b>{firm.get('story_count', len(arts))}</b><span>이슈</span></div>
      <div class="stat"><b>{top}</b><span>최다 보도 언론사</span></div>
    </div>
    <div class="stats" style="margin-top:14px">
      <a class="chip" href="{e(firm['search_url'])}" target="_blank" rel="noopener"
         style="text-decoration:none">Google 뉴스에서 전체 보기 →</a>
    </div>
  </div>
</div>
<div class="meta">
  <span>{d['period_from']} ~ {d['period_to']} 수집 · 아래는 화제도순 상위 <b>{len(arts)}개 이슈</b></span>
  <span class="sort right">정렬
    <button data-mode="buzz" aria-pressed="true">화제도순</button>
    <button data-mode="time" aria-pressed="false">최신순</button>
  </span>
</div>
<ul class="issues">{''.join(rows)}</ul>"""
    return page(f"{firm['name']} 뉴스 · {SITE}", body, "../", nav="board")


# ────────────────────────────── 아카이브 ──────────────────────────────

def archive_index(now: datetime) -> str:
    days = sorted((p for p in (DOCS / "archive").glob("*.html")
                   if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.stem)), reverse=True)
    if days:
        items = "".join(
            f'<li><a href="{p.name}">{p.stem}'
            f'<small>{"오늘" if p.stem == now.strftime("%Y-%m-%d") else ""}</small></a></li>'
            for p in days)
        listing = f'<ul class="days">{items}</ul>'
    else:
        listing = '<div class="empty">아직 저장된 스냅샷이 없습니다.</div>'
    body = f"""<header><h1>아카이브</h1></header>
<div class="meta"><span>매일 갱신 시점의 보드를 그대로 저장합니다 ·
  <b>{len(days)}일치</b></span></div>
{listing}"""
    return page(f"아카이브 · {SITE}", body, "../", nav="archive")


# ────────────────────────────── 빌드 ──────────────────────────────

def main() -> None:
    with open(DATA / "news_board.json", encoding="utf-8") as f:
        d = json.load(f)
    now = datetime.fromisoformat(d["generated_at"])

    (DOCS / "assets").mkdir(parents=True, exist_ok=True)
    (DOCS / "company").mkdir(exist_ok=True)
    (DOCS / "archive").mkdir(exist_ok=True)
    # GitHub Pages 가 Jekyll 처리를 건너뛰게 한다. 지금 구조는 문제가 없지만
    # 밑줄로 시작하는 파일·폴더를 나중에 넣으면 Jekyll 이 조용히 빼먹는다.
    (DOCS / ".nojekyll").touch()
    (DOCS / "assets" / "site.css").write_text(CSS, encoding="utf-8")
    (DOCS / "assets" / "site.js").write_text(JS.replace("var PREVIEW = 5;",
                                                        f"var PREVIEW = {PREVIEW};"),
                                             encoding="utf-8")

    # 메인
    (DOCS / "index.html").write_text(
        page(f"오늘의 이슈 · {SITE}",
             board_body(d, now, "", "오늘의 이슈"), "", nav="board"),
        encoding="utf-8")

    # 회사 상세
    made = 0
    for s in d["sectors"]:
        for c in s["companies"]:
            if not c.get("slug"):
                continue
            (DOCS / "company" / f"{c['slug']}.html").write_text(
                company_page(c, s, d, now), encoding="utf-8")
            made += 1

    # 오늘치 스냅샷 + 목록. 스냅샷은 그날 상태 보존이 목적이라 검색·상세링크는 뺀다.
    stamp = now.strftime("%Y-%m-%d")
    (DOCS / "archive" / f"{stamp}.html").write_text(
        page(f"{stamp} 뉴스 보드 · {SITE}",
             '<a class="back" href="index.html">← 아카이브</a>'
             + board_body(d, now, "../", f"{stamp} 뉴스 보드", linked=False, search=False),
             "../", nav="archive"),
        encoding="utf-8")
    (DOCS / "archive" / "index.html").write_text(archive_index(now), encoding="utf-8")

    print(f"사이트 빌드 완료 → docs/ (메인 1 + 회사 {made} + 아카이브 {stamp})")


if __name__ == "__main__":
    main()
