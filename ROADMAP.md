# Roadmap

Parlons LSQ's next development stage builds on the frozen Runtime v1.5 isolated-sign baseline. The priorities below are **planned work**, not features or validated results available in this Showcase.

## Data and evaluation

- Collect more varied examples with clear consent and provenance
- Expand signer and session diversity
- Establish signer-disjoint and session-disjoint evaluation protocols
- Measure sensitivity to camera framing, lighting, distance, and signing speed

## Recognition models

- Compare landmark-based and visual-temporal representations
- Evaluate pretrained encoders where appropriate
- Study larger, domain-focused vocabularies
- Investigate rejection and uncertainty mechanisms
- Treat continuous signing as a distinct task requiring separate data and methodology

## Deployment

The compact v1.5 classifier runs locally. Later models may require optimized local execution, hosted inference, or a hybrid system. Architecture decisions should be evaluated against privacy, latency, hardware requirements, maintenance, and operating cost rather than selected in advance.

## Release discipline

Each new research generation should identify its training/evaluation data, preprocessing contract, model weights, and supported claims. Preserve earlier baselines as traceable artifacts.

For the current snapshot, see [Architecture](ARCHITECTURE.md), [Evaluation](EVIDENCE.md), and [Build manifest](BUILD_MANIFEST.md).
