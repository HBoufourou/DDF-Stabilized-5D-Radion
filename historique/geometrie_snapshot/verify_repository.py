#!/usr/bin/env python3
"""Deterministic integrity and scientific-boundary gate for this repository."""

from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXCLUDED_FROM_MANIFEST = {"MANIFEST.sha256", "AUDIT_OUTPUT.txt"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


required = [
    "README.md",
    "STATUS.md",
    "CLAIMS_CURRENT.csv",
    "docs/SCIENTIFIC_STATUS.md",
    "docs/LEGACY_DEPRECATION_MAP.md",
    "docs/PUBLICATION_PLAN.md",
    "docs/CLAIM_POLICY.md",
    "docs/ROADMAP_R66_R70.md",
    "articles/article-G-geometry/README.md",
    "articles/article-KK-spectral/README.md",
    "articles/article-physics/README.md",
    "reproducibility/R65/r65_release_gate.py",
    "reproducibility/R65/R65_AUDIT_OUTPUT.txt",
    "MANIFEST.sha256",
]
for relative in required:
    if not (ROOT / relative).is_file():
        fail(f"missing required file: {relative}")
print(f"required files: {len(required)} present")

with (ROOT / "CLAIMS_CURRENT.csv").open(newline="", encoding="utf-8") as handle:
    claims = list(csv.DictReader(handle))
if len(claims) != 20:
    fail(f"expected 20 current claims, found {len(claims)}")
if len({row["id"] for row in claims}) != len(claims):
    fail("duplicate claim identifiers")
if any(not row["status"].strip() for row in claims):
    fail("empty claim status")
print("claim ledger: 20 unique guarded claims")

boundaries = {
    "README.md": [
        "not a peer-reviewed theory release",
        "micron-scale claims",
        "No folder is labelled \u201cpublishable\u201d",
    ],
    "STATUS.md": ["No complete DDF theory is claimed", "NOT DERIVED"],
    "docs/PUBLICATION_PLAN.md": [
        "not submission-ready",
        "scalar result is not mislabeled as spin-2",
        "micron value is an output",
    ],
}
for relative, phrases in boundaries.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            fail(f"scientific boundary missing from {relative}: {phrase}")
print("scientific boundary language: guarded")

expected_releases = {
    "releases/DDF_R63_STRICT_TYURIN_2026-09-04.zip": "dc6cbc37817183e7d6ba0ae6bd026fed677af04216834addf3f4195da91a9802",
    "releases/DDF_R64_SUBSTANCE_2026-09-04.zip": "d00a781b6cf0aa2827f5e93b82e5f243ae87356e44ee8ed6a841a85d8bb30a3e",
    "releases/DDF_R65_SPECTRAL_PILOT_2026-09-05.zip": "ea99020bf91486b67ccd0aad7d6822124265745f8ef678ee11220c0294212013",
}
for relative, expected in expected_releases.items():
    path = ROOT / relative
    if not path.is_file() or sha256(path) != expected:
        fail(f"release checksum mismatch: {relative}")
print("release archives: R63-R65 byte-verified")

r65_dir = ROOT / "reproducibility/R65"
run = subprocess.run(
    [sys.executable, "r65_release_gate.py"],
    cwd=r65_dir,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    check=False,
)
if run.returncode != 0:
    fail("R65 release gate returned non-zero\n" + run.stdout)
expected_output = (r65_dir / "R65_AUDIT_OUTPUT.txt").read_text(encoding="utf-8")
if run.stdout != expected_output:
    fail("R65 release gate output is not byte-identical to its audit record")
print("R65 executable gate: byte-identical GO")

manifest_rows: dict[str, str] = {}
for line in (ROOT / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
    digest, separator, relative = line.partition("  ")
    if not separator or relative in manifest_rows:
        fail(f"malformed or duplicate manifest row: {line}")
    manifest_rows[relative] = digest

actual_paths = sorted(
    path.relative_to(ROOT).as_posix()
    for path in ROOT.rglob("*")
    if path.is_file()
    and path.relative_to(ROOT).as_posix() not in EXCLUDED_FROM_MANIFEST
    and ".git/" not in path.relative_to(ROOT).as_posix()
)
if set(manifest_rows) != set(actual_paths):
    missing = sorted(set(actual_paths) - set(manifest_rows))
    extra = sorted(set(manifest_rows) - set(actual_paths))
    fail(f"manifest file-set mismatch; missing={missing}, extra={extra}")
for relative in actual_paths:
    if sha256(ROOT / relative) != manifest_rows[relative]:
        fail(f"manifest checksum mismatch: {relative}")
print(f"repository manifest: {len(actual_paths)} files byte-verified")

print("FINAL VERDICT")
print("DDF_CORRECTED_REPOSITORY: GO")
print("PUBLISHABLE_ARTICLE_NOW: NO")
print("NEXT_SCIENTIFIC_ROUND: R66")
print("LEGACY_ARTICLES_I_VIII: DEPRECATED_HISTORICAL_ARCHIVE")
print("R_MICRONS_SPIN2_FANO: NOT_DERIVED")

