# Assurance boundary

This repository is a public adapter and evidence harness. It is not the private Frequency core.

## Authority

Provider execution is fail-closed by default. A live request requires the explicit `--execute` flag. Optional model allowlists and prompt-size limits are enforced before any network dispatch.

## Data boundary

Prompts and responses are not written into evidence records. The harness retains hashes, provider status, model identifier, local timing, and the local authority decision. API keys are read from the process environment and are never included in evidence.

## Claim ceiling

A successful record establishes only what this adapter directly observes: the locally constructed request identity, the requested model identifier, the local authority decision, an HTTP response received from the configured provider endpoint, and local elapsed time.

It does **not** by itself establish provider-side runtime attestation, complete mediation, causal attribution inside provider infrastructure, independent external observation, model-weight identity, or that the requested model was the physical runtime that produced the response.

## Threat model

The first release is designed to resist accidental live execution, model-scope expansion, oversized prompts, secret leakage into evidence, raw prompt/response persistence, and claim inflation from an HTTP response into runtime or attestation claims.

Future adapters may add independent witnesses, signed receipts, disclosure accounting, and action-level tool mediation without weakening these ceilings.
