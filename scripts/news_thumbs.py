"""⑤ 카드 썸네일 — 수집된 기사의 대표 이미지(og:image)를 찾아 붙인다.

news_board.py 다음에 실행한다. data/news_board.json 을 읽어 회사마다 이미지 URL을
채워 넣고 다시 저장한다. 이미지를 못 구한 회사는 그냥 비워두면 되고(렌더러가
그라디언트 블록으로 대체), 이 스크립트가 통째로 실패해도 보드는 그대로 나온다.

Google 뉴스 RSS 링크는 실제 기사 주소가 아니라 리다이렉트 URL이고, 2024년부터
base64 디코딩으로는 원문을 풀 수 없다. 그래서 기사 페이지에서 서명(sg)·타임스탬프(ts)를
꺼내 Google 내부 batchexecute 엔드포인트에 물어보는 방식을 쓴다. 비공식 경로라
언제든 막힐 수 있어 실패를 정상 흐름으로 취급한다.

결과는 data/thumbs_cache.json 에 캐시해 재실행 시 다시 안 긁는다.

환경변수:
  THUMB_TRIES   회사당 이미지 찾기를 시도할 기사 수 (기본 8)
                실패한 기사도 캐시하므로 재실행 시 이 값을 올려도 추가 요청은 없다.
"""
from __future__ import annotations
import json
import os
import re
import sys
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from common import DATA

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
H = {"User-Agent": UA, "Accept-Language": "ko-KR,ko;q=0.9"}
TRIES = int(os.environ.get("THUMB_TRIES", "8"))
CACHE = DATA / "thumbs_cache.json"

# 기사 사진이 아니라 언론사 기본 이미지인 경우가 흔하다. 이런 건 버린다.
JUNK = ("logo", "noimage", "no_image", "no-image", "default", "placeholder",
        "favicon", "blank", "share_img", "og_img", "sns_")


def resolve(rss_url: str) -> str | None:
    """Google 뉴스 리다이렉트 URL → 언론사 원문 URL."""
    aid = rss_url.rsplit("/", 1)[-1].split("?")[0]
    page = requests.get(f"https://news.google.com/rss/articles/{aid}",
                        headers=H, timeout=20).text
    sg = re.search(r'data-n-a-sg="([^"]+)"', page)
    ts = re.search(r'data-n-a-ts="([^"]+)"', page)
    if not (sg and ts):
        return None
    inner = json.dumps(["garturlreq",
                        [["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1,
                          None, None, None, None, None, 0, 1],
                         "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0],
                        aid, int(ts.group(1)), sg.group(1)])
    r = requests.post("https://news.google.com/_/DotsSplashUi/data/batchexecute",
                      headers={**H, "Content-Type":
                               "application/x-www-form-urlencoded;charset=UTF-8"},
                      data={"f.req": json.dumps([[["Fbv4je", inner, None, "generic"]]])},
                      timeout=20)
    for line in r.text.splitlines():
        if "garturlres" not in line:
            continue
        for el in json.loads(line):
            if (isinstance(el, list) and len(el) > 2 and isinstance(el[2], str)
                    and "garturlres" in el[2]):
                return json.loads(el[2])[1]
    return None


def og_image(url: str) -> str | None:
    """기사 페이지의 대표 이미지 메타태그를 읽는다."""
    r = requests.get(url, headers=H, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, "html.parser")
    for attrs in ({"property": "og:image"}, {"name": "og:image"},
                  {"name": "twitter:image"}, {"property": "twitter:image"}):
        tag = soup.find("meta", attrs=attrs)
        src = (tag or {}).get("content", "").strip() if tag else ""
        if not src:
            continue
        src = urljoin(r.url, src)
        if any(j in src.lower() for j in JUNK):
            continue          # 언론사 기본 로고 — 다음 기사로
        return src
    return None


def usable(img: str) -> bool:
    """실제로 열리는 이미지인지 확인(깨진 썸네일 방지)."""
    try:
        r = requests.get(img, headers=H, timeout=15, stream=True)
        ok = r.status_code == 200 and r.headers.get("Content-Type", "").startswith("image/")
        r.close()
        return ok
    except requests.RequestException:
        return False


def load_cache() -> dict:
    if CACHE.exists():
        with open(CACHE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def pick(company: dict, cache: dict) -> dict | None:
    """회사의 상위 기사부터 훑어 첫 번째 쓸만한 이미지를 고른다."""
    for a in company["articles"][:TRIES]:
        key = a["url"]
        if key in cache:                       # 실패(None)도 캐시해 재시도 안 함
            hit = cache[key]
            if hit:
                return hit
            continue
        found = None
        try:
            real = resolve(key)
            if real and real.startswith("http"):
                img = og_image(real)
                if img and usable(img):
                    found = {"image": img, "image_alt": a["title"],
                             "image_source": a["source"],
                             "image_host": urlparse(real).netloc}
        except Exception as e:  # noqa: BLE001  — 썸네일은 없어도 되는 정보
            print(f"    [skip] {type(e).__name__}: {str(e)[:60]}", file=sys.stderr)
        cache[key] = found
        time.sleep(0.5)
        if found:
            return found
    return None


def main() -> None:
    path = DATA / "news_board.json"
    if not path.exists():
        sys.exit("data/news_board.json 이 없습니다. news_board.py 를 먼저 실행하세요.")
    with open(path, encoding="utf-8") as f:
        d = json.load(f)

    cache = load_cache()
    ok = 0
    for s in d["sectors"]:
        for c in s["companies"]:
            hit = pick(c, cache)
            c.update(hit or {"image": "", "image_alt": "", "image_source": "",
                             "image_host": ""})
            ok += bool(hit)
            # Windows 콘솔(cp949)에서 깨지지 않게 기호는 ASCII 로만
            print(f"  {c['name']:<10} {'OK ' + c['image_host'] if hit else '-- 이미지 없음'}")

    # 수집 기간에서 빠진 기사는 다시 조회될 일이 없다. 캐시가 무한히 커지지 않게 정리.
    live = {a["url"] for s in d["sectors"] for c in s["companies"] for a in c["articles"]}
    cache = {k: v for k, v in cache.items() if k in live}

    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    print(f"썸네일: {ok}/{d['company_count']}개사 확보")


if __name__ == "__main__":
    main()
