"""공용 유틸 — 설정 로드, 경로, 텍스트 매칭."""
from __future__ import annotations
import re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config"
DATA = ROOT / "data"
TOPICS = ROOT / "topics"

INDUSTRY_LABELS = {
    "entertainment": "엔터",
    "media": "미디어",
    "telecom": "통신",
    "game": "게임",
    "it": "IT",
}


def load_yaml(name: str) -> dict:
    with open(CONFIG / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def companies() -> list[dict]:
    """모든 기업을 industry 태그를 붙여 평탄화해 반환."""
    cfg = load_yaml("companies.yml")
    out = []
    for industry, firms in cfg.items():
        for c in firms:
            out.append({**c, "industry": industry,
                        "industry_label": INDUSTRY_LABELS.get(industry, industry)})
    return out


def keyword_config() -> dict:
    return load_yaml("keywords.yml")


def match_topics(text: str) -> list[str]:
    """텍스트에 등장한 회계 토픽 키를 반환."""
    kw = keyword_config()["topics"]
    hits = []
    for topic, meta in kw.items():
        if any(k in text for k in meta["keywords"]):
            hits.append(topic)
    return hits


def has_audit_signal(text: str) -> bool:
    signals = keyword_config().get("audit_signal", [])
    return any(s in text for s in signals)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text or "")).strip()
