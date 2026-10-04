# Security

Report security issues privately to Altru.dev rather than opening a public issue when disclosure could expose credentials, private prompts, or exploitable execution behavior.

## Default security posture

- no telemetry;
- no remote code execution;
- no provider call without explicit execution authorization;
- provider key is environment-only and is never written to evidence;
- prompt and response bodies are not persisted by the harness;
- model allowlists and prompt-size bounds are enforced before dispatch;
- evidence claims are bounded to observations this adapter can directly support.

This public repository is intentionally separated from the proprietary Frequency core.
