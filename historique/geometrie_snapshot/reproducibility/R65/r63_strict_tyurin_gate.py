#!/usr/bin/env python3
"""Run the complete R63 mathematical gate and fail closed on any mismatch."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys


ROOT = Path(__file__).resolve().parent

BASELINE = (
    ("r61_resolved_tyurin_lmhs_audit.py", "R61_AUDIT_OUTPUT.txt"),
    ("r62_stable_fan_parity_stop_audit.py", "R62_AUDIT_OUTPUT.txt"),
)

AUDITS = (
    (
        "r63_independent_lattice_fan.py",
        "R63 INDEPENDENT LATTICE/FAN AUDIT: PASS",
    ),
    (
        "r63_independent_jacobian_snc.py",
        "R63 INDEPENDENT JACOBIAN/SNC AUDIT: PASS",
    ),
    (
        "meta_audit_r63/r63_toric_independent_audit.py",
        "R63 INDEPENDENT TORIC RECHECK: PASS",
    ),
    (
        "meta_audit_r63/r63_quasifano_certificate.py",
        "Tyurin/DHT quasi-Fano: YES",
    ),
    (
        "meta_audit_r63/r63_ems_cohomology_audit.py",
        "STRICT_DHT_QUASI_FANO_COHOMOLOGY_GATE: PASS",
    ),
)

REPORTS = (
    "R63_README.md",
    "R63_REPORT.md",
    "R63_CLAIM_LEDGER.csv",
    "R63_DATA_MANIFEST.json",
    "R63_MANIFEST.sha256",
    "R63_ERRATA_R61_R62.md",
    "R63_AUDIT_OUTPUT.txt",
    "meta_audit_r63/corpus_and_gaps.md",
    "meta_audit_r63/toric_recheck.md",
    "meta_audit_r63/independent_cas.md",
    "meta_audit_r63/quasifano_normal_bundles.md",
    "meta_audit_r63/log_lmhs_audit.md",
    "meta_audit_r63/literature_novelty.md",
    "meta_audit_r63/adversarial_referee.md",
    "meta_audit_r63/release_audit.md",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def run(script):
    environment = dict(os.environ)
    environment.pop("PYTHONOPTIMIZE", None)
    completed = subprocess.run(
        [sys.executable, str(ROOT / script)],
        cwd=ROOT,
        env=environment,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(
        completed.returncode == 0,
        f"{script} failed with exit code {completed.returncode}\n{completed.stdout}",
    )
    return completed.stdout


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    require(sys.flags.optimize == 0, "Run R63 without python -O; child assertions are mandatory.")
    require(
        sys.version_info[:2] >= (3, 11),
        f"Python 3.11+ is required, found {sys.version.split()[0]}",
    )

    print("R63 STRICT TYURIN RELEASE GATE")
    print("python:", sys.version.split()[0])

    for script, reference in BASELINE:
        output = run(script)
        expected = (ROOT / reference).read_text(encoding="utf-8")
        require(output == expected, f"{script} no longer matches {reference}")
        print("baseline byte-identical:", script, sha256(ROOT / reference))

    captured = {}
    for script, required_token in AUDITS:
        output = run(script)
        require(required_token in output, f"{script} omitted required verdict token")
        captured[script] = output
        print("audit pass:", script)

    for report in REPORTS:
        path = ROOT / report
        require(path.is_file() and path.stat().st_size > 100, f"missing report: {report}")

    manifest = json.loads((ROOT / "R63_DATA_MANIFEST.json").read_text(encoding="utf-8"))
    manifest_rays = tuple(tuple(row) for row in manifest["relative_rays"])
    manifest_q = tuple(tuple(row) for row in manifest["cox_charge_matrix"])
    manifest_cones = tuple(tuple(row) for row in manifest["maximal_cones"])
    manifest_heights = tuple(manifest["support_heights"])
    manifest_sr = {tuple(row) for row in manifest["relative_sr_minimal"]}

    lattice_namespace = runpy.run_path(str(ROOT / "r63_independent_lattice_fan.py"))
    ems_namespace = runpy.run_path(
        str(ROOT / "meta_audit_r63/r63_ems_cohomology_audit.py")
    )
    quasi_namespace = runpy.run_path(
        str(ROOT / "meta_audit_r63/r63_quasifano_certificate.py")
    )
    for namespace, label in (
        (lattice_namespace, "independent lattice"),
        (ems_namespace, "EMS"),
        (quasi_namespace, "quasi-Fano"),
    ):
        require(tuple(namespace["RAYS"]) == manifest_rays, f"{label} rays diverge from manifest")
        require(
            tuple(namespace["MAXIMAL_CONES"] if "MAXIMAL_CONES" in namespace else namespace["CONES"])
            == manifest_cones,
            f"{label} cones diverge from manifest",
        )
    require(tuple(lattice_namespace["Q"]) == manifest_q, "lattice Q diverges from manifest")
    require(tuple(ems_namespace["Q_ROWS"]) == manifest_q, "EMS Q diverges from manifest")
    require(tuple(lattice_namespace["HEIGHTS"]) == manifest_heights, "heights diverge")
    require(set(quasi_namespace["EXPECTED_SR_PAIRS"]) == manifest_sr, "SR diverges")
    print("data manifest cross-checked against three implementations")

    main_report = (ROOT / "R63_REPORT.md").read_text(encoding="utf-8")
    for required_claim in (
        "STRICT_TYURIN_DEGENERATION = YES",
        "RATIONAL_LMHS = TYPE_II_18",
        "FULL_INTEGRAL_GAUSS_MANIN_SNF = OPEN",
        "MICROMETRIC_VALUE = NOT_DERIVED",
        "PHYSICAL_INFINITE_TOWER = NOT_DERIVED",
        "FANO_PLANE = DEFERRED",
    ):
        require(required_claim in main_report, f"claim boundary missing: {required_claim}")

    print("reports present:", len(REPORTS))
    print("R63 report sha256:", sha256(ROOT / "R63_REPORT.md"))
    print("FINAL VERDICT")
    print("STRICT_DHT_TYURIN_GEOMETRY: PASS")
    print("RATIONAL_TYPE_II_18_LMHS: PASS_FOR_VERY_GENERAL_SEAM")
    print("FULL_INTEGRAL_GAUSS_MANIN_SNF: OPEN")
    print("METRIC_R_AND_PHYSICAL_TOWER: OPEN")
    print("IMMEDIATE_JOURNAL_DEPOSIT: NOT_RELEASED")


if __name__ == "__main__":
    main()

