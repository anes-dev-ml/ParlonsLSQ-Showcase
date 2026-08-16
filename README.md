# Parlons LSQ

**From a hand-built LSQ dataset to a reproducible local AI prototype running on Android, Web and Windows.**

![Parlons LSQ Web home](screenshots/01-home-web.webp)

Parlons LSQ is a research-engineering project exploring computer-vision recognition for **Langue des signes québécoise (LSQ)**. The first generation started small on purpose: collect isolated-sign examples, turn motion into a reproducible numerical representation, train a classifier, then prove that the same frozen model contract can survive the full trip from experimentation to real software.

Runtime v1.5 is that first frozen checkpoint. It recognizes **29 isolated signs** through a `64 × 228` temporal input and runs locally on the three product targets developed for the project. The application is useful evidence, but the main story is the AI pipeline, what it taught us, and the larger research direction it unlocked.

## At a glance

| | Runtime v1.5 |
|---|---|
| Research task | Experimental isolated-sign LSQ classification |
| Frozen engine | `prototype-lsq-29-v1` |
| Vocabulary | 29 historical classes |
| Model input | `64 × 228` |
| Feature contract | `legacy-mediapipe-228-v1` |
| Product targets | Android · Web · Windows |
| Recognition path | Local/offline |
| Interface | French · English · Arabic/RTL |
| Source model | Private implementation; reviewed access may be granted case-by-case |

## The idea

The original prototype did not begin with a downloaded end-to-end sign-language model. The pipeline was built manually:

```text
isolated LSQ clips
        ↓
MediaPipe landmarks
        ↓
228-D compatibility representation per observation
        ↓
temporal normalization to 64 steps
        ↓
29-class neural classifier
        ↓
frozen H5 reference
        ↓
platform-specific local inference
        ↓
Android · Web · Windows
```

That path matters. It demonstrates the ability to reason about **data collection, representation design, temporal modelling, model reproducibility, conversion/parity, platform ML integration, privacy, and product deployment** as one connected system rather than as isolated demos.

For the exact runtime split, see [ARCHITECTURE.md](ARCHITECTURE.md). For the research story and next generation, see [RESEARCH.md](RESEARCH.md).

## What the first baseline demonstrated

The 29-class model became strong enough in development conditions to support a real recognition workflow and to produce successful recognitions on inputs beyond the original capture set. Qualitative checks included people and reference footage the model had not been trained on.

The most useful result was not a single headline percentage. It was discovering **where the first dataset stopped being enough**. Recognition was much easier to disturb when signing speed, lighting, framing, camera/body position, or capture conditions moved away from the limited variation represented in the original data.

That is a valuable research result: the pipeline learned the signs, but the next leap depends on **more varied data and a stronger representation**, not squeezing another decimal point out of the same small dataset.

These observations are development evidence, not a population-level accuracy claim. The project deliberately keeps that distinction clear in [EVIDENCE.md](EVIDENCE.md).

## See it running

### Android — local recognition on a physical phone

| Capture in progress | Recognition result |
|---|---|
| <img src="screenshots/02-recognition-ready-android.webp" alt="Android recognition capture in progress" width="300"> | <img src="screenshots/03-recognition-result-android.webp" alt="Android recognized sign result" width="300"> |

The Android result is a **qualitative external-reference check**: the app was pointed at LSQ reference footage and recognized the isolated sign shown. The source footage is not redistributed in this repository and the example is not presented as an accuracy statistic.

### Web — browser-local inference

![Web recognition result](screenshots/04-recognition-result-web.webp)

### Windows — local reference-worker inference

![Windows recognition result](screenshots/05-recognition-result-windows.webp)

For the Web and Windows captures, the camera preview was privacy-redacted after capture. The recognition result and application state were left untouched.

### Arabic / RTL product surface

![Arabic RTL Signs interface](screenshots/06-rtl.webp)

The multilingual product layer is not a mock translation screenshot: navigation, alignment, search, categories and content presentation all move into an RTL layout for Arabic.

## Cross-platform runtime

The same frozen recognition contract is expressed differently on each platform:

```text
Android
CameraImage → native MediaPipe Tasks → 228-D observations → 64 steps → LiteRT/TFLite

Web
short local browser clip → MediaPipe Tasks WASM → 228-D observations → 64 steps → LiteRT.js WASM

Windows
short local clip → local stdio worker → OpenCV + MediaPipe Tasks → 64 steps → frozen H5
```

No normal recognition request is sent to FastAPI in Runtime v1.5. The Backend remains useful for learning content, reproducibility/evaluation tooling, the Windows local worker, and a dormant transport-neutral seam for a future hosted model.

A larger future LSQ model may be **local, server-side, or hybrid** depending on model size, latency, privacy, updateability and model-protection requirements. Runtime v1.5 proves the local path without locking the research program to it forever.

## Scope without hype

Runtime v1.5 is an **experimental 29-class isolated-sign recognizer**. It is not presented as continuous LSQ translation, open-vocabulary recognition, calibrated confidence, a trained unknown-sign detector, clinical validation, or a population-generalized LSQ model.

Those boundaries do not weaken the project; they make the engineering and research evidence easier to trust.

## Frozen public snapshot

This showcase represents these private-source revisions:

- **Frontend:** `4ffa25aab11106a226c98787f567ca4eb3524fba`
- **Backend/reference:** `c33d480db666723bece607990a5ef1b64aac0cf3`
- **Frozen H5 SHA-256:** `98590d3b47e299db7966bdc1d51946de3049d51934280e320e6dfbb18fda8110`

The full provenance record is in [BUILD_MANIFEST.md](BUILD_MANIFEST.md).

## Where the project goes next

Runtime v1.5 is the first frozen checkpoint, not the destination. It proves the full path from hand-built data to a reproducible AI system.

The next research generation is about **scale, variation and robustness**: much broader LSQ data, more signers and sessions, stronger visual-temporal representations, and a model that can justify a much larger vocabulary under genuinely difficult conditions.

That work belongs in the private research workspace so the historical baseline stays reproducible instead of being rewritten every time the project advances. See [ROADMAP.md](ROADMAP.md).

## Private source access

This repository is the public case study. The Flutter application, Backend/reference implementation, platform ML code, model tooling and active research repository remain private.

Serious technical reviewers, recruiters, research collaborators or potential partners may contact **[@anes-dev-ml](https://github.com/anes-dev-ml)**. Selected read-only access can be considered case-by-case. Access does not grant permission to copy, redistribute or relicense the implementation.

More detail: [ACCESS.md](ACCESS.md).

## Documentation

- [Architecture](ARCHITECTURE.md)
- [Research scope](RESEARCH.md)
- [Evidence record](EVIDENCE.md)
- [Privacy boundary](PRIVACY.md)
- [Build manifest](BUILD_MANIFEST.md)
- [Roadmap](ROADMAP.md)
- [Release policy](RELEASES.md)
- [Source access](ACCESS.md)
- [Security](SECURITY.md)
- [License](LICENSE)

---

**A small model was enough to prove the chain. The next model is where the research gets ambitious.**
