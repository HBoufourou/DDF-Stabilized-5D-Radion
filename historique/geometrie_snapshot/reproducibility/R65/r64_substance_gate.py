#!/usr/bin/env python3
"""Fail-closed release gate for the R64 substance dossier."""

from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent

BASELINE = ("r63_strict_tyurin_gate.py", "R63_AUDIT_OUTPUT.txt")

AUDITS = (
    (
        "meta_audit_r64/r64_equivariant_nogo_audit.py",
        "GENERAL_C4_ACTIVE_NONNEGATIVE_NOGO: POSITIVE_THREE_PLANE_COROLLARY",
    ),
    (
        "meta_audit_r64/r64_lattice_classification.py",
        "U2_ISOMETRY_AND_AMPLE_CONE_CLASSIFICATION: EXACT_COMPLETE",
    ),
    (
        "meta_audit_r64/r64_boundary_certificate.py",
        "VERDICT: EXACT_ARITHMETIC_PASS",
    ),
)

REPORTS = (
    "R64_README.md",
    "R64_REPORT.md",
    "R64_CLAIM_LEDGER.csv",
    "R64_DATA_MANIFEST.json",
    "R64_ERRATA_R62_R63.md",
    "R64_ARTICLE1_DECISION.md",
    "R64_GITHUB_SYNC_NOTE.md",
    "R64_MANIFEST.sha256",
    "R64_AUDIT_OUTPUT.txt",
    "meta_audit_r64/adversarial_pre_referee.md",
    "meta_audit_r64/counterexamples_and_boundaries.md",
    "meta_audit_r64/equivariant_nogo.md",
    "meta_audit_r64/general_construction.md",
    "meta_audit_r64/integrated_final_referee.md",
    "meta_audit_r64/lattice_classification.md",
    "meta_audit_r64/literature_novelty.md",
    "meta_audit_r64/no_go_novelty_comparison.md",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


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
    require(
        completed.returncode == 0,
        f"{script} failed with exit code {completed.returncode}\n{completed.stdout}",
    )
    return completed.stdout


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_hash_manifest() -> int:
    lines = (ROOT / "R64_MANIFEST.sha256").read_text(encoding="utf-8").splitlines()
    checked = 0
    for line in lines:
        if not line or line.startswith("#"):
            continue
        fields = line.split(maxsplit=1)
        require(len(fields) == 2, f"malformed hash line: {line}")
        expected, relative = fields
        path = ROOT / relative
        require(path.is_file(), f"hashed file missing: {relative}")
        require(sha256(path) == expected, f"hash mismatch: {relative}")
        checked += 1
    require(checked >= 18, f"too few files in hash manifest: {checked}")
    return checked


def verify_parity_manifest(data: dict[str, object]) -> None:
    route = data["route_B_parity_hodge"]
    require(isinstance(route, dict), "route_B_parity_hodge must be an object")
    rows = route["parity_table"]
    require(isinstance(rows, list) and len(rows) == 4, "four parity rows required")

    expected = {
        ("O3/O7", "preserved"): (-1, +1, -1, +1),
        ("O3/O7", "exchanged"): (-1, -1, +1, -1),
        ("O5/O9", "preserved"): (+1, +1, +1, -1),
        ("O5/O9", "exchanged"): (+1, -1, -1, +1),
    }
    seen: set[tuple[str, str]] = set()
    for row in rows:
        require(isinstance(row, dict), "parity row must be an object")
        key = (str(row["projection"]), str(row["branches"]))
        require(key in expected, f"unexpected parity row: {key}")
        s = int(row["s"])
        eta = int(row["eta"])
        omega = int(row["epsilon_OmegaS"])
        curve = int(row["epsilon_C"])
        require((s, eta, omega, curve) == expected[key], f"wrong row: {key}")
        require(omega == s * eta, f"Omega seam identity failed: {key}")
        require(curve == -omega, f"curve/Omega parity identity failed: {key}")
        require(curve * eta == -s, f"C4 vector survival identity failed: {key}")
        seen.add(key)
    require(seen == set(expected), "parity table is incomplete")


def verify_claim_ledger() -> None:
    with (ROOT / "R64_CLAIM_LEDGER.csv").open(
        "r", encoding="utf-8", newline=""
    ) as handle:
        rows = {row["id"]: row for row in csv.DictReader(handle)}
    required = {
        "R64-C03": "PROVED",
        "R64-C04": "FAIL_PRIOR_ART",
        "R64-C07": "PROVED_CONDITIONALLY_RATIONAL",
        "R64-C09": "PROVED_CONDITIONALLY_RATIONAL",
        "R64-C10": "DERIVED_CONDITIONALLY",
        "R64-C11": "DERIVED_CONDITIONALLY",
        "R64-C12": "PROVED_CONDITIONAL_ON_NS_EQUALS_U2",
        "R64-C20": "DISPROVED",
        "R64-C22": "FAIL_BROAD_NOVELTY",
        "R64-C23": "PLAUSIBLE_NOT_CERTIFIED",
        "R64-C25": "FALSE_SCOPE",
        "R64-C27": "NOT_DERIVED",
        "R64-C28": "NOT_DERIVED",
        "R64-C29": "NO_GO",
        "R64-C30": "DEFERRED",
        "R64-C31": "FALSE_CURRENT_STATE",
    }
    for claim_id, status in required.items():
        require(claim_id in rows, f"claim missing: {claim_id}")
        require(rows[claim_id]["status"] == status, f"wrong status: {claim_id}")


def main() -> None:
    require(sys.flags.optimize == 0, "Run R64 without python -O.")
    require(
        sys.version_info[:2] >= (3, 11),
        f"Python 3.11+ is required, found {sys.version.split()[0]}",
    )

    print("R64 SUBSTANCE RELEASE GATE")
    print("python:", sys.version.split()[0])

    baseline_output = run(BASELINE[0])
    baseline_reference = (ROOT / BASELINE[1]).read_text(encoding="utf-8")
    require(baseline_output == baseline_reference, "R63 gate no longer matches its release")
    print("R63 baseline byte-identical:", sha256(ROOT / BASELINE[1]))

    for script, token in AUDITS:
        output = run(script)
        require(token in output, f"{script} omitted required verdict token")
        print("audit pass:", script)

    for report in REPORTS:
        path = ROOT / report
        require(path.is_file() and path.stat().st_size > 100, f"missing report: {report}")

    data = json.loads((ROOT / "R64_DATA_MANIFEST.json").read_text(encoding="utf-8"))
    require(data["schema"] == "ddf-r64-substance-manifest-v1", "wrong schema")
    verify_parity_manifest(data)
    route_b = data["route_B_parity_hodge"]
    require(
        route_b["conclusion"]
        == "under the equivariant-tube hypothesis, every nonzero surviving active closed-C4 eigenclass has a rational orthogonal representative of negative square",
        "main proposition boundary changed",
    )
    require(
        route_b["integral_equivariant_tube_map"] == "open",
        "integral tube-map boundary missing",
    )
    require(
        data["novelty_verdict"]["standalone_no_go_article"] == "no_go",
        "standalone novelty guard missing",
    )
    require(
        data["next_round"]["round"] == "R65",
        "roadmap must continue with R65 spectral pilot",
    )
    require(
        data["public_repository_audit"]["remote_write_performed"] is False,
        "unexpected remote repository write",
    )
    print("four-case parity manifest: exact")

    verify_claim_ledger()
    print("claim ledger: guarded")

    main_report = (ROOT / "R64_REPORT.md").read_text(encoding="utf-8")
    for token in (
        "R64_INTERNAL_SUBSTANCE_GATE = PASS_NARROW",
        "INTEGRAL_EQUIVARIANT_TUBE_MAP = OPEN",
        "GLOBAL_ORIENTIFOLD_REALIZATIONS = NOT_CONSTRUCTED",
        "INDEPENDENT_NOVELTY_CERTIFICATION = OPEN",
        "ARTICLE_1_READY_FOR_SUBMISSION = NO",
        "METRIC_R_AND_MICROMETRIC_SCALE = NOT_DERIVED",
        "NEUTRAL_KK_OR_OPEN_STRING_TOWER = NOT_EXCLUDED",
        "FANO_PLANE = DEFERRED",
    ):
        require(token in main_report, f"main report boundary missing: {token}")

    novelty = (ROOT / "meta_audit_r64/no_go_novelty_comparison.md").read_text(
        encoding="utf-8"
    )
    require(
        "BROAD_ORIENTIFOLD_OBSTRUCTION_NOVELTY = FAIL" in novelty,
        "prior-art collision guard missing",
    )
    require(
        "STANDALONE_THEOREM_PAPER               = NO" in novelty,
        "standalone-paper guard missing",
    )

    referee = (ROOT / "meta_audit_r64/integrated_final_referee.md").read_text(
        encoding="utf-8"
    )
    require(
        "R64_INTEGRATED_REFEREE_VERDICT: PASS_WITH_LIMITS" in referee,
        "integrated referee did not release the bounded result",
    )

    hashed = verify_hash_manifest()
    print("hash manifest files checked:", hashed)
    print("reports present:", len(REPORTS))
    print("R64 report sha256:", sha256(ROOT / "R64_REPORT.md"))
    print("FINAL VERDICT")
    print("GENERAL_ANTICANONICAL_CUT: PASS_BUT_STANDARD")
    print("PARITY_HODGE_C4_EIGENTUBE_PROPOSITION: PASS_CONDITIONALLY_RATIONAL")
    print("R64_SUBSTANCE: PASS_NARROW")
    print("BROAD_NOVELTY_AND_STANDALONE_NO_GO_ARTICLE: FAIL")
    print("ARTICLE_1_IMMEDIATE_SUBMISSION: HOLD")
    print("METRIC_R_MICRONS_KK_FANO: OPEN_OR_DEFERRED")


if __name__ == "__main__":
    main()

