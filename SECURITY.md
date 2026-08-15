# Security and responsible disclosure

This public repository is a documentation/evidence showcase. It does not contain the private Parlons LSQ application source, credentials, production configuration, private research sessions, or datasets.

## Reporting a security issue

If you believe you found a security or privacy issue affecting Parlons LSQ, do **not** publish sensitive details in a public issue.

Contact the project owner through **[@anes-dev-ml](https://github.com/anes-dev-ml)** and provide enough information to reproduce and assess the issue safely.

Useful details include:

- affected platform or component;
- version/revision if known;
- reproduction steps;
- expected versus observed behavior;
- potential privacy/security impact;
- whether any real user/research data may have been exposed.

## Areas of particular concern

Responsible reports are especially useful for issues involving:

- camera or recognition media unexpectedly leaving the local runtime;
- local history storing frames, clips, landmarks, or feature tensors contrary to the documented boundary;
- unsafe file/path handling in local runtime adapters;
- credential/token leakage;
- unintended public access to private repositories, model assets, or research data;
- privacy/consent bypass in any future research-participation workflow.

## Scope boundary

The showcase documentation describes reviewed architecture and expected behavior but is not a security certification. Third-party Flutter packages, MediaPipe, TensorFlow/LiteRT, browser runtimes, OS camera systems, and other dependencies retain their own security/support boundaries.

No bounty program or response-time SLA is implied by this document.
