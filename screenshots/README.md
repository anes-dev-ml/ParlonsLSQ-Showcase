# Visual evidence gallery

This directory contains the six curated images used by the `v1.0.0-showcase` case study.

The set is deliberately small. Parlons LSQ is presented primarily as an AI/research-engineering project; the application screenshots prove that the frozen prototype was carried into real cross-platform software.

| File | Platform | Purpose |
|---|---|---|
| `01-home-web.webp` | Web | Product overview / hero |
| `02-recognition-ready-android.webp` | Android | Physical-device capture flow and camera switching |
| `03-recognition-result-android.webp` | Android | Successful qualitative external-reference recognition |
| `04-recognition-result-web.webp` | Web | Browser-local recognition result |
| `05-recognition-result-windows.webp` | Windows | Local-worker recognition result |
| `06-rtl.webp` | Windows/desktop UI | Arabic RTL navigation and learning surface |

## Integrity and privacy notes

- These files are optimized WebP presentation copies of the supplied screenshots.
- Web and Windows camera previews were privacy-redacted after capture. Recognition labels/result state were not edited.
- The Android result used external LSQ reference footage as a qualitative test. The source footage itself is not redistributed here and is not claimed as project-owned media.
- No debug overlays, private notifications, participant datasets, model binary or raw research capture is included.

Per-file SHA-256 values are recorded in [../BUILD_MANIFEST.md](../BUILD_MANIFEST.md) and `../release/manifest.json`.
