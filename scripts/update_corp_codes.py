"""DART corp_code(고유번호) 자동 채우기 — 회사명 매칭 기반.

DART corpCode.xml(전체 기업 매핑)을 받아 companies.yml 의 '회사명'으로 corp_code 를 채운다.
상장사는 stock_code 도 백필한다. 비상장 외감법인이 많아 종목코드보다 회사명 매칭이 안전하다.

- 이름은 공백·특수문자를 제거해 정규화 후 비교한다.
- 매칭 실패/중복은 로그로 보고한다(추측으로 채우지 않음).
"""
from __future__ import annotations
import io
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

import requests
import yaml

from common import CONFIG

API = "https://opendart.fss.or.kr/api/corpCode.xml"


def norm(s: str) -> str:
    """공백/괄호/기호 제거 + 소문자화 후 흔한 법인격 표기 제거."""
    s = re.sub(r"[\s()\[\]·.,'\"-]", "", (s or "").lower())
    s = s.replace("주식회사", "").replace("(주)", "")
    return s


def load_maps(key: str):
    r = requests.get(API, params={"crtfc_key": key}, timeout=60)
    r.raise_for_status()
    zf = zipfile.ZipFile(io.BytesIO(r.content))
    root = ET.fromstring(zf.read(zf.namelist()[0]))
    by_name: dict[str, list[dict]] = {}
    by_stock: dict[str, dict] = {}
    for node in root.iter("list"):
        corp = (node.findtext("corp_code") or "").strip()
        name = (node.findtext("corp_name") or "").strip()
        stock = (node.findtext("stock_code") or "").strip()
        if not corp or not name:
            continue
        rec = {"corp_code": corp, "corp_name": name, "stock_code": stock}
        by_name.setdefault(norm(name), []).append(rec)
        if stock:
            by_stock[stock] = rec
    return by_name, by_stock


def main() -> None:
    key = os.environ.get("DART_API_KEY")
    if not key:
        print("DART_API_KEY 미설정", file=sys.stderr)
        sys.exit(1)

    by_name, by_stock = load_maps(key)
    path = CONFIG / "companies.yml"
    with open(path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    filled, unmatched, ambiguous = 0, [], []
    for firms in cfg.values():
        for c in firms:
            if c.get("corp_code"):
                continue
            sc = str(c.get("stock_code") or "").strip()
            rec = None
            if sc and sc in by_stock:
                rec = by_stock[sc]
            else:
                cands = by_name.get(norm(c["name"]), [])
                if len(cands) == 1:
                    rec = cands[0]
                elif len(cands) > 1:
                    # 상장(종목코드 有) 우선 선택
                    listed = [x for x in cands if x["stock_code"]]
                    if len(listed) == 1:
                        rec = listed[0]
                    else:
                        ambiguous.append((c["name"], [x["corp_name"] for x in cands]))
            if rec:
                c["corp_code"] = rec["corp_code"]
                if not c.get("stock_code") and rec["stock_code"]:
                    c["stock_code"] = rec["stock_code"]
                filled += 1
            else:
                if c["name"] not in [a[0] for a in ambiguous]:
                    unmatched.append(c["name"])

    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(cfg, f, allow_unicode=True, sort_keys=False)

    print(f"corp_code {filled}건 채움")
    if unmatched:
        print(f"[미매칭 {len(unmatched)}] 수동 확인 필요: {', '.join(unmatched)}", file=sys.stderr)
    if ambiguous:
        print("[중복매칭] 아래는 후보가 여러 개 — companies.yml 에 정확한 법인명으로 수정 필요:",
              file=sys.stderr)
        for name, cands in ambiguous:
            print(f"  - {name} → 후보: {cands}", file=sys.stderr)


if __name__ == "__main__":
    main()
