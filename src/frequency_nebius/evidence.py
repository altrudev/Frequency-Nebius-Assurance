from __future__ import annotations
import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_json(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class EvidenceRecord:
    schema: str
    observed_at: str
    provider: str
    model: str
    request_sha256: str
    response_sha256: str | None
    authority_allowed: bool
    authority_reason: str
    executed: bool
    http_status: int | None
    latency_ms: int | None
    claim_ceiling: list[str]
    prompt_retained: bool = False
    response_retained: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
