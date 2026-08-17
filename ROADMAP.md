# Roadmap

Parlons LSQ now has a frozen first-generation checkpoint. The roadmap moves forward from that baseline rather than extending the 29-class prototype indefinitely.

## Runtime v1.5 — first checkpoint

Runtime v1.5 established the complete chain:

```text
hand-built LSQ data
→ reproducible feature representation
→ temporal classifier
→ frozen model identity
→ local Android/Web/Windows inference
→ multilingual product surface
→ documented privacy and research boundaries
```

It also revealed the main limitation of the original data: robustness changes quickly when signing speed, lighting, framing, distance, or position move outside the narrow capture conditions represented in training.

That lesson defines the next phase.

## Next — stronger data and model generation

Priorities include:

- a substantially larger and more varied LSQ dataset;
- stronger provenance and consent metadata;
- more signers and independent recording sessions;
- signer-disjoint and session-disjoint evaluation;
- broader environmental and camera variation;
- stronger visual-temporal representations;
- pretrained video/sign-language encoders where appropriate;
- better uncertainty/open-set methodology;
- a vocabulary large enough to support a more meaningful use case.

The goal is a model whose performance remains useful across **people and conditions it was not optimized around**.

## Toward larger LSQ recognition

As data quality and robustness improve, the project can expand toward:

- hundreds of signs in a focused domain;
- broader vocabulary;
- richer hand/body/face/motion modelling;
- continuous signing and sequence modelling;
- multimodal alignment with text, gloss, or semantic representations where appropriate;
- cross-lingual sign-language representation experiments;
- retrieval and open-vocabulary approaches.

Each generation will define its own model identity, data assumptions, and evaluation scope.

## Deployment evolution

Runtime v1.5 is local because the compact model makes local inference practical.

A future large or sensitive model can use:

- optimized local inference;
- secure hosted GPU inference;
- or a hybrid design with local fallback and a stronger remote model.

The choice will be driven by model size, latency, privacy, updateability, infrastructure cost, and model-protection requirements. The Backend already preserves a transport-neutral seam for that evolution.

## Community and domain partnership

As technical scope grows, priorities also include stronger collaboration with LSQ users, Deaf community organizations, educators, interpreters, and qualified linguistic/domain partners; careful treatment of regional and signer variants; and explicit consent/provenance for new research data.

## Versioning principle

Every major research generation should answer three questions:

1. **What changed?**
2. **What did the new data/model enable?**
3. **Can the previous baseline still be reproduced?**

Runtime v1.5 gives the project a solid answer to the third question from the beginning.
