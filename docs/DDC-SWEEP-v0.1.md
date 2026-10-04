# DDC / Frequency sweep — v0.1

## Scope

Public Nebius Token Factory adapter and local evidence harness only.

## Established

- live provider execution is deny-by-default;
- `--execute` is required for a provider call;
- optional model allowlist is enforced before dispatch;
- prompt-size limit is enforced before dispatch;
- API key is consumed only from `NEBIUS_API_KEY`;
- evidence records do not retain prompt or response bodies;
- denied requests produce evidence without calling the provider;
- dry-run requires no provider secret;
- request and response identities are represented by SHA-256 hashes;
- claim ceilings are present in every record.

## NOT ESTABLISHED

- provider-side runtime attestation;
- model-weight identity;
- complete mediation within Nebius infrastructure;
- independent external observation;
- causal attribution inside provider infrastructure;
- production reliability;
- live-provider interoperability, until a user-authorized API-key run is executed.

## Test result

The initial local suite passes 6 tests. A dry-run confirms no network execution and no prompt/response retention. No GitHub Actions workflow is added.

## Release decision

Suitable for public adapter review as v0.1 candidate. A live Nebius run should be a separate, explicitly authorized evidence event after account credit/key setup.
