# Visual evidence gallery

Only clean screenshots from the validated Runtime v1.5 revisions belong here.

Do not commit debug screenshots, Flutter error banners, overflow markers, stale branding, or captures from a different private-source revision.

## Required evidence

| File | Purpose |
|---|---|
| `01-home-desktop.png` | Wide Home/product overview |
| `02-home-compact.png` | Compact/responsive Home layout |
| `03-recognition-ready-android.png` | Physical Android recognition ready/positioning state |
| `04-recognition-result-android.png` | Successful controlled Android result |
| `05-recognition-uncertain.png` | Honest non-success/uncertain state |
| `06-sign-library.png` | Learning catalogue/search/categories |
| `07-sign-detail.png` | Sign detail and learning/source presentation |
| `08-practice.png` | Practice flow |
| `09-privacy.png` | Privacy/data boundary in the product |
| `10-settings-arabic-rtl.png` | Arabic RTL or settings/accessibility evidence |
| `11-android-launcher.png` | Final Android launcher identity on a physical device |

## Capture rules

- Use the exact Frontend revision recorded in `../BUILD_MANIFEST.md`.
- Use controlled/demo content only.
- Avoid personal notifications, account identifiers, unrelated desktop content, or real participant data.
- Prefer native-resolution PNG.
- Crop only when it improves focus without hiding relevant product state.
- Do not edit model labels, confidence/score presentation, or UI state after capture.
- Keep one canonical file per evidence role rather than accumulating near-duplicates.

## README selection

The main README should embed approximately 4–6 of the strongest final images rather than every screenshot. This directory remains the full visual evidence index.

## Optional walkthrough

If a short walkthrough video is published, record its filename/hash in `../release/manifest.json` and describe the exact represented Frontend revision.
