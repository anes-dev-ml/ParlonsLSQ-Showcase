# Evaluation and evidence

Runtime v1.5 is a frozen 29-class isolated-sign recognition baseline. The available public evidence demonstrates integration across Android, Web, and Windows and records qualitative development observations. It does **not** establish population-level recognition accuracy.

## Runtime verification

The historical snapshot uses the same temporal feature contract on three targets:

| Platform | Processing and inference |
| --- | --- |
| Android | MediaPipe Tasks, 64 × 228 features, LiteRT/TFLite |
| Web | MediaPipe Tasks WASM, 64 × 228 features, LiteRT.js |
| Windows | Local OpenCV/MediaPipe worker, 64 × 228 features, H5 |

Platform-specific implementations and the snapshot's source revisions are documented in [Architecture](ARCHITECTURE.md) and [Build manifest](BUILD_MANIFEST.md).

## Qualitative observations

Successful recognition was observed in development conditions and on selected external inputs, including footage and people outside the original training captures. Performance could degrade under changes in signing speed, lighting, framing, camera distance, and body position.

These observations suggest sensitivity to capture conditions that were insufficiently varied in the original small dataset. They should not be interpreted as a signer-independent benchmark or evidence of reliable open-set recognition.

## Evidence gallery

| Asset | Description |
| --- | --- |
| [Web home](screenshots/01-home-web.webp) | Application interface |
| [Android capture](screenshots/02-recognition-ready-android.webp) | Recognition capture flow |
| [Android result](screenshots/03-recognition-result-android.webp) | Qualitative test with external reference footage |
| [Web result](screenshots/04-recognition-result-web.webp) | Browser-local recognition |
| [Windows result](screenshots/05-recognition-result-windows.webp) | Local-worker recognition |
| [Arabic interface](screenshots/06-rtl.webp) | Right-to-left interface |

Web and Windows camera previews were privacy-redacted after capture; displayed results and interface state were retained. External reference footage is not redistributed.

The authoritative SHA-256 values for all six assets are stored in [release/manifest.json](release/manifest.json) and described in the [build manifest](BUILD_MANIFEST.md).

## Interpretation

The documented baseline establishes that the 29-class model was integrated into a multi-platform application with a stable input contract. It does not establish continuous LSQ translation, calibrated confidence, a trained unknown-sign detector, or robustness across representative signers and recording settings.

Broader evaluation requires more independent signers and sessions, controlled capture variation, documented test splits, and larger datasets. See [Research direction](RESEARCH.md).
