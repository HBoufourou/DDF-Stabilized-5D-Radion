#!/usr/bin/env python3
"""Fail-closed release gate for the R65 spectral pilot dossier."""

from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run(script: str) -> str:
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
    require(completed.returncode == 0, f"{script} failed\n{completed.stdout}")
    return completed.stdout


def verify_hash_manifest() -> int:
    checked = 0
    for line in (ROOT / "R65_MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        fields = line.split(maxsplit=1)
        require(len(fields) == 2, f"malformed manifest line: {line}")
        expected, relative = fields
        path = ROOT / relative
        require(path.is_file(), f"manifest file missing: {relative}")
        require(sha256(path) == expected, f"hash mismatch: {relative}")
        checked += 1
    require(checked >= 60, f"manifest too short: {checked}")
    return checked


def csv_rows(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def verify_claims() -> None:
    rows = {row["id"]: row for row in csv_rows("R65_CLAIM_LEDGER.csv")}
    required = {
        "R65-C01": "PROVED_WITH_TRACE",
        "R65-C02": "PROVED_ON_ANALYTIC_CONTROLS",
        "R65-C03": "PROVED_ON_ANALYTIC_CONTROL",
        "R65-C04": "PROVED_FOR_PILOT",
        "R65-C05": "PROVED_5_OF_5",
        "R65-C06": "PROVED_4_OF_5",
        "R65-C07": "FALSE_BY_PREREGISTERED_RULE",
        "R65-C08": "GO_PIPELINE",
        "R65-C09": "NOT_TESTED",
        "R65-C10": "FALSE_SCOPE",
        "R65-C11": "NOT_DERIVED",
        "R65-C12": "NOT_DERIVED",
        "R65-C13": "NOT_DERIVED",
        "R65-C14": "FALSE_NUMERICAL_ALIASING",
        "R65-C15": "FALSE",
        "R65-C16": "DEFERRED",
    }
    for claim, status in required.items():
        require(claim in rows, f"claim missing: {claim}")
        require(rows[claim]["status"] == status, f"claim status changed: {claim}")


def main() -> None:
    require(sys.flags.optimize == 0, "Run without python -O")
    require(sys.version_info[:2] >= (3, 11), "Python 3.11+ required")
    print("R65 SPECTRAL RELEASE GATE")
    print("python:", sys.version.split()[0])

    r64_output = run("r64_substance_gate.py")
    r64_reference = (ROOT / "R64_AUDIT_OUTPUT.txt").read_text(encoding="utf-8")
    require(r64_output == r64_reference, "R64 baseline changed")
    print("R64 baseline byte-identical:", sha256(ROOT / "R64_AUDIT_OUTPUT.txt"))

    config = json.loads((ROOT / "R65_CONFIG.json").read_text(encoding="utf-8"))
    results_before = json.loads((ROOT / "R65_RESULTS.json").read_text(encoding="utf-8"))
    require(config["schema"] == "ddf-r65-preregistered-spectral-pilot-v1", "wrong config")
    require(results_before["config_sha256"] == sha256(ROOT / "R65_CONFIG.json"), "config hash changed")
    require(
        results_before["preregistration_sha256"] == sha256(ROOT / "R65_PREREGISTRATION.md"),
        "preregistration hash changed",
    )
    print("config frozen:", results_before["config_sha256"])
    print("preregistration frozen:", results_before["preregistration_sha256"])

    fresh_output = run("r65_spectral_pilot.py")
    frozen_output = (ROOT / "R65_RUN_OUTPUT.txt").read_text(encoding="utf-8")
    require(fresh_output == frozen_output, "fresh spectral run output changed")
    results = json.loads((ROOT / "R65_RESULTS.json").read_text(encoding="utf-8"))
    require(results == results_before, "fresh structured results changed")
    print("fresh spectral run: byte-identical structured results")

    require(results["global_gate"] == "GO_PIPELINE", "pilot gate not GO")
    require(results["dimensionless_only"] is True, "dimensionless guard removed")
    require(results["spin2_not_computed"] is True, "spin-2 boundary removed")
    require(results["ddf_geometry_not_tested"] is True, "DDF scope boundary removed")
    require(all(results["positive_control_pass"].values()), "positive control failed")
    require(results["transverse_rejection_count"] == 5, "transverse rejection count changed")
    require(results["transverse_rejected"] is True, "transverse false positive accepted")
    require(results["tunneling_rejection_count"] == 4, "tunneling rejection count changed")
    require(results["tunneling_rejected"] is True, "tunneling false positive accepted")

    thresholds = config["thresholds"]
    positive_names = set(results["positive_control_pass"])
    for row in results["product_metrics"]:
        if row["model"] not in positive_names:
            continue
        require(row["point_pass"] is True, "positive parameter point failed")
        require(
            row["richardson_change_fv"] < thresholds["max_richardson_relative_change_first10"],
            "FV convergence threshold failed",
        )
        require(
            row["richardson_change_fem"] < thresholds["max_richardson_relative_change_first10"],
            "FEM convergence threshold failed",
        )
        require(
            row["cross_method_difference"] < thresholds["max_cross_method_relative_difference_first10"],
            "cross-method threshold failed",
        )
        require(
            row["quadratic_relative_l2_residual"] < thresholds["max_quadratic_relative_l2_residual"],
            "quadratic threshold failed",
        )
        require(row["transverse_modes_first10"] == 0, "transverse mode leaked into positive control")

    spectra = csv_rows("R65_SPECTRA.csv")
    metrics = csv_rows("R65_METRICS.csv")
    profiles = csv_rows("R65_PROFILES.csv")
    require(len(spectra) == 750, f"wrong spectral row count: {len(spectra)}")
    require(len(metrics) == 25, f"wrong metric row count: {len(metrics)}")
    require(len(profiles) == 801, f"wrong profile row count: {len(profiles)}")
    require((ROOT / "R65_SPECTRAL_DIAGNOSTICS.png").stat().st_size > 150000, "figure missing")
    print("data rows: spectra=750 metrics=25 profiles=801")

    verify_claims()
    print("claim ledger: guarded")
    report = (ROOT / "R65_REPORT.md").read_text(encoding="utf-8")
    for token in (
        "R65_SPECTRAL_PIPELINE = GO",
        "DDF_GEOMETRY_SPECTRUM = NOT_TESTED",
        "SPIN2_KK_SPECTRUM = NOT_TESTED",
        "R_OF_T_AND_MICROMETRIC_SCALE = NOT_DERIVED",
        "FANO_PLANE = DEFERRED",
        "R66_REAL_GEOMETRY_PILOT = AUTHORIZED_AFTER_PLATFORM_LOCK",
        "Incident numérique conservé",
    ):
        require(token in report, f"report boundary missing: {token}")
    print("aliasing incident disclosure: present")

    hashed = verify_hash_manifest()
    print("hash manifest files checked:", hashed)
    print("R65 results sha256:", sha256(ROOT / "R65_RESULTS.json"))
    print("FINAL VERDICT")
    print("R65_SPECTRAL_PIPELINE: GO")
    print("POSITIVE_1D_CONTROLS: PASS_3_OF_3")
    print("TRANSVERSE_FALSE_POSITIVE: REJECTED_5_OF_5")
    print("CHEEGER_TUNNELING_FALSE_POSITIVE: REJECTED_4_OF_5")
    print("R66: AUTHORIZED_AFTER_SINGLE_PLATFORM_LOCK")
    print("DDF_METRIC_SPIN2_R_MICRONS_FANO: NOT_DERIVED")


if __name__ == "__main__":
    main()

