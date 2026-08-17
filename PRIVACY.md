# Privacy

Recognition and research data collection are separate by design in Parlons LSQ.

Runtime v1.5 keeps ordinary recognition local to the user's device or browser path, while any future research-data contribution would use a separate opt-in workflow.

## Recognition runtime

### Android

Recognition runs on-device through MediaPipe and LiteRT/TFLite.

### Web

Recognition runs inside the browser through MediaPipe WASM and LiteRT.js WASM.

### Windows

A short local clip is passed to a local stdio Python worker on the same machine.

## Product history

Optional local recognition history stores result-oriented metadata such as recognized label/status, time, and runtime/version information where applicable.

Camera frames, video clips, raw landmarks, and 228-D feature tensors are temporary recognition inputs rather than ordinary history records.

Saved signs and interface preferences are local product state and do not require an account.

## Network use

The product may use network access for versioned learning content. Runtime v1.5 recognition itself remains local across Android, Web, and Windows.

## Research participation

Future research-data contribution should be explicit and separate from normal recognition. A contribution flow would define what is collected, why it is collected, consent state, provenance, retention/deletion rules, sharing boundaries, and how derived research artifacts are handled.

This separation lets the product evolve toward larger research datasets without turning everyday camera use into silent data collection.

## Logging

Recognition logging is designed around runtime events and diagnostics rather than camera media or feature payloads. Credentials and authentication material also remain outside normal logs.

## Why local-first fits Runtime v1.5

Sign-language video can contain face, body, movement, environment, and identity cues. With a model small enough to run locally, keeping the recognition path on-device/in-browser provides a simple and useful privacy boundary.

Future model generations can revisit deployment architecture alongside their model size, performance, and security requirements.

## Public Showcase

The Showcase contains curated screenshots and documentation only. It does not include raw research sessions, private user recordings, production credentials, model binaries, or datasets.
