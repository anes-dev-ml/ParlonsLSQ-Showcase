# Showcase release policy

The public Showcase is a curated research-engineering record for private-source revisions.

## Release model

A Showcase release binds together:

- one Frontend revision;
- one Backend/reference revision;
- one frozen model/runtime identity;
- one curated public evidence set;
- the documentation and claim boundary describing that snapshot.

Canonical provenance is recorded in [BUILD_MANIFEST.md](BUILD_MANIFEST.md) and `release/manifest.json`.

## Release validation

The repository includes a standard-library validator:

```powershell
.\scripts\validate_showcase.ps1
```

For the publication snapshot, use strict release mode:

```powershell
.\scripts\validate_showcase.ps1 -Release
```

Release mode checks that:

- the manifest is marked `ready`;
- Frontend and Backend revisions are valid 40-character SHAs and appear in the public provenance documents;
- the frozen recognition identity has not drifted;
- Runtime v1.5 remains documented as local/offline recognition;
- every declared screenshot exists and matches its recorded SHA-256;
- obvious private-key/secret artifacts are not present.

The release gate deliberately validates **provenance and evidence integrity**, not an invented numeric accuracy requirement for the historical prototype.

## `v1.0.0-showcase`

This release represents:

- Frontend `4ffa25aab11106a226c98787f567ca4eb3524fba`;
- Backend/reference `c33d480db666723bece607990a5ef1b64aac0cf3`;
- engine `prototype-lsq-29-v1`;
- six curated Android/Web/Windows/RTL visual evidence assets;
- the final Runtime v1.5 architecture, research narrative, privacy boundary and source-access policy.

## Correction policy

A public release tag should be treated as immutable. If a material documentation/evidence correction is needed later:

- leave the old tag intact;
- make the correction on `main`;
- publish a patch Showcase release;
- record what changed and why.

## What requires a new Showcase release

A new release is appropriate when the represented Frontend/Backend revision, frozen model identity, feature schema, public evidence set or claim boundary changes materially.

Future research generations should get their own release records rather than silently mutating the v1.5 story.

## Private implementation releases

Showcase tags are evidence/case-study releases, not application-distribution releases. They do not make private implementation repositories or model/data assets public.
