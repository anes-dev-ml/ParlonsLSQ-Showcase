# Prototype results

Runtime v1.5 preserves the first complete Parlons LSQ research-to-product checkpoint: a frozen 29-class isolated-sign model, reproduced across Android, Web, and Windows, with the behavior and limitations of the original small dataset documented clearly.

## Cross-platform deployment

The same recognition contract runs through three platform-specific paths:

| Platform | Runtime path |
|---|---|
| Android | native MediaPipe observations → `64 × 228` → local LiteRT/TFLite |
| Web | local browser clip → MediaPipe Tasks WASM → `64 × 228` → LiteRT.js WASM |
| Windows | local clip → persistent local worker → MediaPipe/OpenCV → frozen H5 |

This turns the original model into a reproducible software system rather than leaving it as a training artifact.

## What we observed

Development use showed two important behaviors.

**Strong performance in familiar conditions.** When signing conditions stayed reasonably close to the original capture setup, the recognizer was reliable enough to support the full product flow.

**Transfer beyond the original capture set.** Successful recognitions were observed with people and reference footage that were not part of the original training captures.

The limitations were equally useful. Changes in signing speed, lighting, framing, distance, camera angle, and body position could reduce reliability quickly. The original dataset simply did not contain enough variation across those dimensions.

That result shaped the next research generation: expand the data and representation rather than spending more effort optimizing the same small 29-class dataset.

## Public visual record

The public gallery is intentionally compact because the model and research story are the focus.

| File | What it shows | SHA-256 |
|---|---|---|
| `screenshots/01-home-web.webp` | Finished Web product surface | `544c5ff857c573c199c97a0c69a4ae3c968f0b21aebb27c8216983bbf45b5614` |
| `screenshots/02-recognition-ready-android.webp` | Physical Android capture flow and camera switching | `36c2ca22c88d5c68990edce29840d60b20573387ef46b53d45fe086101f1b28d` |
| `screenshots/03-recognition-result-android.webp` | Android local recognition result from an external-reference check | `283a0eff17611b9ed89c57daca710b7a49d60332c31392f21fa6745964cb121d` |
| `screenshots/04-recognition-result-web.webp` | Web recognition result | `476b9aadb1a392ee133a68793a4067f2c345b1e596a63349597d3110b5023d0d` |
| `screenshots/05-recognition-result-windows.webp` | Windows recognition result | `5e3b6b93d83b6af77bae152ed00d45f802645f9ddf8e83f733f4f3e65b72ef94` |
| `screenshots/06-rtl.webp` | Arabic RTL layout and learning surface | `eb4a9cff97b12c1e241ddc917f98f056ff848662b22109bba8ebf0454ab1c776` |

The Web and Windows camera previews were privacy-redacted after capture; their recognition result and UI state were left unchanged. The Android result used external LSQ reference footage as a qualitative check, and the source footage itself is not redistributed here.

## How to read this baseline

Runtime v1.5 answers a specific question: can the first hand-built LSQ recognition pipeline be frozen, reproduced, and deployed into a working multi-platform application? The answer is yes.

Broader questions—population-level signer generalization, continuous signing, open-vocabulary recognition, calibrated uncertainty, and large-model behavior—belong to later research generations with larger datasets and stronger evaluation design.

That makes v1.5 useful as a stable point of comparison: future models can improve the science without losing the history of how the project began.
