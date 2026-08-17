# Showcase releases

A Showcase release captures one stable Parlons LSQ research-and-engineering snapshot: the represented private-source revisions, frozen model identity, curated screenshots, and documentation for that generation.

Canonical provenance is recorded in [BUILD_MANIFEST.md](BUILD_MANIFEST.md) and `release/manifest.json`.

## Release validation

The repository includes a standard-library validator:

```powershell
.\scripts\validate_showcase.ps1
```

For a publication snapshot, strict release mode checks provenance and asset integrity:

```powershell
.\scripts\validate_showcase.ps1 -Release
```

It verifies:

- manifest status and source revision format;
- frozen model identity and input contract;
- local/offline Runtime v1.5 recognition transport;
- presence and SHA-256 integrity of each declared screenshot;
- obvious secret/private-key artifacts.

The validator protects the identity of the Showcase snapshot; model-quality research evolves through its own evaluation methods.

## `v1.0.0-showcase`

The first Showcase release represents:

- Frontend `4ffa25aab11106a226c98787f567ca4eb3524fba`;
- Backend/reference `c33d480db666723bece607990a5ef1b64aac0cf3`;
- engine `prototype-lsq-29-v1`;
- six curated Android/Web/Windows/RTL screenshots;
- the Runtime v1.5 architecture, research observations, privacy design, and source-access policy.

## Future releases

A new Showcase version is appropriate when the represented Frontend/Backend revision, model generation, feature schema, public visual set, or research scope changes materially.

Existing release tags stay immutable so earlier checkpoints remain easy to trace. Documentation-only corrections can be published as patch Showcase releases.

Showcase releases describe the project; they do not distribute the private implementation, model binaries, or research datasets.
