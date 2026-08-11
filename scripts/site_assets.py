"""사이트 공통 자산(CSS/JS). build_site.py 가 docs/assets/ 로 내보낸다.

페이지가 여러 장이 되면서 스타일·스크립트를 각 HTML 에 심는 건 의미가 없어졌다.
한 곳에 모아두고 모든 페이지가 같은 파일을 참조한다.
"""

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
a{color:inherit}
.wrap{max-width:1400px;margin:0 auto;padding:0 20px 64px}

/* 상단 공통 바 */
.topbar{border-bottom:1px solid var(--line);background:var(--card);margin-bottom:26px}
.topbar .inner{max-width:1400px;margin:0 auto;padding:12px 20px;display:flex;
  align-items:center;gap:18px}
.brand{font-weight:800;font-size:15px;letter-spacing:-.01em;text-decoration:none}
.brand span{color:var(--accent)}
.nav{display:flex;gap:14px;margin-left:auto;font-size:13px}
.nav a{color:var(--muted);text-decoration:none;font-weight:600}
.nav a:hover,.nav a[aria-current=page]{color:var(--accent)}

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

#q{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:8px;
  padding:7px 12px;font:inherit;font-size:13px;width:220px}
#q:focus{outline:2px solid var(--accent);outline-offset:-1px}
.sort{display:flex;gap:4px;align-items:center}
.sort button{border:1px solid var(--line);background:var(--card);color:var(--muted);
  border-radius:6px;padding:3px 10px;font:inherit;font-size:12px;cursor:pointer}
.sort button[aria-pressed=true]{border-color:var(--accent);color:var(--accent);font-weight:700}

.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(290px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;
  box-shadow:var(--shadow);display:flex;flex-direction:column;overflow:hidden}
.card.hide{display:none}
.card-head{padding:16px 16px 0}
.chip{display:inline-block;background:var(--chip);color:var(--chip-fg);border-radius:6px;
  padding:3px 9px;font-size:11.5px;font-weight:700}
.name{font-size:18px;font-weight:700;margin:10px 0 4px;letter-spacing:-.01em}
.name a{text-decoration:none}
.name a:hover{color:var(--accent)}
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
.list li.more,.list li.nomatch{display:none}
.card.open .list li.more{display:list-item}
.card.open .list li.more.nomatch{display:none}
.list a{text-decoration:none;font-size:13.5px;line-height:1.45;display:block}
.list a:hover{color:var(--accent)}
.src{color:var(--muted);font-size:11.5px;margin-top:5px;display:flex;flex-wrap:wrap;
  align-items:center;gap:5px}
.buzz{background:var(--chip);color:var(--accent);font-weight:700;font-size:10.5px;
  border-radius:4px;padding:1px 6px}
.foot{display:flex;border-top:1px solid var(--line)}
.foot a,.foot button{flex:1;border:0;background:none;color:var(--muted);font:inherit;
  font-size:12.5px;font-weight:600;padding:12px 0;text-align:center;text-decoration:none;
  cursor:pointer}
.foot a{border-right:1px solid var(--line)}
.foot a:hover,.foot button:hover{color:var(--accent);background:var(--chip)}
.empty{color:var(--muted);font-size:13px;padding:14px 16px}
footer{margin-top:32px;color:var(--muted);font-size:12px;text-align:center;line-height:1.7}

/* ── 회사 상세 페이지 ── */
.back{display:inline-block;color:var(--muted);text-decoration:none;font-size:13px;
  font-weight:600;margin:4px 0 14px}
.back:hover{color:var(--accent)}
.hero{display:grid;grid-template-columns:300px 1fr;gap:22px;background:var(--card);
  border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-bottom:24px}
.hero .thumb{height:100%;min-height:190px;margin:0}
.hero .info{padding:20px 22px 20px 0}
.hero h1{margin:0 0 8px}
.stats{display:flex;flex-wrap:wrap;gap:10px 26px;margin-top:16px}
.stat b{display:block;font-size:22px;font-weight:800;letter-spacing:-.02em}
.stat span{color:var(--muted);font-size:12px}
.issues{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.issue{background:var(--card);border:1px solid var(--line);border-radius:12px;
  padding:14px 16px;display:grid;grid-template-columns:44px 1fr;gap:14px;align-items:start}
.issue .rank{color:var(--muted);font-size:19px;font-weight:800;text-align:center;padding-top:2px}
.issue.top .rank{color:var(--accent)}
.issue h3{margin:0 0 6px;font-size:15px;font-weight:700;line-height:1.4}
.issue h3 a{text-decoration:none}
.issue h3 a:hover{color:var(--accent)}
.outlets{color:var(--muted);font-size:11.5px;margin-top:6px;line-height:1.6}
.outlets b{color:var(--chip-fg);font-weight:600}
@media (max-width:760px){
  .hero{grid-template-columns:1fr}
  .hero .thumb{min-height:150px}
  .hero .info{padding:0 18px 18px}
}

/* ── 아카이브 ── */
.days{list-style:none;margin:0;padding:0;display:grid;gap:8px;
  grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}
.days a{display:flex;justify-content:space-between;align-items:center;background:var(--card);
  border:1px solid var(--line);border-radius:10px;padding:13px 16px;text-decoration:none;
  font-weight:600;font-size:14px}
.days a:hover{border-color:var(--accent);color:var(--accent)}
.days small{color:var(--muted);font-weight:500}
"""

JS = """
var PREVIEW = 5;

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

/* 썸네일 대체 순서: 같은 주소 재시도 2회 → 예비 후보 → 색 블록.
   한 번 실패했다고 바로 포기하면 일시적인 네트워크 오류에 카드가 빈 채로 남는다.

   error 이벤트만 믿으면 안 된다. 핫링크를 막는 언론사 중에는 거부도 응답도 하지 않고
   연결을 붙잡고만 있는 곳이 있어(조선일보 resizer) 그때는 error 가 영영 안 온다.
   그래서 타임아웃 감시를 같이 건다. 감시가 성립하려면 이미지가 즉시 로드를 시작해야
   하므로 loading=lazy 는 쓰지 않는다 — 화면 밖이라 안 받은 걸 실패로 오인하게 된다. */
var IMG_TIMEOUT = 6000;
document.querySelectorAll('.thumb img').forEach(function(img){
  var alts, tries = 0, timer = null;
  try { alts = JSON.parse(img.dataset.alts || '[]'); } catch (e) { alts = []; }
  function stop(){ if (timer){ clearTimeout(timer); timer = null; } }
  function watch(){ stop(); timer = setTimeout(fail, IMG_TIMEOUT); }
  function swap(url, source){
    img.dataset.base = url;
    img.src = url;
    var credit = img.parentNode.querySelector('.credit');
    if (credit && source !== undefined) credit.textContent = source || '';
    watch();
  }
  function fail(){
    stop();
    if (++tries <= 2){
      swap(img.dataset.base + (img.dataset.base.indexOf('?') < 0 ? '?' : '&') + 'r=' + tries);
      return;
    }
    var next = alts.shift();
    if (next){ tries = 0; swap(next.url, next.source); return; }
    img.parentNode.classList.add('noimg');
    img.remove();
  }
  img.addEventListener('load', stop);
  img.addEventListener('error', fail);
  if (!(img.complete && img.naturalWidth > 0)) watch();
});

/* 정렬을 바꾸면 '더보기'로 접히는 대상도 다시 계산해야 한다. */
function sortLists(mode){
  document.querySelectorAll('.list, .issues').forEach(function(ul){
    var items = Array.prototype.slice.call(ul.children);
    items.sort(function(a, b){
      var ta = Date.parse(a.dataset.time) || 0, tb = Date.parse(b.dataset.time) || 0;
      if (mode === 'time') return tb - ta;
      return (+b.dataset.score) - (+a.dataset.score) || tb - ta;
    });
    items.forEach(function(li, i){
      ul.appendChild(li);
      if (ul.classList.contains('list')) li.classList.toggle('more', i >= PREVIEW);
      var rank = li.querySelector('.rank');
      if (rank){ rank.textContent = i + 1; li.classList.toggle('top', i < 3); }
    });
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
  t.onclick = function(){
    var s = t.dataset.sector;
    document.querySelectorAll('.tab').forEach(function(x){
      x.setAttribute('aria-pressed', String(x === t)); });
    document.querySelectorAll('.card').forEach(function(c){
      c.classList.toggle('hide', s !== 'all' && c.dataset.sector !== s); });
  };
});
document.querySelectorAll('.toggle').forEach(function(b){
  b.onclick = function(){
    var c = b.closest('.card'), open = c.classList.toggle('open');
    b.textContent = open ? '접기' : b.dataset.label;
  };
});

/* 검색: 회사명이 걸리면 카드 전체를, 아니면 제목이 걸린 기사만 남긴다. */
var q = document.getElementById('q');
if (q) q.oninput = function(){
  var k = q.value.trim().toLowerCase();
  document.querySelectorAll('.card').forEach(function(c){
    var name = c.querySelector('.name').textContent.toLowerCase();
    var byName = !k || name.indexOf(k) >= 0, any = byName;
    c.querySelectorAll('.list li').forEach(function(li){
      var hit = byName || li.textContent.toLowerCase().indexOf(k) >= 0;
      li.classList.toggle('nomatch', !hit);
      if (hit) any = true;
    });
    c.classList.toggle('hide', !any);
  });
  if (k) document.querySelectorAll('.card').forEach(function(c){ c.classList.add('open'); });
};
"""
