# Research scope

Parlons LSQ began with a practical research question: **how far can a carefully designed sign representation and temporal model go when the available LSQ data is small?**

Runtime v1.5 freezes the answer from the first generation so the next generation can improve on a real baseline rather than an undocumented prototype.

## Frozen first-generation baseline

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
| Scores | Raw classifier outputs, not calibrated probability |
| Trained open-set detector | None |

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

This was a manually constructed ML pipeline, not an end-to-end pretrained sign-language model.

## What the baseline taught us

The prototype became strong enough in development conditions to drive a working recognition product and showed promising qualitative transfer to inputs outside the original capture set, including successful recognitions from people/reference footage not used to train the model.

Its weakness was equally informative. Performance became easier to disturb when signing speed, lighting, framing, distance, camera/body position or capture conditions shifted away from the limited variation represented in the small original dataset.

That points to a clear research lesson:

> **The first model learned useful sign structure, but robustness is now a data-and-representation problem.**

Instead of spending the next cycle over-optimizing a 29-class dataset, the project is moving toward a much broader and more varied research foundation.

## How to read the evidence

The current evidence supports statements such as:

- the frozen model can power real local inference;
- the same model contract can be carried across Android, Web and Windows;
- recognition can work on qualitative examples outside the original capture set;
- the original dataset's limited variation creates clear sensitivity to environmental and signing changes.

It is **not** used to claim population-level accuracy, signer-independent performance across LSQ users, continuous translation, open-vocabulary recognition or clinical validation.

This distinction keeps the first baseline useful instead of forcing it to answer research questions it was never designed to answer.

## Why freeze it

Freezing Runtime v1.5 preserves:

- the exact feature layout;
- the model identity;
- the temporal input contract;
- the platform deployment lineage;
- the lessons learned from the original dataset.

Future experiments can therefore replace the representation/model without rewriting history.

## Next research generation

The next model is expected to focus on:

- substantially larger and more varied LSQ data;
- more signers and independent sessions;
- signer/session-disjoint evaluation;
- stronger visual-temporal representations;
- better robustness to speed, lighting, framing, position and background;
- pretrained video/sign-language encoders where scientifically and legally appropriate;
- cross-lingual/cross-sign-language representation learning where it genuinely helps;
- uncertainty/open-set methodology rather than forced closed-set answers;
- a deployment strategy chosen from the model's actual size and security needs.

For a compact model, local inference remains attractive. A future larger or more valuable model may use secure server-side inference or a hybrid local/cloud design.

## LSQ-specific responsibility

Scaling the model is only useful if the data and labels remain meaningful. As the project grows, technical work should be matched by stronger involvement from LSQ users, educators, interpreters, Deaf community organizations and qualified linguistic/domain partners.

Normal product recognition is not research data collection. Any future contribution flow should have explicit consent, purpose, provenance, retention and deletion rules.

## The role of Runtime v1.5

Runtime v1.5 is no longer where the project needs to spend its research energy. Its job is to remain a **reproducible first checkpoint** showing that the complete chain—from hand-built data to a working AI product—was achieved.

The next checkpoint should be harder to earn.
