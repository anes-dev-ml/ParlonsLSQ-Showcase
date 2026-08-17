# Screenshots

This directory contains the six curated images used by the `v1.0.0-showcase` case study.

The gallery stays intentionally small: Parlons LSQ is presented primarily as an AI/research-engineering project, while the screenshots show how the frozen prototype reached real Android, Web, and Windows software.

| File | Platform | Shows |
|---|---|---|
| `01-home-web.webp` | Web | Product overview / hero |
| `02-recognition-ready-android.webp` | Android | Physical-device capture flow and camera switching |
| `03-recognition-result-android.webp` | Android | Qualitative external-reference recognition |
| `04-recognition-result-web.webp` | Web | Browser-local recognition result |
| `05-recognition-result-windows.webp` | Windows | Local-worker recognition result |
| `06-rtl.webp` | Windows/desktop UI | Arabic RTL navigation and learning surface |

## Presentation notes

The Web and Windows camera previews were privacy-redacted after capture, with the recognition result and UI state left unchanged. The Android result used external LSQ reference footage as a qualitative check; that source footage is not redistributed here.

The files are optimized WebP presentation copies of the supplied screenshots. Per-file SHA-256 values are recorded in [../BUILD_MANIFEST.md](../BUILD_MANIFEST.md) and `../release/manifest.json`.
