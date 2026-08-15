# Roadmap

Parlons LSQ uses Runtime v1.5 as a frozen baseline. The roadmap therefore separates **finishing the current evidence package** from **starting new research**.

## Phase 0 — Runtime v1.5 sign-off

Status: implementation frozen; validation remains.

Remaining work:

- execute Frontend and Backend final validation gates;
- complete H5 ↔ TFLite parity evidence;
- run the 145-trial controlled evaluation;
- record latency/agreement evidence where planned;
- capture clean Android/Web/Windows screenshots;
- publish the reviewed showcase evidence set.

No feature expansion belongs in this phase unless a gate exposes a release-blocking defect.

## Phase 1 — Stronger research baseline

Goal: move beyond the historical 29-class compatibility pipeline without losing reproducibility.

Likely work:

- define a new dataset/provenance manifest;
- establish signer-disjoint and session-disjoint splits;
- compare stronger spatial-temporal representations;
- benchmark pretrained video/sign-language encoders where licensing and data fit allow;
- define robust baselines before scaling class count;
- document uncertainty and open-set methodology rather than forcing closed-set predictions into every input.

The key success criterion is **credible unseen-signer evaluation**, not simply a larger label count.

## Phase 2 — Larger LSQ recognition scope

Potential directions:

- hundreds of signs in a focused domain;
- broader vocabulary after data quality is proven;
- improved motion/hand/body/face representation;
- efficient local inference for real product constraints;
- signer and environment robustness;
- better handling of variants and context.

Domain focus may be used when it improves data quality and real usefulness rather than presenting a tiny vocabulary as general LSQ coverage.

## Phase 3 — Toward richer sign-language modelling

Only after the isolated-sign methodology is strong enough:

- continuous signing segmentation/recognition;
- sequence modelling;
- multimodal alignment with text/gloss/semantic representations where appropriate;
- cross-lingual sign-language representation experiments;
- larger pretrained/fine-tuned sign-language models;
- open-vocabulary or retrieval-style systems.

These directions require substantially different evidence and should not inherit Runtime v1.5 claims automatically.

## Community and domain partnership

As the project grows, technical scaling must be matched by stronger domain involvement.

Priorities include:

- collaboration with LSQ users and Deaf community organizations;
- review by educators/interpreters/linguistic specialists where appropriate;
- careful treatment of regional or signer variants;
- consent/provenance processes for new data collection;
- product testing with intended users rather than developer-only evaluation.

## Product evolution

The current four-area product architecture—Home, Recognize, Signs, You—is intentionally stable.

Future product work should focus on depth rather than navigation sprawl:

- richer authentic sign-learning media;
- meaningful practice feedback;
- progress/review flows based on real usage;
- clearer uncertainty/error recovery;
- accessibility validation;
- privacy-preserving research contribution only when a proper consent system exists.

## What is not on the roadmap

The project does not plan to manufacture progress by:

- adding unsupported AI labels to the UI;
- claiming continuous translation from isolated-sign results;
- increasing class count without signer-generalization evidence;
- silently collecting recognition footage for research;
- replacing reproducibility with one-off demo performance;
- treating the historical 228-D compatibility representation as the permanent scientific architecture.

## Versioning principle

Every major research/runtime generation should answer three questions clearly:

1. **What exactly changed?**
2. **What evidence supports the new claims?**
3. **Can the previous baseline still be reproduced?**

Runtime v1.5 exists to make that discipline possible from the beginning.
