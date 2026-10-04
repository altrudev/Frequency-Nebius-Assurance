from __future__ import annotations
import os
import time
from .authority import decide
from .evidence import EvidenceRecord, now_iso, sha256_json, sha256_text
from .nebius import TokenFactoryClient


CLAIM_CEILING = [
    "request_integrity_hash",
    "provider_http_response_observed_by_this_process",
    "model_identifier_requested",
    "local_authority_decision",
    "local_latency_measurement",
]


def run_case(
    *,
    model: str,
    prompt: str,
    execute: bool,
    allowed_models: list[str] | None = None,
    max_prompt_chars: int = 32_000,
    base_url: str = "https://api.tokenfactory.nebius.com",
) -> EvidenceRecord:
    decision = decide(
        model=model,
        prompt_chars=len(prompt),
        allowed_models=allowed_models,
        max_prompt_chars=max_prompt_chars,
        execute=execute,
    )
    request_hash = sha256_json(
        {"model": model, "prompt_sha256": sha256_text(prompt)}
    )

    if not decision.allowed:
        return EvidenceRecord(
            schema="frequency.nebius.evidence.v0.1",
            observed_at=now_iso(),
            provider="nebius-token-factory",
            model=model,
            request_sha256=request_hash,
            response_sha256=None,
            authority_allowed=False,
            authority_reason=decision.reason,
            executed=False,
            http_status=None,
            latency_ms=None,
            claim_ceiling=CLAIM_CEILING,
        )

    client = TokenFactoryClient(
        os.environ.get("NEBIUS_API_KEY", ""),
        base_url=base_url,
    )
    started = time.perf_counter()
    response = client.chat(model=model, prompt=prompt)
    latency_ms = round((time.perf_counter() - started) * 1000)
    return EvidenceRecord(
        schema="frequency.nebius.evidence.v0.1",
        observed_at=now_iso(),
        provider="nebius-token-factory",
        model=model,
        request_sha256=request_hash,
        response_sha256=sha256_json(response.body),
        authority_allowed=True,
        authority_reason=decision.reason,
        executed=True,
        http_status=response.status,
        latency_ms=latency_ms,
        claim_ceiling=CLAIM_CEILING,
    )
