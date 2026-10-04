# Frequency Nebius Assurance

Public Nebius Token Factory adapter and bounded execution-evidence harness for **Frequency** by **Val Rukhaylo / Altru.dev**.

The purpose is not to benchmark model quality alone. It is to make model and agent evaluations carry an explicit authority decision, durable evidence identity, and a strict claim ceiling.

## What v0.1 does

- targets the Nebius Token Factory OpenAI-compatible chat endpoint;
- defaults to **no execution**;
- requires explicit authorization for a live provider call;
- can restrict live calls to a model allowlist;
- hashes request and response evidence without retaining prompt or response bodies;
- records provider HTTP status and local latency;
- states what the evidence can and cannot prove.

## What it does not claim

This adapter does not claim runtime attestation, complete mediation inside Nebius, independent observation, model-weight identity, or causal proof of provider internals. Those remain `NOT_ESTABLISHED` unless separate evidence is added.

## Quick start

Python 3.10+ is enough; the adapter uses the standard library.

Dry run:

```bash
PYTHONPATH=src python -m frequency_nebius.cli run \
  --model openai/gpt-oss-120b \
  --prompt "Return the word READY."
```

Live execution requires both an API key and explicit authorization:

```bash
export NEBIUS_API_KEY="..."
PYTHONPATH=src python -m frequency_nebius.cli run \
  --model openai/gpt-oss-120b \
  --allow-model openai/gpt-oss-120b \
  --prompt "Return the word READY." \
  --execute \
  --out evidence.json
```

## Frequency boundary

This repository deliberately contains only the public adapter/evidence contract. The private Frequency core, proprietary policies, broader reasoning controls, and internal assurance logic are not exported here.

See `docs/ASSURANCE.md` for the current authority, privacy, threat-model, and claim-ceiling contract.

## Provider endpoint

Default base URL:

`https://api.tokenfactory.nebius.com`

Override with `--base-url` when testing a compatible endpoint or a controlled mock.

## License

Apache-2.0 for this public adapter. Frequency core remains separate.
