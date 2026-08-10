"""data/news_board.json → docs/index.html (카드형 뉴스 보드).

빅카인즈 '오늘의 이슈' 배치를 참고한 회사 단위 카드 그리드.
외부 CSS/JS/폰트를 전혀 쓰지 않는 단일 HTML이라 파일을 그냥 더블클릭해도 열리고,
GitHub Pages(docs/)에 그대로 올려도 동작한다.
"""
from __future__ import annotations
import html
import json
from datetime import datetime, timezone, timedelta

from common import ROOT, DATA

KST = timezone(timedelta(hours=9))
OUT = ROOT / "docs" / "index.html"
PREVIEW = 5      # 카드에 펼쳐 보여줄 기사 수, 나머지는 '더보기'

CSS = """
:root{
  --bg:#f4f6fa; --card:#fff; --fg:#111827; --muted:#6b7280; --line:#e5e7eb;
  --accent:#2563eb; --chip:#eef2f7; --chip-fg:#4b5563; --shadow:0 1px 3px rgba(16,24,40,.08);
}
@media (prefers-color-scheme:dark){
  :root{ --bg:#0f1115; --card:#171a21; --fg:#e5e7eb; --muted:#9aa3b2; --line:#262b36;
         --accent:#60a5fa; --chip:#222733; --chip-fg:#c2c9d6; --shadow:none; }
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Malgun Gothic","Apple SD Gothic Neo",
  "Noto Sans KR",sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:1400px;margin:0 auto;padding:28px 20px 64px}

header{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px 16px;margin-bottom:6px}
h1{font-size:26px;font-weight:800;margin:0;letter-spacing:-.02em}
.tabs{margin-left:auto;display:flex;flex-wrap:wrap;gap:6px}
.tab{border:1px solid var(--line);background:var(--card);color:var(--muted);
  border-radius:999px;padding:6px 14px;font-size:13px;cursor:pointer;font-weight:600}
.tab:hover{color:var(--fg)}
.tab[aria-pressed=true]{background:var(--accent);border-color:var(--accent);color:#fff}
.meta{display:flex;flex-wrap:wrap;gap:8px 16px;color:var(--muted);font-size:13px;
  padding-bottom:16px;border-bottom:1px solid var(--line);margin-bottom:20px}
.meta b{color:var(--fg)}
.meta .right{margin-left:auto}

.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(290px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;
  box-shadow:var(--shadow);display:flex;flex-direction:column;overflow:hidden}
.card.hide{display:none}
.card-head{padding:16px 16px 0}
.chip{display:inline-block;background:var(--chip);color:var(--chip-fg);border-radius:6px;
  padding:3px 9px;font-size:11.5px;font-weight:700}
.name{font-size:18px;font-weight:700;margin:10px 0 4px;letter-spacing:-.01em}
.count{color:var(--accent);font-size:13px;font-weight:700}
.count .code{color:var(--muted);font-weight:500;margin-left:6px}
.thumb{position:relative;height:150px;margin:12px 0 0;overflow:hidden;
  display:flex;align-items:center;justify-content:center}
.thumb .ph{font-size:30px;font-weight:800;color:#fff;letter-spacing:-.02em;
  text-shadow:0 1px 8px rgba(0,0,0,.25)}
.thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.thumb .credit{position:absolute;right:8px;bottom:7px;background:rgba(17,24,39,.62);color:#fff;
  font-size:10.5px;padding:2px 7px;border-radius:5px;backdrop-filter:blur(2px)}
.thumb.noimg .credit{display:none}
.list{list-style:none;margin:0;padding:12px 16px;flex:1}
.list li{padding:9px 0;border-bottom:1px dashed var(--line)}
.list li:last-child{border-bottom:0}
.list li.more{display:none}
.card.open .list li.more{display:list-item}
.list a{color:inherit;text-decoration:none;font-size:13.5px;line-height:1.45;display:block}
.list a:hover{color:var(--accent)}
.src{color:var(--muted);font-size:11.5px;margin-top:5px;display:flex;flex-wrap:wrap;
  align-items:center;gap:5px}
.buzz{background:var(--chip);color:var(--accent);font-weight:700;font-size:10.5px;
  border-radius:4px;padding:1px 6px}
.sort{display:flex;gap:4px;align-items:center}
.sort button{border:1px solid var(--line);background:var(--card);color:var(--muted);
  border-radius:6px;padding:3px 10px;font:inherit;font-size:12px;cursor:pointer}
.sort button[aria-pressed=true]{border-color:var(--accent);color:var(--accent);font-weight:700}
.foot{display:flex;border-top:1px solid var(--line)}
.foot a,.foot button{flex:1;border:0;background:none;color:var(--muted);font:inherit;font-size:12.5px;
  font-weight:600;padding:12px 0;text-align:center;text-decoration:none;cursor:pointer}
.foot a{border-right:1px solid var(--line)}
.foot a:hover,.foot button:hover{color:var(--accent);background:var(--chip)}
.empty{color:var(--muted);font-size:13px;padding:14px 16px}
footer{margin-top:32px;color:var(--muted);font-size:12px;text-align:center}
"""

JS = """
var PREVIEW = %d;

/* '3시간 전' 은 파일을 언제 열든 맞아야 하므로 렌더 시각이 아니라 브라우저 시각으로
   다시 계산한다. 서버에서 찍어둔 값은 JS 가 꺼져 있을 때의 대비책. */
function fmtAgo(ms){
  if (ms < 0) return '방금';
  var m = Math.floor(ms/60000);
  if (m < 1) return '방금';
  if (m < 60) return m + '분 전';
  var h = Math.floor(m/60);
  if (h < 24) return h + '시간 전';
  var d = Math.floor(h/24);
  return d < 7 ? d + '일 전' : Math.floor(d/7) + '주 전';
}
function refreshAgo(){
  var now = Date.now();
  document.querySelectorAll('time.ago').forEach(function(t){
    var at = Date.parse(t.getAttribute('datetime'));
    if (at) t.textContent = fmtAgo(now - at);
  });
}
refreshAgo();
setInterval(refreshAgo, 60000);

/* 정렬을 바꾸면 '더보기'로 접히는 대상도 다시 계산해야 한다. */
function sortLists(mode){
  document.querySelectorAll('.list').forEach(function(ul){
    var items = Array.prototype.slice.call(ul.children);
    items.sort(function(a, b){
      var ta = Date.parse(a.dataset.time) || 0, tb = Date.parse(b.dataset.time) || 0;
      if (mode === 'time') return tb - ta;
      return (+b.dataset.score) - (+a.dataset.score) || tb - ta;
    });
    /* 펼침 상태는 .card.open 이 CSS 로 처리하므로 여기서는 순번만 본다. */
    items.forEach(function(li, i){ ul.appendChild(li); li.classList.toggle('more', i >= PREVIEW); });
  });
}
document.querySelectorAll('.sort button').forEach(function(b){
  b.onclick = function(){
    document.querySelectorAll('.sort button').forEach(function(x){
      x.setAttribute('aria-pressed', String(x === b)); });
    sortLists(b.dataset.mode);
  };
});

document.querySelectorAll('.tab').forEach(function(t){
  t.onclick=function(){
    var s=t.dataset.sector;
    document.querySelectorAll('.tab').forEach(function(x){
      x.setAttribute('aria-pressed', String(x===t)); });
    document.querySelectorAll('.card').forEach(function(c){
      c.classList.toggle('hide', s!=='all' && c.dataset.sector!==s); });
  };
});
document.querySelectorAll('.toggle').forEach(function(b){
  b.onclick=function(){
    var c=b.closest('.card'), open=c.classList.toggle('open');
    b.textContent = open ? '접기' : b.dataset.label;
  };
});
"""


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


def initials(name: str) -> str:
    """썸네일에 넣을 짧은 표기 — 한글은 앞 2자, 영문은 첫 단어."""
    head = name.split()[0].rstrip(".")
    return head[:2] if any("가" <= ch <= "힣" for ch in head) else head[:6]


def thumb(firm: dict, color: str) -> str:
    """기사 사진이 있으면 그걸 쓰고, 없거나 로딩에 실패하면 분야색 블록으로 떨어진다.

    referrerpolicy=no-referrer 는 일부 언론사의 외부참조 차단을 피하기 위한 것.
    """
    e = html.escape
    grad = f"background:linear-gradient(135deg,{color},{color}99)"
    layers = [f'<span class="ph">{e(initials(firm["name"]))}</span>']
    if firm.get("image"):
        layers.append(
            f'<img src="{e(firm["image"])}" alt="{e(firm.get("image_alt", ""))}" '
            f'loading="lazy" referrerpolicy="no-referrer" '
            f'onerror="this.parentNode.classList.add(&quot;noimg&quot;);this.remove()">')
        if firm.get("image_source"):
            layers.append(f'<span class="credit">{e(firm["image_source"])}</span>')
    return f'<div class="thumb" style="{grad}">{"".join(layers)}</div>'


def card(firm: dict, sector: dict, now: datetime) -> str:
    e = html.escape
    color = sector["color"]
    items = []
    for i, a in enumerate(firm["articles"]):
        cls = ' class="more"' if i >= PREVIEW else ""
        # 시각은 JS 가 열람 시점 기준으로 다시 채운다. 여기 값은 JS 없을 때의 대비책.
        when = (f'<time class="ago" datetime="{e(a["published"])}">'
                f'{ago(a["published"], now)}</time>') if a["published"] else ""
        n = a.get("outlet_count", 1)
        buzz = f'<span class="buzz">{n}개 언론사</span>' if n > 1 else ""
        meta = "".join(x for x in (f'<span>{e(a["source"])}</span>' if a["source"] else "",
                                   "<span>·</span>" if a["source"] and when else "",
                                   when, buzz) if x)
        items.append(
            f'<li{cls} data-score="{a.get("score", 0)}" data-time="{e(a["published"])}">'
            f'<a href="{e(a["url"])}" target="_blank" rel="noopener">{e(a["title"])}</a>'
            f'<div class="src">{meta}</div></li>')
    body = ("<ul class=\"list\">" + "".join(items) + "</ul>") if items else \
           '<div class="empty">기간 내 수집된 기사가 없습니다.</div>'

    rest = len(firm["articles"]) - PREVIEW
    more = (f'<button class="toggle" data-label="기사 {rest}건 더보기">기사 {rest}건 더보기</button>'
            if rest > 0 else '<button class="toggle" data-label="더보기" disabled>&nbsp;</button>')
    bits = [f'{firm["found"]}건']
    if firm.get("story_count"):
        bits.append(f'{firm["story_count"]}개 이슈')
    code = f'<span class="code">{e(firm["stock_code"])}</span>' if firm["stock_code"] else ""

    return f"""<article class="card" data-sector="{e(sector['name'])}">
  <div class="card-head">
    <span class="chip">{e(sector['name'])}</span>
    <div class="name">{e(firm['name'])}</div>
    <div class="count">{' · '.join(bits)}{code}</div>
  </div>
  {thumb(firm, color)}
  {body}
  <div class="foot">
    <a href="{e(firm['search_url'])}" target="_blank" rel="noopener">전체 뉴스보기</a>
    {more}
  </div>
</article>"""


def main() -> None:
    with open(DATA / "news_board.json", encoding="utf-8") as f:
        d = json.load(f)
    now = datetime.fromisoformat(d["generated_at"])

    tabs = ['<button class="tab" data-sector="all" aria-pressed="true">전체</button>']
    cards = []
    for s in d["sectors"]:
        tabs.append(f'<button class="tab" data-sector="{html.escape(s["name"])}">'
                    f'{html.escape(s["name"])}</button>')
        cards += [(c["found"], card(c, s, now)) for c in s["companies"]]
    cards.sort(key=lambda x: x[0], reverse=True)   # 뉴스 많은 회사부터

    doc = f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TMT 뉴스 보드</title>
<style>{CSS}</style></head><body><div class="wrap">
<header><h1>오늘의 이슈</h1>
<div class="tabs">{''.join(tabs)}</div></header>
<div class="meta">
  <span>분석 대상 뉴스 <b>{d['total_articles']:,}건</b> / 대상 기업 <b>{d['company_count']}개사</b></span>
  <span class="sort">기사 정렬
    <button data-mode="buzz" aria-pressed="true">화제도순</button>
    <button data-mode="time" aria-pressed="false">최신순</button>
  </span>
  <span class="right">분석기준 {d['period_from']} ~ {d['period_to']} · 갱신
    <time class="ago" datetime="{d['generated_at']}">{now.strftime('%m.%d %H:%M')}</time></span>
</div>
<div class="grid">{''.join(c for _, c in cards)}</div>
<footer>Google 뉴스 RSS 기반 · 화제도 = 같은 사건을 보도한 언론사 수 + 매체 · 최신성 · Google 노출순위<br>
클릭수·반응수는 공개 데이터가 없어 위 대리 지표로 산출합니다 · TMT Research Radar</footer>
</div><script>{JS % PREVIEW}</script></body></html>"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(doc, encoding="utf-8")
    print(f"뉴스 보드 렌더 완료 → {OUT.relative_to(ROOT)} ({len(cards)}개 카드)")


if __name__ == "__main__":
    main()
