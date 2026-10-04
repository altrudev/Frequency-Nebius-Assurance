from frequency_nebius.authority import decide


def test_execution_requires_explicit_authorization():
    decision = decide(model="x", prompt_chars=10, execute=False)
    assert not decision.allowed
    assert decision.reason == "execution_not_explicitly_authorized"


def test_model_allowlist_is_enforced():
    decision = decide(
        model="x",
        prompt_chars=10,
        execute=True,
        allowed_models=["y"],
    )
    assert not decision.allowed
    assert decision.reason == "model_not_in_allowlist"


def test_prompt_limit_is_enforced():
    decision = decide(
        model="x",
        prompt_chars=11,
        execute=True,
        max_prompt_chars=10,
    )
    assert not decision.allowed
    assert decision.reason == "prompt_exceeds_limit"


def test_authorized_case():
    decision = decide(
        model="x",
        prompt_chars=10,
        execute=True,
        allowed_models=["x"],
    )
    assert decision.allowed
