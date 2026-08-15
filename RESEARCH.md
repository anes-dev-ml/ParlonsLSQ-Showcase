# Research scope

Parlons LSQ combines product engineering with a longer-term research goal: understand how to move from a small reproducible isolated-sign prototype toward stronger, larger-scale LSQ recognition and representation learning.

Runtime v1.5 is deliberately conservative. It preserves one historical classifier and makes its behavior reproducible before the research program expands.

## Frozen baseline

| Property | Frozen value |
|---|---|
| Engine | `prototype-lsq-29-v1` |
| Task | isolated-sign classification |
| Classes | 29 fixed historical labels |
| Temporal input | 64 steps |
| Per-step feature size | 228 |
| Feature schema | `legacy-mediapipe-228-v1` |
| Reference model | frozen H5 |
| Product derivative | fixed-batch TFLite/LiteRT where required |
| Score interpretation | raw classifier outputs, not calibrated probability |
| Open-set detector | none trained |

The exact model identity and feature layout are frozen in the private reference implementation. The purpose is reproducibility, not to imply that this is the final LSQ representation.

## How the prototype was built

The project lineage is important because it explains the present architecture:

```text
record isolated sign clips
→ extract landmarks with MediaPipe
→ convert each frame into a fixed numerical representation
→ store processed examples as NumPy arrays
→ assemble 64-step temporal training samples
→ train a 29-class classifier
→ recover/freeze the historical H5
→ reproduce the encoder exactly
→ validate local product derivatives
```

This was a manually constructed pipeline rather than an end-to-end pretrained sign-language model.

## Why freeze it now

Freezing the baseline prevents several common research mistakes:

- silently changing preprocessing while comparing model results;
- mixing product improvements with model improvements;
- presenting a compatibility representation as a scientifically preferred representation;
- treating a successful app demo as evidence of population-level generalization;
- losing the exact model/data contract that produced earlier results.

The 29-class runtime therefore becomes a reproducible reference point for future work.

## Evidence hierarchy

Parlons LSQ distinguishes several levels of evidence:

### Engineering evidence

Examples:

- the model runs locally on a platform;
- camera input reaches the frozen classifier;
- H5 and TFLite derivatives agree within the declared tolerance;
- Android/Web/Windows produce compatible outputs on controlled inputs;
- the product handles permission, lifecycle, uncertain, and failure states.

### Controlled prototype evidence

The final Runtime v1.5 protocol targets all 29 classes with five attempts per class, for 145 controlled trials. This can support statements about the frozen prototype under the documented test conditions.

### Generalization evidence

This requires substantially stronger methodology: multiple unseen signers, independent sessions, broader data, signer-disjoint splits, enough samples per class, and analysis of class imbalance and failure modes.

Runtime v1.5 does **not** claim that level of evidence.

## Current claim boundary

The project may accurately be described as:

> an experimental LSQ learning application with a local/offline 29-class isolated-sign recognition prototype and a reproducible cross-platform runtime.

It is not currently described as:

- a general LSQ translator;
- a continuous sign-language recognition system;
- a fingerspelling recognizer;
- an open-vocabulary sign recognizer;
- a calibrated confidence system;
- a clinically validated accessibility product;
- a population-generalized LSQ model;
- a large sign-language model.

## Future research direction

The long-term research direction is intentionally broader than the frozen prototype.

Areas under investigation include:

- larger LSQ datasets and better data provenance;
- signer-disjoint and session-disjoint evaluation;
- more robust visual-temporal representations;
- hand, body, face, motion, and appearance information without overfitting to one capture setup;
- pretrained sign-language or video encoders;
- cross-lingual/cross-sign-language representation learning where scientifically appropriate;
- contrastive and multimodal pretraining;
- open-set behavior and uncertainty calibration;
- continuous recognition once isolated-sign methodology is strong enough;
- efficient deployment paths that preserve privacy and acceptable latency.

These experiments belong in the private research workspace and should produce their own frozen manifests and evaluation protocols rather than mutating Runtime v1.5 in place.

## LSQ-specific responsibility

A technically strong model can still be a poor sign-language project if the data, labels, variants, cultural context, or evaluation assumptions are weak.

Future work therefore needs increasing collaboration with LSQ users, educators, interpreters, Deaf community organizations, and qualified linguistic/domain partners. Product labels and learning content should not be treated as authoritative linguistic reference merely because a classifier can predict them.

## Research data boundary

Normal product recognition is not research data collection.

Any future research contribution flow should define at minimum:

- explicit informed opt-in;
- what media/features are collected;
- purpose and retention;
- withdrawal/deletion process where applicable;
- provenance and consent state;
- permitted research uses;
- whether data may be shared with research partners;
- whether derived features/models can outlive raw media.

The current product intentionally keeps this separate from ordinary recognition.

## What success looks like next

The next meaningful research milestone is not simply “more classes.” It is a model/evaluation package where a stronger representation and larger dataset demonstrate convincing performance on **unseen signers under a predeclared protocol** while preserving a clear privacy and provenance story.

Runtime v1.5 gives that future work a baseline to beat without rewriting history.
