from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AuthorityDecision:
    allowed: bool
    reason: str
    policy_id: str = "frequency-nebius-v0.1"


def decide(
    *,
    model: str,
    prompt_chars: int,
    allowed_models: Iterable[str] | None = None,
    max_prompt_chars: int = 32_000,
    execute: bool = False,
) -> AuthorityDecision:
    if prompt_chars < 0:
        return AuthorityDecision(False, "invalid_prompt_length")
    if prompt_chars > max_prompt_chars:
        return AuthorityDecision(False, "prompt_exceeds_limit")
    allow = set(allowed_models or ())
    if allow and model not in allow:
        return AuthorityDecision(False, "model_not_in_allowlist")
    if not execute:
        return AuthorityDecision(False, "execution_not_explicitly_authorized")
    return AuthorityDecision(True, "authorized")
