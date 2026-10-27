# Releases

The public Showcase records historical project snapshots. It does not package the private application source, datasets, or model binaries.

## Current snapshot

`v1.0.0-showcase` documents Parlons LSQ Runtime v1.5:

- A 29-class isolated-sign model using 64 × 228 input
- Local Android, Web, and Windows inference paths
- Six curated screenshots
- Frozen model identification and historical source revisions

Full identifiers and checksums are maintained in [Build manifest](BUILD_MANIFEST.md) and [release/manifest.json](release/manifest.json).

## Validate the Showcase

The repository includes a Python standard-library validator:

```sh
python scripts/validate_showcase.py
```

For publication, use its strict release mode as described by `python scripts/validate_showcase.py --help`, or run the PowerShell wrapper:

```powershell
.\scripts\validate_showcase.ps1 -Release
```

The validator checks the release manifest and public artifact integrity. It is **not** a machine-learning accuracy evaluation.

Release tags should remain tied to their original snapshot. Publish changes to model identity, source lineage, or evidence as a new version rather than silently rewriting an earlier release.
