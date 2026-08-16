# Roadmap

Parlons LSQ now has a frozen first-generation checkpoint. The roadmap moves forward from that baseline rather than extending the 29-class prototype indefinitely.

## Runtime v1.5 — frozen first checkpoint

**Status: complete as the public showcase baseline.**

Runtime v1.5 established the full chain:

```text
hand-built LSQ data
→ reproducible feature representation
→ temporal classifier
→ frozen model identity
→ local Android/Web/Windows inference
→ multilingual product surface
→ documented privacy and claim boundaries
```

The prototype also exposed the key limitation of its original data: robustness changes quickly with signing speed, lighting, framing, distance and position when those conditions were not represented well during data collection.

That lesson defines the next phase.

## Next — stronger data and model generation

Priorities include:

- a substantially larger and more varied LSQ dataset;
- stronger provenance and consent metadata;
- more signers and independent recording sessions;
- signer-disjoint and session-disjoint evaluation;
- broader environmental/camera variation;
- stronger visual-temporal representations;
- pretrained video/sign-language encoders where appropriate;
- better uncertainty/open-set methodology;
- a vocabulary large enough to support a more meaningful use case.

The goal is not simply “more classes.” The goal is a model whose performance survives **people and conditions it was not optimized around**.

## Toward larger LSQ recognition

Once data quality and robustness justify it, the project can expand toward:

- hundreds of signs in a focused domain;
- broader vocabulary;
- richer hand/body/face/motion modelling;
- continuous signing and sequence modelling;
- multimodal alignment with text/gloss/semantic representations where appropriate;
- cross-lingual sign-language representation experiments;
- retrieval/open-vocabulary approaches.

Each generation should earn its own claims rather than inheriting them from Runtime v1.5.

## Deployment evolution

Runtime v1.5 is local because the compact model makes local inference practical.

A future large or sensitive model can move to:

- optimized local inference;
- secure hosted GPU inference;
- or a hybrid design with a local fallback and stronger remote model.

The choice should be driven by model size, latency, privacy, updateability, infrastructure cost and model-protection requirements. The Backend already preserves a transport-neutral future seam without exposing a dormant recognition API in the current runtime.

## Community and domain partnership

As technical scope grows, priorities also include stronger collaboration with LSQ users, Deaf community organizations, educators, interpreters and qualified linguistic/domain partners; careful treatment of regional/signer variants; and explicit consent/provenance for new research data.

## Versioning principle

Every major research generation should answer three questions:

1. **What changed?**
2. **What evidence supports the new capability?**
3. **Can the previous baseline still be reproduced?**

Runtime v1.5 exists so the answer to question three is already yes.
