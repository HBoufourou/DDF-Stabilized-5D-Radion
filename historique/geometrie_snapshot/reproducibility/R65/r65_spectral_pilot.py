#!/usr/bin/env python3
"""R65 preregistered spectral pilot.

The program validates a spectral classifier on analytic product controls and
two registered false positives.  It does not model the DDF Ricci-flat metric.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import least_squares
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "R65_CONFIG.json"
PREREG_PATH = ROOT / "R65_PREREGISTRATION.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def length_from_t(t_abs: float) -> float:
    return 6.0 * (1.0 - math.log10(t_abs))


def axis_eigenvalue(method: str, bc: str, length: float, resolution: int, k: int) -> float:
    """Continuum, cell-centered FV/FD, or P1-FEM eigenvalue on one axis."""
    if method == "exact":
        factor = 2.0 if bc == "periodic" else 1.0
        return (factor * math.pi * k / length) ** 2

    n = int(round(length * resolution))
    require(n >= 4 and abs(n / resolution - length) < 1e-12, "unaligned grid")
    h = length / n
    theta = (2.0 * math.pi * k / n) if bc == "periodic" else (math.pi * k / n)
    if method == "fv":
        return 2.0 * (1.0 - math.cos(theta)) / h**2
    if method == "fem":
        return 6.0 * (1.0 - math.cos(theta)) / (h**2 * (2.0 + math.cos(theta)))
    raise ValueError(method)


def axis_residual(method: str, bc: str, length: float, resolution: int, k: int) -> float:
    """Relative algebraic residual for the closed-form discrete eigenvector."""
    n = int(round(length * resolution))
    h = length / n

    if method == "fv":
        if bc == "dirichlet":
            j = np.arange(1, n, dtype=float)
            vector = np.sin(math.pi * k * j / n)
            diagonal = np.full(n - 1, 2.0 / h**2)
            off = np.full(n - 2, -1.0 / h**2)
        elif bc == "neumann":
            j = np.arange(n, dtype=float)
            vector = np.cos(math.pi * k * (j + 0.5) / n)
            diagonal = np.full(n, 2.0 / h**2)
            diagonal[[0, -1]] = 1.0 / h**2
            off = np.full(n - 1, -1.0 / h**2)
        elif bc == "periodic":
            j = np.arange(n, dtype=float)
            vector = np.cos(2.0 * math.pi * k * j / n)
            matrix = diags(
                [np.full(n - 1, -1.0 / h**2), np.full(n, 2.0 / h**2), np.full(n - 1, -1.0 / h**2)],
                [-1, 0, 1],
                format="lil",
            )
            matrix[0, -1] = -1.0 / h**2
            matrix[-1, 0] = -1.0 / h**2
            matrix = matrix.tocsr()
            lam = axis_eigenvalue(method, bc, length, resolution, k)
            left = matrix @ vector
            right = lam * vector
            denom = np.linalg.norm(left) + np.linalg.norm(right)
            return 0.0 if denom == 0.0 else float(np.linalg.norm(left - right) / denom)
        else:
            raise ValueError(bc)
        matrix = diags([off, diagonal, off], [-1, 0, 1], format="csr")
        lam = axis_eigenvalue(method, bc, length, resolution, k)
        left = matrix @ vector
        right = lam * vector
    elif method == "fem":
        if bc == "dirichlet":
            j = np.arange(1, n, dtype=float)
            vector = np.sin(math.pi * k * j / n)
            kdiag = np.full(n - 1, 2.0 / h)
            koff = np.full(n - 2, -1.0 / h)
            mdiag = np.full(n - 1, 2.0 * h / 3.0)
            moff = np.full(n - 2, h / 6.0)
            stiffness = diags([koff, kdiag, koff], [-1, 0, 1], format="csr")
            mass = diags([moff, mdiag, moff], [-1, 0, 1], format="csr")
        elif bc == "neumann":
            j = np.arange(n + 1, dtype=float)
            vector = np.cos(math.pi * k * j / n)
            kdiag = np.full(n + 1, 2.0 / h)
            kdiag[[0, -1]] = 1.0 / h
            koff = np.full(n, -1.0 / h)
            mdiag = np.full(n + 1, 2.0 * h / 3.0)
            mdiag[[0, -1]] = h / 3.0
            moff = np.full(n, h / 6.0)
            stiffness = diags([koff, kdiag, koff], [-1, 0, 1], format="csr")
            mass = diags([moff, mdiag, moff], [-1, 0, 1], format="csr")
        elif bc == "periodic":
            j = np.arange(n, dtype=float)
            vector = np.cos(2.0 * math.pi * k * j / n)
            stiffness = diags(
                [np.full(n - 1, -1.0 / h), np.full(n, 2.0 / h), np.full(n - 1, -1.0 / h)],
                [-1, 0, 1],
                format="lil",
            )
            mass = diags(
                [np.full(n - 1, h / 6.0), np.full(n, 2.0 * h / 3.0), np.full(n - 1, h / 6.0)],
                [-1, 0, 1],
                format="lil",
            )
            stiffness[0, -1] = stiffness[-1, 0] = -1.0 / h
            mass[0, -1] = mass[-1, 0] = h / 6.0
            stiffness = stiffness.tocsr()
            mass = mass.tocsr()
        else:
            raise ValueError(bc)
        lam = axis_eigenvalue(method, bc, length, resolution, k)
        left = stiffness @ vector
        right = lam * (mass @ vector)
    else:
        raise ValueError(method)

    denom = np.linalg.norm(left) + np.linalg.norm(right)
    return 0.0 if denom == 0.0 else float(np.linalg.norm(left - right) / denom)


def product_spec(model: str, length: float, method: str, resolution: int | None, count: int = 30):
    if model == "kk_interval_neumann":
        xbc, ybc, width, xstart = "neumann", "neumann", 1.0, 0
    elif model == "kk_interval_dirichlet":
        xbc, ybc, width, xstart = "dirichlet", "neumann", 1.0, 1
    elif model == "kk_circle_periodic":
        xbc, ybc, width, xstart = "periodic", "periodic", 1.0, 0
    elif model == "transverse_contaminated":
        xbc, ybc, width, xstart = "neumann", "neumann", length / 3.0, 0
    else:
        raise ValueError(model)

    eval_method = "exact" if method == "exact" else method
    use_resolution = 1 if resolution is None else resolution

    def maximum_index(bc: str, axis_length: float, analytic_cap: int) -> int:
        if method == "exact":
            return analytic_cap
        cells = int(round(axis_length * use_resolution))
        if bc == "periodic":
            return min(analytic_cap, cells // 2)
        return min(analytic_cap, cells - 1)

    kx_max = maximum_index(xbc, length, 100)
    ky_max = maximum_index(ybc, width, 30)
    candidates = []
    for kx in range(xstart, kx_max + 1):
        for ky in range(0, ky_max + 1):
            if kx == 0 and ky == 0:
                continue
            value = axis_eigenvalue(eval_method, xbc, length, use_resolution, kx)
            value += axis_eigenvalue(eval_method, ybc, width, use_resolution, ky)
            if model == "kk_circle_periodic":
                multiplicity = (2 if kx > 0 else 1) * (2 if ky > 0 else 1)
            else:
                multiplicity = 1
            candidates.append(
                {
                    "value": float(value),
                    "kx": kx,
                    "ky": ky,
                    "multiplicity": multiplicity,
                    "xbc": xbc,
                    "ybc": ybc,
                    "width": width,
                }
            )
    candidates.sort(key=lambda row: (row["value"], row["ky"], row["kx"]))
    return candidates[:count]


def fit_spectrum(values: np.ndarray) -> dict[str, float]:
    values = np.asarray(values[:10], dtype=float)
    n = np.arange(1.0, 11.0)
    scale = float(values[-1])
    y = values / scale
    initial_a = max((y[-1] - y[0]) / 99.0, 1e-6)

    def qres(par):
        a, delta, c = par
        return a * (n + delta) ** 2 + c - y

    qfit = least_squares(
        qres,
        x0=np.array([initial_a, 0.0, 0.0]),
        bounds=(np.array([1e-12, -0.49, -2.0]), np.array([10.0, 0.49, 2.0])),
        xtol=1e-14,
        ftol=1e-14,
        gtol=1e-14,
        max_nfev=10000,
    )
    qa, qdelta, qc = qfit.x
    qpred = qa * (n + qdelta) ** 2 + qc
    qrelative = float(np.linalg.norm(qpred - y) / np.linalg.norm(y))

    def pres(par):
        a, delta, c, exponent = par
        return a * (n + delta) ** exponent + c - y

    pfit = least_squares(
        pres,
        x0=np.array([initial_a, 0.0, 0.0, 2.0]),
        bounds=(np.array([1e-12, -0.49, -2.0, 0.5]), np.array([10.0, 0.49, 2.0, 4.0])),
        xtol=1e-13,
        ftol=1e-13,
        gtol=1e-13,
        max_nfev=20000,
    )
    pa, pdelta, pc, exponent = pfit.x
    ppred = pa * (n + pdelta) ** exponent + pc
    prelative = float(np.linalg.norm(ppred - y) / np.linalg.norm(y))
    counting_slope = float(np.polyfit(np.log(values), np.log(n), 1)[0])
    return {
        "a": float(qa * scale),
        "delta": float(qdelta),
        "c": float(qc * scale),
        "quadratic_relative_l2_residual": qrelative,
        "free_exponent": float(exponent),
        "free_power_relative_l2_residual": prelative,
        "effective_counting_dimension": 2.0 * counting_slope,
    }


def richardson_metrics(spectra_by_resolution: dict[int, np.ndarray]) -> tuple[np.ndarray, float]:
    resolutions = sorted(spectra_by_resolution)
    medium = spectra_by_resolution[resolutions[-2]][:10]
    fine = spectra_by_resolution[resolutions[-1]][:10]
    extrapolated = (4.0 * fine - medium) / 3.0
    relative = np.abs(extrapolated - fine) / np.maximum(np.abs(extrapolated), 1e-30)
    return extrapolated, float(np.max(relative))


def area_profile(x: np.ndarray, epsilon: float) -> np.ndarray:
    ax = np.abs(np.asarray(x))
    area = np.ones_like(ax, dtype=float)
    area[ax <= 0.25] = epsilon
    transition = (ax > 0.25) & (ax < 0.75)
    area[transition] = epsilon + (1.0 - epsilon) * (ax[transition] - 0.25) / 0.50
    return area


def solve_dumbbell_fv(epsilon: float, cells: int, modes: int = 30):
    left, right = -2.0, 2.0
    h = (right - left) / cells
    x = left + (np.arange(cells) + 0.5) * h
    area = area_profile(x, epsilon)
    face_area = 2.0 * area[:-1] * area[1:] / (area[:-1] + area[1:])
    conductance = face_area / h
    kdiag = np.zeros(cells)
    kdiag[:-1] += conductance
    kdiag[1:] += conductance
    koff = -conductance
    mass_diag = area * h
    bdiag = kdiag / mass_diag
    boff = koff / np.sqrt(mass_diag[:-1] * mass_diag[1:])
    eigenvalues, bvec = eigh_tridiagonal(
        bdiag,
        boff,
        select="i",
        select_range=(0, modes),
        check_finite=True,
    )
    order = np.argsort(eigenvalues)
    eigenvalues = np.maximum(eigenvalues[order], 0.0)
    bvec = bvec[:, order]
    vectors = bvec / np.sqrt(mass_diag)[:, None]

    residuals = []
    for column, lam in enumerate(eigenvalues[1:11], start=1):
        u = vectors[:, column]
        ku = kdiag * u
        ku[:-1] += koff * u[1:]
        ku[1:] += koff * u[:-1]
        rhs = lam * mass_diag * u
        denominator = np.linalg.norm(ku) + np.linalg.norm(rhs)
        residuals.append(0.0 if denominator == 0.0 else np.linalg.norm(ku - rhs) / denominator)

    u1 = vectors[:, 1]
    face_x = 0.5 * (x[:-1] + x[1:])
    energy = conductance * np.diff(u1) ** 2
    neck_fraction = float(np.sum(energy[np.abs(face_x) < 0.75]) / np.sum(energy))
    return {
        "values": eigenvalues[1 : modes + 1],
        "max_residual_first10": float(max(residuals)),
        "neck_energy_fraction": neck_fraction,
        "x": x,
        "u1": u1,
    }


def solve_dumbbell_fem(epsilon: float, elements: int, modes: int = 30):
    left, right = -2.0, 2.0
    h = (right - left) / elements
    x = np.linspace(left, right, elements + 1)
    midpoint = 0.5 * (x[:-1] + x[1:])
    area_element = area_profile(midpoint, epsilon)

    kdiag = np.zeros(elements + 1)
    kdiag[:-1] += area_element / h
    kdiag[1:] += area_element / h
    koff = -area_element / h
    mdiag = np.zeros(elements + 1)
    mdiag[:-1] += area_element * h / 3.0
    mdiag[1:] += area_element * h / 3.0
    moff = area_element * h / 6.0
    stiffness = diags([koff, kdiag, koff], [-1, 0, 1], format="csr")
    mass = diags([moff, mdiag, moff], [-1, 0, 1], format="csr")
    eigenvalues, vectors = eigsh(
        stiffness,
        k=modes + 1,
        M=mass,
        sigma=-1e-10,
        which="LM",
        tol=1e-12,
        maxiter=200000,
        v0=np.linspace(1.0, 2.0, elements + 1),
    )
    order = np.argsort(eigenvalues)
    eigenvalues = np.maximum(eigenvalues[order], 0.0)
    vectors = vectors[:, order]

    residuals = []
    for column, lam in enumerate(eigenvalues[1:11], start=1):
        u = vectors[:, column]
        ku = stiffness @ u
        rhs = lam * (mass @ u)
        denominator = np.linalg.norm(ku) + np.linalg.norm(rhs)
        residuals.append(0.0 if denominator == 0.0 else np.linalg.norm(ku - rhs) / denominator)

    u1 = vectors[:, 1]
    energy = area_element / h * np.diff(u1) ** 2
    neck_fraction = float(np.sum(energy[np.abs(midpoint) < 0.75]) / np.sum(energy))
    norm = math.sqrt(float(u1 @ (mass @ u1)))
    u1 = u1 / norm
    if np.mean(u1[x > 1.0]) < 0.0:
        u1 = -u1
    return {
        "values": eigenvalues[1 : modes + 1],
        "max_residual_first10": float(max(residuals)),
        "neck_energy_fraction": neck_fraction,
        "x": x,
        "u1": u1,
    }


def positive_point_metrics(model: str, t_abs: float, config: dict, spectra_rows: list[dict]) -> dict:
    length = length_from_t(t_abs)
    resolutions = config["resolutions"]["product_cells_per_unit"]
    exact = product_spec(model, length, "exact", None)
    numerical: dict[str, dict[int, list[dict]]] = {"fv": {}, "fem": {}}
    for method in numerical:
        for resolution in resolutions:
            numerical[method][resolution] = product_spec(model, length, method, resolution)

    extrapolated = {}
    changes = {}
    for method in numerical:
        arrays = {
            resolution: np.array([row["value"] for row in numerical[method][resolution]])
            for resolution in resolutions
        }
        extrapolated[method], changes[method] = richardson_metrics(arrays)
    merged = 0.5 * (extrapolated["fv"] + extrapolated["fem"])
    cross = float(
        np.max(
            np.abs(extrapolated["fv"] - extrapolated["fem"])
            / np.maximum(np.abs(merged), 1e-30)
        )
    )

    fit = fit_spectrum(merged)
    factor = 2.0 if model == "kk_circle_periodic" else 1.0
    effective_length = factor * math.pi / math.sqrt(fit["a"])
    length_error = abs(effective_length - length) / length
    first10 = exact[:10]
    transverse_count = sum(row["ky"] > 0 for row in first10)
    xbc = first10[0]["xbc"]
    ybc = first10[0]["ybc"]
    width = first10[0]["width"]
    transverse_threshold = axis_eigenvalue("exact", ybc, width, 1, 1)
    longitudinal_tenth = axis_eigenvalue("exact", xbc, length, 1, 10)
    transverse_gap = transverse_threshold / longitudinal_tenth

    finest = resolutions[-1]
    residuals = []
    for method in ("fv", "fem"):
        for row in numerical[method][finest][:10]:
            residuals.append(axis_residual(method, row["xbc"], length, finest, row["kx"]))
            residuals.append(axis_residual(method, row["ybc"], width, finest, row["ky"]))
    max_residual = float(max(residuals))

    if model == "kk_circle_periodic":
        multiplicity_ok = all(row["multiplicity"] == 2 and row["ky"] == 0 for row in first10)
    elif model in ("kk_interval_neumann", "kk_interval_dirichlet"):
        multiplicity_ok = all(row["multiplicity"] == 1 and row["ky"] == 0 for row in first10)
    else:
        multiplicity_ok = True

    thresholds = config["thresholds"]
    point_pass = all(
        (
            changes["fv"] < thresholds["max_richardson_relative_change_first10"],
            changes["fem"] < thresholds["max_richardson_relative_change_first10"],
            cross < thresholds["max_cross_method_relative_difference_first10"],
            max_residual < thresholds["max_algebraic_relative_residual"],
            fit["quadratic_relative_l2_residual"] < thresholds["max_quadratic_relative_l2_residual"],
            thresholds["free_exponent_interval"][0]
            <= fit["free_exponent"]
            <= thresholds["free_exponent_interval"][1],
            thresholds["effective_counting_dimension_interval"][0]
            <= fit["effective_counting_dimension"]
            <= thresholds["effective_counting_dimension_interval"][1],
            length_error < thresholds["max_control_length_relative_error"],
            transverse_gap >= thresholds["minimum_transverse_gap_ratio_to_longitudinal_mode10"],
            transverse_count <= thresholds["maximum_transverse_modes_among_first10"],
            multiplicity_ok,
        )
    )

    for rank, exact_row in enumerate(exact, start=1):
        spectra_rows.append(
            {
                "model": model,
                "t_abs": t_abs,
                "L": length,
                "rank": rank,
                "lambda_exact": exact_row["value"],
                "lambda_fv_fine": numerical["fv"][finest][rank - 1]["value"],
                "lambda_fem_fine": numerical["fem"][finest][rank - 1]["value"],
                "kx": exact_row["kx"],
                "ky": exact_row["ky"],
                "multiplicity": exact_row["multiplicity"],
            }
        )

    return {
        "model": model,
        "t_abs": t_abs,
        "L": length,
        "richardson_change_fv": changes["fv"],
        "richardson_change_fem": changes["fem"],
        "cross_method_difference": cross,
        "max_algebraic_residual": max_residual,
        **fit,
        "effective_length": effective_length,
        "length_relative_error": length_error,
        "transverse_gap_ratio": transverse_gap,
        "transverse_modes_first10": transverse_count,
        "multiplicity_ok": bool(multiplicity_ok),
        "point_pass": bool(point_pass),
        "first10_extrapolated": merged.tolist(),
    }


def dumbbell_point_metrics(t_abs: float, config: dict, spectra_rows: list[dict]):
    resolutions = config["resolutions"]["dumbbell_elements_or_cells"]
    numerical: dict[str, dict[int, dict]] = {"fv": {}, "fem": {}}
    for resolution in resolutions:
        numerical["fv"][resolution] = solve_dumbbell_fv(t_abs, resolution)
        numerical["fem"][resolution] = solve_dumbbell_fem(t_abs, resolution)

    extrapolated = {}
    changes = {}
    for method in numerical:
        arrays = {resolution: numerical[method][resolution]["values"] for resolution in resolutions}
        extrapolated[method], changes[method] = richardson_metrics(arrays)
    merged = 0.5 * (extrapolated["fv"] + extrapolated["fem"])
    cross = float(
        np.max(
            np.abs(extrapolated["fv"] - extrapolated["fem"])
            / np.maximum(np.abs(merged), 1e-30)
        )
    )
    fit = fit_spectrum(merged)
    fine = resolutions[-1]
    isolation = float(merged[1] / merged[0])
    neck_fraction = 0.5 * (
        numerical["fv"][fine]["neck_energy_fraction"]
        + numerical["fem"][fine]["neck_energy_fraction"]
    )
    max_residual = max(
        numerical["fv"][fine]["max_residual_first10"],
        numerical["fem"][fine]["max_residual_first10"],
    )
    thresholds = config["thresholds"]
    quadratic_packet = all(
        (
            fit["quadratic_relative_l2_residual"] < thresholds["max_quadratic_relative_l2_residual"],
            thresholds["free_exponent_interval"][0]
            <= fit["free_exponent"]
            <= thresholds["free_exponent_interval"][1],
            thresholds["effective_counting_dimension_interval"][0]
            <= fit["effective_counting_dimension"]
            <= thresholds["effective_counting_dimension_interval"][1],
        )
    )
    tunneling_flag = all(
        (
            isolation >= thresholds["tunneling_isolation_ratio_lambda2_over_lambda1"],
            neck_fraction >= thresholds["minimum_neck_gradient_energy_fraction"],
            not quadratic_packet,
        )
    )
    for rank in range(30):
        spectra_rows.append(
            {
                "model": "cheeger_tunneling",
                "t_abs": t_abs,
                "L": 4.0,
                "rank": rank + 1,
                "lambda_exact": "",
                "lambda_fv_fine": numerical["fv"][fine]["values"][rank],
                "lambda_fem_fine": numerical["fem"][fine]["values"][rank],
                "kx": "",
                "ky": "",
                "multiplicity": 1,
            }
        )
    metrics = {
        "model": "cheeger_tunneling",
        "t_abs": t_abs,
        "L": 4.0,
        "richardson_change_fv": changes["fv"],
        "richardson_change_fem": changes["fem"],
        "cross_method_difference": cross,
        "max_algebraic_residual": max_residual,
        **fit,
        "isolation_ratio_lambda2_over_lambda1": isolation,
        "neck_gradient_energy_fraction": float(neck_fraction),
        "quadratic_packet": bool(quadratic_packet),
        "tunneling_flag": bool(tunneling_flag),
        "first10_extrapolated": merged.tolist(),
    }
    profile = numerical["fem"][fine]
    return metrics, profile


def write_csv(path: Path, rows: list[dict]) -> None:
    require(bool(rows), f"no rows for {path.name}")
    fieldnames = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def make_figure(product_metrics: list[dict], dumbbell_metrics: list[dict], selected_profile: dict) -> None:
    figure, axes = plt.subplots(2, 2, figsize=(12, 9), constrained_layout=True)
    representative_t = 1e-3
    labels = {
        "kk_interval_neumann": "intervalle N",
        "kk_interval_dirichlet": "intervalle D",
        "kk_circle_periodic": "cercle",
        "transverse_contaminated": "transverse",
    }
    for row in product_metrics:
        if row["t_abs"] == representative_t:
            values = np.asarray(row["first10_extrapolated"])
            axes[0, 0].plot(np.arange(1, 11), values / values[0], "o-", label=labels[row["model"]])
    dumb = next(row for row in dumbbell_metrics if row["t_abs"] == representative_t)
    values = np.asarray(dumb["first10_extrapolated"])
    axes[0, 0].plot(np.arange(1, 11), values / values[0], "o-", label="haltère")
    axes[0, 0].set_yscale("log")
    axes[0, 0].set_xlabel("rang spectral")
    axes[0, 0].set_ylabel(r"$\lambda_n/\lambda_1$")
    axes[0, 0].set_title("Forme des dix premiers niveaux")
    axes[0, 0].legend(fontsize=8)

    for model in ("kk_interval_neumann", "kk_interval_dirichlet", "kk_circle_periodic"):
        rows = [row for row in product_metrics if row["model"] == model]
        axes[0, 1].plot(
            [row["L"] for row in rows],
            [row["effective_length"] / row["L"] for row in rows],
            "o-",
            label=labels[model],
        )
    axes[0, 1].axhline(1.0, color="black", linewidth=1)
    axes[0, 1].axhspan(0.95, 1.05, color="green", alpha=0.12)
    axes[0, 1].set_xlabel("longueur analytique L")
    axes[0, 1].set_ylabel(r"$L_{eff}/L$")
    axes[0, 1].set_title("Récupération de la longueur")
    axes[0, 1].legend(fontsize=8)

    axes[1, 0].loglog(
        [row["t_abs"] for row in dumbbell_metrics],
        [row["first10_extrapolated"][0] for row in dumbbell_metrics],
        "o-",
        label=r"$\lambda_1$",
    )
    axes[1, 0].loglog(
        [row["t_abs"] for row in dumbbell_metrics],
        [row["first10_extrapolated"][1] for row in dumbbell_metrics],
        "o-",
        label=r"$\lambda_2$",
    )
    axes[1, 0].invert_xaxis()
    axes[1, 0].set_xlabel(r"aire du col $|t|$")
    axes[1, 0].set_ylabel("valeur propre")
    axes[1, 0].set_title("Petit mode isolé de l'haltère")
    axes[1, 0].legend()

    x = np.asarray(selected_profile["x"])
    u = np.asarray(selected_profile["u1"])
    axes[1, 1].plot(x, u, label="premier mode haltère")
    axes[1, 1].axvspan(-0.75, 0.75, color="orange", alpha=0.15, label="région du col")
    axes[1, 1].set_xlabel("x")
    axes[1, 1].set_ylabel("fonction propre normalisée")
    axes[1, 1].set_title(r"Profil à $|t|=10^{-3}$")
    axes[1, 1].legend(fontsize=8)

    figure.suptitle("R65 — pilote spectral préenregistré", fontsize=15)
    figure.savefig(ROOT / "R65_SPECTRAL_DIAGNOSTICS.png", dpi=180)
    plt.close(figure)


def main() -> None:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    require(config["schema"] == "ddf-r65-preregistered-spectral-pilot-v1", "wrong config schema")
    require(config["smoothing_parameters_abs_t"] == [0.1, 0.01, 0.001, 0.0001, 0.00001], "t grid changed")
    require(config["resolutions"]["product_cells_per_unit"] == [12, 24, 48], "product grids changed")
    require(config["resolutions"]["dumbbell_elements_or_cells"] == [200, 400, 800], "dumbbell grids changed")

    spectra_rows: list[dict] = []
    product_metrics: list[dict] = []
    positive_models = ["kk_interval_neumann", "kk_interval_dirichlet", "kk_circle_periodic"]
    all_product_models = positive_models + ["transverse_contaminated"]
    for model in all_product_models:
        for t_abs in config["smoothing_parameters_abs_t"]:
            product_metrics.append(positive_point_metrics(model, t_abs, config, spectra_rows))

    dumbbell_metrics: list[dict] = []
    selected_profile = None
    profile_rows = []
    for t_abs in config["smoothing_parameters_abs_t"]:
        metrics, profile = dumbbell_point_metrics(t_abs, config, spectra_rows)
        dumbbell_metrics.append(metrics)
        if t_abs == 1e-3:
            selected_profile = profile
            for x, u in zip(profile["x"], profile["u1"]):
                profile_rows.append({"model": "cheeger_tunneling", "t_abs": t_abs, "x": x, "u1": u})

    require(selected_profile is not None, "registered profile missing")
    thresholds = config["thresholds"]
    positive_control_pass = {
        model: all(row["point_pass"] for row in product_metrics if row["model"] == model)
        for model in positive_models
    }
    transverse_points = [row for row in product_metrics if row["model"] == "transverse_contaminated"]
    transverse_rejection_count = sum(
        row["transverse_modes_first10"] > 0
        and row["transverse_gap_ratio"] < thresholds["minimum_transverse_gap_ratio_to_longitudinal_mode10"]
        for row in transverse_points
    )
    transverse_rejected = (
        transverse_rejection_count >= thresholds["minimum_parameter_points_for_false_positive_class"]
    )
    tunneling_count = sum(row["tunneling_flag"] for row in dumbbell_metrics)
    tunneling_rejected = tunneling_count >= thresholds["minimum_parameter_points_for_false_positive_class"]
    global_pass = all(positive_control_pass.values()) and transverse_rejected and tunneling_rejected

    metrics_rows = []
    for row in product_metrics + dumbbell_metrics:
        metrics_rows.append({key: value for key, value in row.items() if key != "first10_extrapolated"})
    write_csv(ROOT / "R65_SPECTRA.csv", spectra_rows)
    write_csv(ROOT / "R65_METRICS.csv", metrics_rows)
    write_csv(ROOT / "R65_PROFILES.csv", profile_rows)
    make_figure(product_metrics, dumbbell_metrics, selected_profile)

    results = {
        "schema": "ddf-r65-spectral-results-v1",
        "config_sha256": sha256(CONFIG_PATH),
        "preregistration_sha256": sha256(PREREG_PATH),
        "dimensionless_only": True,
        "spin2_not_computed": True,
        "ddf_geometry_not_tested": True,
        "positive_control_pass": positive_control_pass,
        "transverse_rejection_count": transverse_rejection_count,
        "transverse_rejected": bool(transverse_rejected),
        "tunneling_rejection_count": tunneling_count,
        "tunneling_rejected": bool(tunneling_rejected),
        "global_gate": "GO_PIPELINE" if global_pass else "STOP_PIPELINE",
        "product_metrics": product_metrics,
        "dumbbell_metrics": dumbbell_metrics,
        "next_round_if_go": "R66_REAL_GEOMETRY_SCALAR_THEN_SPIN2_OPERATOR",
    }
    (ROOT / "R65_RESULTS.json").write_text(
        json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print("R65 PREREGISTERED SPECTRAL PILOT")
    print("config sha256:", results["config_sha256"])
    print("preregistration sha256:", results["preregistration_sha256"])
    for model in positive_models:
        rows = [row for row in product_metrics if row["model"] == model]
        print(
            model,
            "PASS" if positive_control_pass[model] else "FAIL",
            "max_length_error",
            f"{max(row['length_relative_error'] for row in rows):.6e}",
            "max_fit_residual",
            f"{max(row['quadratic_relative_l2_residual'] for row in rows):.6e}",
            "p_range",
            f"[{min(row['free_exponent'] for row in rows):.6f},{max(row['free_exponent'] for row in rows):.6f}]",
        )
    print(
        "transverse_contaminated",
        "REJECTED" if transverse_rejected else "MISCLASSIFIED",
        "registered_points",
        transverse_rejection_count,
    )
    print(
        "cheeger_tunneling",
        "REJECTED" if tunneling_rejected else "MISCLASSIFIED",
        "registered_points",
        tunneling_count,
        "isolation_range",
        f"[{min(row['isolation_ratio_lambda2_over_lambda1'] for row in dumbbell_metrics):.3e},"
        f"{max(row['isolation_ratio_lambda2_over_lambda1'] for row in dumbbell_metrics):.3e}]",
    )
    print("FINAL VERDICT")
    print("R65_SPECTRAL_PIPELINE:", "GO" if global_pass else "STOP")
    print("ONE_DIMENSIONAL_KK_CONTROLS: RECOGNIZED" if all(positive_control_pass.values()) else "ONE_DIMENSIONAL_KK_CONTROLS: FAILED")
    print("CHEEGER_TUNNELING_FALSE_POSITIVE: REJECTED" if tunneling_rejected else "CHEEGER_TUNNELING_FALSE_POSITIVE: NOT_REJECTED")
    print("TRANSVERSE_FALSE_POSITIVE: REJECTED" if transverse_rejected else "TRANSVERSE_FALSE_POSITIVE: NOT_REJECTED")
    print("DDF_METRIC_OR_SPIN2_SPECTRUM: NOT_TESTED")
    print("R_MICRONS: NOT_DERIVED")


if __name__ == "__main__":
    main()

