# Research direction

Parlons LSQ began with a compact isolated-sign classifier built around manually collected examples and a fixed temporal landmark representation. Runtime v1.5 preserves that baseline so subsequent studies can use a documented reference.

## Baseline

| Property | Runtime v1.5 |
| --- | --- |
| Task | Isolated-sign classification |
| Vocabulary | 29 classes |
| Representation | 64 time steps × 228 features |
| Feature contract | `legacy-mediapipe-228-v1` |
| Model identity | `prototype-lsq-29-v1` |
| Output | Uncalibrated classifier scores |

Successful qualitative recognitions were observed in development and on selected external examples; sensitivity to recording conditions remains an important limitation. These observations are detailed in [Evaluation](EVIDENCE.md).

## Next research questions

The next model generation should test whether performance improves with:

- More signers, sessions, and recording environments
- Explicit signer-disjoint and session-disjoint evaluation
- Better coverage of signing speed, framing, distance, and camera viewpoints
- Visual-temporal representations beyond the legacy 228-feature contract
- Open-set behavior and properly evaluated uncertainty estimates
- Larger focused vocabularies, followed by continuous-signing research where data supports it

Pretrained visual or sign-language encoders may be evaluated against simpler baselines rather than assumed to be superior.

## Data and community considerations

Sign-language datasets require accurate labels, variant awareness, provenance, consent, and appropriate handling of identifiable video. New data collection should involve LSQ users and qualified Deaf-community or linguistic partners as the work develops.

Normal in-app recognition and any future voluntary research-data contribution should remain separate workflows with explicit user choice.

## Reproducibility

Each future experiment should record dataset provenance, train/validation/test splits, checkpoint identity, preprocessing, evaluation metrics, and limitations. The frozen first-generation identifiers are recorded in the [Build manifest](BUILD_MANIFEST.md).

These are planned research directions, not additional results already demonstrated by Runtime v1.5.
