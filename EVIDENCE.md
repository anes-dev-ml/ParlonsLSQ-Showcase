# Evidence record

This document explains what the public Runtime v1.5 showcase demonstrates and how to interpret it without turning prototype evidence into inflated claims.

## Engineering evidence

The frozen recognition contract was carried into working application paths on all three developed targets:

| Platform | Recognition path |
|---|---|
| Android | native MediaPipe observations → `64 × 228` → local LiteRT/TFLite |
| Web | local browser clip → MediaPipe Tasks WASM → `64 × 228` → LiteRT.js WASM |
| Windows | local clip → persistent local worker → MediaPipe/OpenCV → frozen H5 |

This is the central engineering proof of Runtime v1.5: the research artifact did not stop at a notebook or a single-machine script.

## Prototype observations

Development testing showed two complementary behaviors:

1. **Strong behavior in familiar conditions.** Under conditions similar to the original training/capture setup, the 29-class recognizer was reliable enough to support the product workflow.
2. **Promising qualitative transfer with clear robustness limits.** Successful recognitions were observed on inputs from people/reference footage outside the original capture set, while changes in signing speed, lighting, framing, distance and camera/body position could reduce reliability quickly.

Those sensitivities are consistent with the limited variation of the original small dataset and directly motivate the next data/model generation.

No population-level accuracy statistic is inferred from these observations. They are presented as what they are: useful prototype evidence and a clear research lesson.

## Public visual evidence

The public gallery is intentionally small because the model/research story is the focus.

| File | What it demonstrates | SHA-256 |
|---|---|---|
| `screenshots/01-home-web.webp` | Finished Web product surface | `544c5ff857c573c199c97a0c69a4ae3c968f0b21aebb27c8216983bbf45b5614` |
| `screenshots/02-recognition-ready-android.webp` | Physical Android capture flow and camera-switch control | `36c2ca22c88d5c68990edce29840d60b20573387ef46b53d45fe086101f1b28d` |
| `screenshots/03-recognition-result-android.webp` | Android local recognition result from an external-reference check | `283a0eff17611b9ed89c57daca710b7a49d60332c31392f21fa6745964cb121d` |
| `screenshots/04-recognition-result-web.webp` | Web recognition result | `476b9aadb1a392ee133a68793a4067f2c345b1e596a63349597d3110b5023d0d` |
| `screenshots/05-recognition-result-windows.webp` | Windows recognition result | `5e3b6b93d83b6af77bae152ed00d45f802645f9ddf8e83f733f4f3e65b72ef94` |
| `screenshots/06-rtl.webp` | Arabic RTL layout and learning surface | `eb4a9cff97b12c1e241ddc917f98f056ff848662b22109bba8ebf0454ab1c776` |

## Screenshot provenance and privacy

- The Web and Windows camera previews were privacy-redacted after capture; prediction labels and result state were not edited.
- The Android recognition-result example used external LSQ reference footage as a qualitative check. This repository does **not** redistribute that source footage or claim ownership of it.
- No participant dataset, private model binary, raw camera clip, landmark tensor or feature sequence is included in the public showcase.
- Images are optimized WebP presentation copies of the supplied screenshots.

## Claim boundary

The evidence supports a public description of Parlons LSQ as:

> **an experimental LSQ research-engineering project with a frozen 29-class isolated-sign baseline and local cross-platform inference on Android, Web and Windows.**

It does not support claims of continuous LSQ translation, general signer-independent accuracy, open-set recognition, calibrated confidence, clinical validation or a large sign-language model.

## Why this evidence is enough for the first checkpoint

Runtime v1.5 was built to document and preserve the first full research-to-product chain. Its value is that the system is reproducible, deployable and honest about where the small original dataset breaks down.

The next major evidence effort belongs to the larger research generation, where dataset diversity and model scale can justify substantially stronger evaluation.
