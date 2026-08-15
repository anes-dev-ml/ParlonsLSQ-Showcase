# Build manifest

This document records the private application revisions represented by the Parlons LSQ public showcase.

## Canonical Runtime v1.5 snapshot

| Component | Repository | Revision / identity |
|---|---|---|
| Frontend product | private `ParlonsLSQ-Frontend` | `09d60a139ed81b84c6ca59ea1d70d6f1796816d7` |
| Backend/reference runtime | private `ParlonsLSQ-Backend` | `71c6d7dae280f6f207ccdf67048ecaf7e2af2571` |
| Recognition engine | frozen prototype | `prototype-lsq-29-v1` |
| Feature schema | frozen compatibility schema | `legacy-mediapipe-228-v1` |
| Reference H5 SHA-256 | private model artifact | `98590d3b47e299db7966bdc1d51946de3049d51934280e320e6dfbb18fda8110` |
| Model input | frozen contract | `64 × 228` |
| Model output | frozen contract | 29 classes |
| Product targets | frozen validation target | Android · Web · Windows |

## Product/runtime status

Runtime v1.5 implementation is **frozen for final validation**.

Permitted changes before showcase release are limited to targeted fixes caused by a failed validation gate. Any such fix must update the represented source SHA above before new public evidence is captured.

New features, new datasets, model architecture experiments, or large-model work do not mutate this snapshot; they belong to future research revisions.

## Evidence status

The public evidence set is captured only after the final validation pass.

Until those files are added and reviewed:

- architecture/documentation may be considered release-candidate documentation;
- final accuracy/latency fields remain intentionally absent;
- no screenshot from an earlier debug build is accepted as release evidence;
- no final showcase tag should be created.

The required visual set is defined in [EVIDENCE.md](EVIDENCE.md) and `release/manifest.json`.

## Release rule

A public showcase release represents **one exact pair** of private application revisions.

If either private source revision changes after evidence capture:

1. update this manifest and `release/manifest.json`;
2. rerun the affected validation gate;
3. recapture any evidence whose behavior or appearance changed;
4. create a new showcase release record rather than silently rewriting an old tag.

## Private-source boundary

The SHAs above provide provenance without publishing private source code.

Selected read-only access may be granted case-by-case as described in [ACCESS.md](ACCESS.md).
