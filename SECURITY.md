# Security

This repository is the public Parlons LSQ Showcase. The application source, model/runtime implementation, credentials, research sessions, and datasets are maintained separately.

## Reporting an issue

If you find a security or privacy issue related to Parlons LSQ, contact **[@anes-dev-ml](https://github.com/anes-dev-ml)** with the affected platform/component, version or revision if known, reproduction steps, and the observed impact.

Please avoid posting sensitive reproduction details publicly when they could expose user data, credentials, private research assets, or implementation access.

## Areas of interest

Reports are especially useful for issues involving:

- recognition media unexpectedly leaving its documented runtime boundary;
- local history retaining camera media or feature data;
- unsafe file/path handling in local runtime adapters;
- credential or token exposure;
- unintended access to private repositories, model assets, or research data;
- consent/provenance issues in future research-participation workflows.

## Dependency boundary

Parlons LSQ builds on Flutter, MediaPipe, TensorFlow/LiteRT, browser runtimes, operating-system camera APIs, and other third-party components. Those dependencies retain their own security and support processes.

This Showcase documents the project's architecture and practices; it is not a security certification or bounty program.
