# Build manifest

This file records the private-source and model identities represented by the public `v1.0.0-showcase` case study.

## Release identity

| Field | Value |
|---|---|
| Showcase | `v1.0.0-showcase` |
| Runtime | `v1.5` |
| Public status | Ready for publication |
| Recognition transport | Local/offline |

## Private source revisions

| Repository | Represented revision |
|---|---|
| `ParlonsLSQ-Frontend` | `4ffa25aab11106a226c98787f567ca4eb3524fba` |
| `ParlonsLSQ-Backend` | `c33d480db666723bece607990a5ef1b64aac0cf3` |

The source repositories remain private. These SHAs identify the frozen implementation lineage represented here; they do not make source code part of this public repository.

## Frozen recognition identity

| Property | Value |
|---|---|
| Engine | `prototype-lsq-29-v1` |
| Task | Isolated-sign classification |
| Classes | 29 |
| Input | `64 × 228` |
| Feature schema | `legacy-mediapipe-228-v1` |
| Reference model | `final_server.h5` |
| H5 SHA-256 | `98590d3b47e299db7966bdc1d51946de3049d51934280e320e6dfbb18fda8110` |
| Score semantics | Raw classifier outputs, not calibrated confidence |
| Trained unknown detector | None |

## Public evidence assets

| Asset | SHA-256 |
|---|---|
| `screenshots/01-home-web.webp` | `544c5ff857c573c199c97a0c69a4ae3c968f0b21aebb27c8216983bbf45b5614` |
| `screenshots/02-recognition-ready-android.webp` | `36c2ca22c88d5c68990edce29840d60b20573387ef46b53d45fe086101f1b28d` |
| `screenshots/03-recognition-result-android.webp` | `283a0eff17611b9ed89c57daca710b7a49d60332c31392f21fa6745964cb121d` |
| `screenshots/04-recognition-result-web.webp` | `476b9aadb1a392ee133a68793a4067f2c345b1e596a63349597d3110b5023d0d` |
| `screenshots/05-recognition-result-windows.webp` | `5e3b6b93d83b6af77bae152ed00d45f802645f9ddf8e83f733f4f3e65b72ef94` |
| `screenshots/06-rtl.webp` | `eb4a9cff97b12c1e241ddc917f98f056ff848662b22109bba8ebf0454ab1c776` |

The machine-readable equivalent lives in `release/manifest.json`.

## Public/private boundary

This showcase contains documentation and curated visual evidence. It intentionally excludes private Flutter/Python source, model binaries, MediaPipe task assets, raw training/research data, credentials and participant media.

Selected read-only implementation access may be considered under [ACCESS.md](ACCESS.md).
