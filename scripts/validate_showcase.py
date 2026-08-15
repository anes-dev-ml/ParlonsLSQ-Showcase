#!/usr/bin/env python3
"""Validate the public Parlons LSQ showcase using only the Python standard library."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "ARCHITECTURE.md",
    "RESEARCH.md",
    "EVIDENCE.md",
    "PRIVACY.md",
    "ACCESS.md",
    "BUILD_MANIFEST.md",
    "ROADMAP.md",
    "RELEASES.md",
    "CHANGELOG.md",
    "SECURITY.md",
    "LICENSE",
    "release/manifest.json",
    "screenshots/README.md",
]

FORBIDDEN_NAMES = {
    ".env",
    ".env.local",
    "id_rsa",
    "id_ed25519",
}

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(?:api[_-]?key|secret[_-]?key|access[_-]?token|refresh[_-]?token)\s*[:=]\s*[\"'][^\"']{8,}"),
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_manifest() -> dict:
    path = ROOT / "release/manifest.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read release manifest: {exc}")
    if not isinstance(data, dict):
        fail("release manifest root must be an object")
    return data


def validate_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))


def validate_manifest(data: dict, release: bool) -> None:
    frontend = data.get("frontend", {}).get("revision")
    backend = data.get("backend_reference", {}).get("revision")
    engine = data.get("recognition", {}).get("engine")
    shape = data.get("recognition", {}).get("input_shape")
    trials = data.get("controlled_evaluation", {}).get("planned_trials")

    for name, value in (("frontend revision", frontend), ("backend revision", backend)):
        if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40}", value):
            fail(f"invalid {name}")

    if engine != "prototype-lsq-29-v1":
        fail("unexpected recognition engine")
    if shape != [64, 228]:
        fail("unexpected frozen input shape")
    if trials != 145:
        fail("controlled evaluation must remain 145 planned trials")

    if data.get("recognition_transport") != "local/offline":
        fail("recognition transport drifted from local/offline")

    if release:
        if data.get("status") != "ready":
            fail("release mode requires manifest status=ready")
        evaluation_status = data.get("controlled_evaluation", {}).get("status")
        if evaluation_status != "complete":
            fail("release mode requires controlled_evaluation.status=complete")
        expected = data.get("expected_screenshots")
        if not isinstance(expected, list) or not expected:
            fail("release mode requires expected_screenshots")
        missing = [path for path in expected if not (ROOT / path).is_file()]
        if missing:
            fail("release mode missing screenshots: " + ", ".join(missing))


def validate_provenance(data: dict) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    build = (ROOT / "BUILD_MANIFEST.md").read_text(encoding="utf-8")
    for label, sha in (
        ("frontend", data["frontend"]["revision"]),
        ("backend", data["backend_reference"]["revision"]),
    ):
        if sha not in readme:
            fail(f"{label} revision missing from README")
        if sha not in build:
            fail(f"{label} revision missing from BUILD_MANIFEST")


def validate_safety() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.name in FORBIDDEN_NAMES:
            fail(f"forbidden sensitive filename: {path.relative_to(ROOT)}")
        if path.suffix.lower() in {".pem", ".p12", ".pfx", ".key"}:
            fail(f"forbidden private-key/certificate artifact: {path.relative_to(ROOT)}")
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".mov", ".ico"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret pattern in {path.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", action="store_true", help="require final evidence and ready status")
    args = parser.parse_args()

    validate_required_files()
    manifest = load_manifest()
    validate_manifest(manifest, args.release)
    validate_provenance(manifest)
    validate_safety()

    mode = "release" if args.release else "record"
    print(f"Parlons LSQ showcase validation passed ({mode} mode).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
