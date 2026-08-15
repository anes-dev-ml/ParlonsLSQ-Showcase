# Showcase release policy

The public showcase is a reviewed evidence record for private-source application revisions.

## Release model

A showcase release binds together:

- one Frontend revision;
- one Backend/reference revision;
- one frozen runtime/model identity;
- one reviewed public evidence set;
- the documentation describing those exact boundaries.

The canonical source revisions are recorded in [BUILD_MANIFEST.md](BUILD_MANIFEST.md) and `release/manifest.json`.

## Runtime v1.5 release sequence

1. Freeze implementation.
2. Run product/reference validation.
3. Apply only targeted fixes caused by failed gates.
4. Update represented private-source SHAs if a fix changed either repository.
5. Capture clean visual evidence from the final validated revisions.
6. Insert measured controlled-evaluation results without expanding the claim boundary.
7. Run showcase validation in release mode.
8. Merge the reviewed showcase branch to `main`.
9. Tag the immutable public evidence record as `v1.0.0-showcase`.
10. Make the repository public only after the reviewed release record is ready.

## Correction policy

A public release tag is immutable.

If documentation or evidence later needs correction:

- do not move an existing release tag;
- create a new showcase patch release;
- record what changed and why;
- preserve the previous tag for provenance.

## What requires a new showcase release

A new release record is required when any of these change materially:

- represented Frontend revision;
- represented Backend/reference revision;
- frozen model identity;
- feature schema;
- user-visible evidence;
- controlled evaluation summary;
- claim boundary.

Minor typo corrections that do not alter evidence can still use a patch showcase release once a public tag exists.

## Private implementation releases

Showcase tags are not application distribution releases and do not make the private source repositories public.

Read-only implementation access remains discretionary under [ACCESS.md](ACCESS.md).
