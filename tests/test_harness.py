from frequency_nebius.harness import run_case


def test_dry_run_does_not_execute_or_require_secret():
    record = run_case(
        model="example/model",
        prompt="hello",
        execute=False,
    )
    assert record.executed is False
    assert record.response_sha256 is None
    assert record.prompt_retained is False
    assert record.response_retained is False


def test_denied_model_does_not_execute():
    record = run_case(
        model="blocked/model",
        prompt="hello",
        execute=True,
        allowed_models=["allowed/model"],
    )
    assert record.executed is False
    assert record.authority_reason == "model_not_in_allowlist"
