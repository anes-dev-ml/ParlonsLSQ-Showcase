# Evidence and validation

Parlons LSQ separates **implementation status**, **engineering validation**, **controlled prototype evidence**, and **future generalization research**.

This distinction is central to the showcase: a polished interface and a working local model are valuable evidence, but they do not by themselves establish signer-generalized accuracy.

## Current status

Runtime v1.5 implementation is frozen at the private source revisions recorded in [BUILD_MANIFEST.md](BUILD_MANIFEST.md).

Remaining work is validation and evidence capture only. A failed gate can trigger one targeted implementation fix; a passing gate does not trigger another redesign or model change.

## Final validation gates

### Frontend / product

The retained release-candidate checklist verifies:

- dependency resolution, localization generation, analysis, and tests;
- Android physical-device installation and platform identity;
- camera permission and lifecycle behavior;
- recognition state transitions and result actions;
- local saved signs/history persistence;
- French, English, Arabic, and RTL behavior;
- larger text, stronger contrast, and reduced motion;
- Web recognition staying local to the browser;
- Windows local-worker startup and teardown;
- absence of missing-asset, image-codec, and overflow errors.

### Backend / reference runtime

The retained validation gate verifies:

- lint/tests;
- frozen model identity and feature schema;
- fixed input/output signatures;
- H5 ↔ TFLite parity;
- matched cross-platform clip behavior;
- controlled 29-class evaluation;
- privacy/runtime boundary.

## Controlled evaluation target

The predeclared Runtime v1.5 evaluation covers:

```text
29 classes × 5 attempts = 145 controlled trials
```

The final report should include at minimum:

- Top-1 and Top-3 results;
- per-class results;
- failure distribution;
- signer/session conditions;
- platform/runtime identity;
- latency measurements where relevant;
- exact model and feature-schema identifiers.

This evaluation can support claims about the frozen prototype **under the documented conditions**. It does not establish population-level signer generalization.

## Visual evidence policy

Only clean evidence from the final validation snapshot belongs in this public showcase.

The repository intentionally excludes:

- screenshots containing Flutter error banners;
- debug overflow markers;
- stale launcher icons;
- obsolete product layouts;
- screenshots from model/runtime branches that are not the represented release candidate;
- images whose source revision cannot be identified.

## Final screenshot set

The recommended minimum public gallery is small and deliberate rather than a dump of every screen.

### 1. Product overview

- `screenshots/01-home-desktop.png` — wide Home layout;
- `screenshots/02-home-compact.png` — compact/responsive Home layout.

### 2. Recognition

- `screenshots/03-recognition-ready-android.png` — physical Android device, ready/positioning state;
- `screenshots/04-recognition-result-android.png` — successful controlled result;
- `screenshots/05-recognition-uncertain.png` — non-success state demonstrating honest feedback.

### 3. Learning

- `screenshots/06-sign-library.png` — catalogue/search/categories;
- `screenshots/07-sign-detail.png` — detail/source/review presentation;
- `screenshots/08-practice.png` — practice flow.

### 4. User/privacy

- `screenshots/09-privacy.png` — privacy/data screen;
- `screenshots/10-settings-arabic-rtl.png` — Arabic/RTL or settings/accessibility evidence.

### 5. Platform identity

- `screenshots/11-android-launcher.png` — final installed Android icon;
- optional small comparison showing Web/Windows identity if it adds meaningful evidence.

## Video evidence

A short product walkthrough is optional but valuable.

If produced, the strongest 45–75 second sequence is:

```text
Home
→ open Signs
→ open one sign
→ practice
→ Recognition
→ perform one controlled sign
→ result
→ Privacy / language switch
```

The video should show the real release-candidate application. Avoid simulated model output, hidden cuts that imply unsupported behavior, or claims not established by the evaluation.

## Historical smoke evidence

Small earlier checks may be useful as project history, but they should remain labeled **historical smoke evidence**. They are not substitutes for the frozen 145-trial protocol and should not headline the public accuracy story.

## Evidence that should not be fabricated

Do not add placeholder numbers for:

- final Top-1/Top-3 accuracy;
- unseen-signer accuracy;
- cross-platform latency;
- model size/performance comparison;
- data volume;
- signer count;
- clinical/accessibility outcomes.

When the final tests are complete, insert measured results together with the exact conditions.

## Public evidence record

After final capture, the showcase should record:

- represented Frontend SHA;
- represented Backend SHA;
- evidence date;
- screenshot inventory;
- optional SHA-256 hashes for final screenshots/video;
- controlled evaluation summary or link to its reviewed public summary.

The private raw evaluation sessions, research media, and implementation source remain outside this repository.
