# Privacy and data boundary

Parlons LSQ is designed around a simple principle: **using recognition is not the same thing as contributing research data**.

Runtime v1.5 keeps normal recognition local to the user's device/browser path and treats research participation as a separate future decision.

## Normal recognition

### Android

Recognition runs on-device through the local MediaPipe + LiteRT/TFLite path.

### Web

Recognition runs inside the browser through MediaPipe WASM + LiteRT.js WASM.

### Windows development runtime

A short local clip is passed to a local stdio Python worker on the same machine. The worker does not expose an HTTP recognition service.

## Product history

When optional local recognition history is enabled, the intended record contains result metadata such as:

- result/status;
- recognized label when available;
- time;
- recognition/runtime version metadata where applicable.

Ordinary product history does **not** store:

- camera frames;
- video clips;
- raw landmarks;
- 228-D feature tensors.

Saved signs and interface preferences are also local product state and do not require an account.

## Network boundary

The product can use network access for non-recognition content when configured, such as the versioned learning catalogue.

Normal recognition clips and feature tensors are not sent to the Parlons LSQ HTTP API.

The HTTP API is intentionally limited to ordinary service health/readiness and learning-content endpoints.

## Research participation

Normal recognition sessions are not automatically converted into research samples.

Any future contribution flow should be explicit and separate from ordinary app use. It should clearly state:

- what is being collected;
- why it is being collected;
- whether raw video, landmarks, derived features, labels, or metadata are retained;
- retention/deletion rules;
- research partners or sharing boundaries;
- consent state and provenance;
- withdrawal process where applicable;
- whether trained models or derived artifacts can persist after raw-data deletion.

This showcase does not claim that a production research-consent system has already been deployed.

## Logging boundary

Product/runtime logging should not contain camera frames, clips, landmark arrays, 228-D tensors, credentials, or authentication tokens.

## Why local-first matters here

Sign-language video can contain far more personal information than a text query: face, body, environment, movement, identity cues, and potentially sensitive context.

Keeping the recognition path local reduces unnecessary transfer and makes the product's privacy story easier to understand. It does not remove the need for strong consent and governance if future research data collection is introduced.

## Public showcase boundary

This public repository contains no private user recordings, research-session media, production credentials, or raw datasets. Public screenshots should use only controlled/test content suitable for portfolio publication.
