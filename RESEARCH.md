# Research scope

Parlons LSQ began with a practical research question: **how far can a carefully designed sign representation and temporal model go when the available LSQ data is small?**

Runtime v1.5 freezes the first answer to that question so the next generation can improve on a real baseline rather than an undocumented prototype.

## First-generation baseline

| Property | Value |
|---|---|
| Engine | `prototype-lsq-29-v1` |
| Task | Isolated-sign classification |
| Classes | 29 fixed historical labels |
| Temporal input | 64 steps |
| Per-step feature size | 228 |
| Feature schema | `legacy-mediapipe-228-v1` |
| Reference model | Frozen H5 |
| Product derivative | Fixed-batch TFLite/LiteRT where required |
| Scores | Raw classifier outputs |
| Open-set detector | Not part of this generation |

## How it was built

```text
record isolated LSQ examples
→ extract MediaPipe landmarks
→ convert observations into a fixed 228-D representation
→ store processed examples
→ assemble 64-step temporal samples
→ train a 29-class classifier
→ freeze/recover the H5 artifact
→ reproduce the encoder exactly
→ deploy compatible local runtimes on Android, Web and Windows
```

This was a manually constructed ML pipeline. Each stage—from representation design to deployment—became part of the project rather than being hidden behind a pretrained end-to-end model.

## What the baseline taught us

The model became strong enough in development conditions to drive a working recognition product and showed promising qualitative transfer to inputs outside the original capture set, including successful recognitions from people and reference footage not used in training.

Its sensitivity also pointed directly to the next research problem. Speed, lighting, framing, distance, camera/body position, and other capture changes could move inputs outside the narrow variation represented in the original dataset.

The first generation therefore produced a clear conclusion:

> **The model learned useful sign structure; the next gains depend on broader data and a stronger representation.**

That is why Runtime v1.5 is frozen rather than endlessly tuned.

## Current research scope

Runtime v1.5 focuses on isolated-sign classification and cross-platform deployment of one reproducible baseline. It gives the project a stable reference for model identity, preprocessing, temporal input, and deployment behavior.

The next generations can then address broader questions with the right methodology: more signers, independent sessions, larger vocabularies, stronger robustness testing, open-set behavior, and eventually continuous signing.

## Next research generation

The next model is expected to focus on:

- substantially larger and more varied LSQ data;
- more signers and independent sessions;
- signer/session-disjoint evaluation;
- stronger visual-temporal representations;
- better robustness to speed, lighting, framing, position, and background;
- pretrained video/sign-language encoders where scientifically and legally appropriate;
- cross-lingual/cross-sign-language representation learning where it genuinely helps;
- uncertainty/open-set methodology;
- a deployment strategy chosen from the model's actual size and security needs.

For a compact model, local inference remains attractive. A larger or more valuable future model may use secure server-side inference or a hybrid local/cloud design.

## LSQ and domain collaboration

As the project grows, technical scaling should be matched by stronger involvement from LSQ users, educators, interpreters, Deaf community organizations, and qualified linguistic/domain partners. Better data is not only more data; it also means better labels, provenance, variants, consent, and context.

Normal product recognition remains separate from research data collection. Any future contribution flow should define explicit consent, purpose, provenance, retention, and deletion rules.

## Role of Runtime v1.5

Runtime v1.5 is the project's **reproducible first checkpoint**: a complete path from hand-built data and model design to working local AI software.

The next checkpoint should be larger, harder, and supported by stronger data.
