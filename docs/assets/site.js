
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
