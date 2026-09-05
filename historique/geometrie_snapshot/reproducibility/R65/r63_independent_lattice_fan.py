#!/usr/bin/env python3
"""Independent R63 audit of the R62 lattice and relative fan certificate.

This program deliberately does not import the R62 code and does not use
SymPy for exact linear algebra.  Determinants, ranks, rational solves and
polyhedron vertices are recomputed with Python integers/Fractions.  A second,
numerical cross-check of the completed polytope uses SciPy/Qhull.

What is certified:

* Q V^T = 0, rank(Q)=6 and saturation of the Cox relations;
* unimodularity of all 28 relative maximal cones;
* exact coherence from the support vector h;
* the 20 boundary facets, the relative support and the 48-cone completion;
* completeness/smoothness of the completed normal fan;
* the relative Stanley--Reisner minimal non-faces.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd


# Coordinate order: x0,...,x7,E,p,m.  These constants are copied from the
# mathematical statement of R62, not imported from its implementation.
RAYS = (
    (1, 0, 0, 0, 0),
    (-2, 0, -1, 0, 0),
    (-2, 0, 0, -1, 0),
    (0, 0, 0, 1, 0),
    (0, 0, 1, 0, 0),
    (-1, -1, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (-1, 0, 0, 0, 0),
    (1, 1, 0, 0, 0),
    (0, -1, 0, 0, 1),
    (0, 0, 0, 0, 1),
)

Q = (
    (2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    (2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0),
    (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    (-1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, -1, 0, 1, 0, 1, -1),
)

CONES = (
    (0, 1, 2, 5, 9), (0, 1, 3, 5, 9),
    (0, 2, 4, 5, 9), (0, 3, 4, 5, 9),
    (1, 2, 5, 7, 9), (1, 3, 5, 7, 9),
    (2, 4, 5, 7, 9), (3, 4, 5, 7, 9),
    (0, 1, 2, 8, 10), (0, 1, 3, 8, 10),
    (0, 2, 4, 8, 10), (0, 3, 4, 8, 10),
    (1, 2, 6, 7, 10), (1, 2, 6, 8, 10),
    (1, 3, 6, 7, 10), (1, 3, 6, 8, 10),
    (2, 4, 6, 7, 10), (2, 4, 6, 8, 10),
    (3, 4, 6, 7, 10), (3, 4, 6, 8, 10),
    (0, 1, 2, 9, 10), (0, 1, 3, 9, 10),
    (0, 2, 4, 9, 10), (0, 3, 4, 9, 10),
    (1, 2, 7, 9, 10), (1, 3, 7, 9, 10),
    (2, 4, 7, 9, 10), (3, 4, 7, 9, 10),
)

HEIGHTS = (0, 0, 0, 5, 5, 0, 5, 2, 4, 0, 3)
INFINITY_RAY = (0, 0, 0, 0, -1)
INFINITY_HEIGHT = 1


def dot(left, right):
    return sum(a * b for a, b in zip(left, right, strict=True))


def transpose(matrix):
    return tuple(zip(*matrix, strict=True))


def matmul(left, right):
    right_t = transpose(right)
    return tuple(tuple(dot(row, col) for col in right_t) for row in left)


def det_bareiss(matrix):
    """Fraction-free exact determinant, independent of a CAS package."""
    work = [list(map(int, row)) for row in matrix]
    n = len(work)
    assert all(len(row) == n for row in work)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for column in range(n - 1):
        pivot_row = next(
            (row for row in range(column, n) if work[row][column] != 0),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign *= -1
        pivot = work[column][column]
        for row in range(column + 1, n):
            for col in range(column + 1, n):
                numerator = work[row][col] * pivot - work[row][column] * work[column][col]
                assert numerator % previous == 0
                work[row][col] = numerator // previous
            work[row][column] = 0
        previous = pivot
    return sign * work[-1][-1]


def rational_solve(matrix, rhs):
    """Exact Gauss--Jordan solve over Q; None means singular."""
    n = len(matrix)
    work = [
        [Fraction(value) for value in row] + [Fraction(target)]
        for row, target in zip(matrix, rhs, strict=True)
    ]
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if work[row][column]),
            None,
        )
        if pivot is None:
            return None
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        work[column] = [entry / pivot_value for entry in work[column]]
        for row in range(n):
            if row == column:
                continue
            factor = work[row][column]
            if factor:
                work[row] = [
                    a - factor * b
                    for a, b in zip(work[row], work[column], strict=True)
                ]
    return tuple(work[row][-1] for row in range(n))


def enumerate_vertices(rays, heights):
    """Enumerate every vertex of {y : <y,v_i> <= h_i} exactly."""
    dimension = len(rays[0])
    vertices = {}
    for candidate in combinations(range(len(rays)), dimension):
        solution = rational_solve(
            tuple(rays[index] for index in candidate),
            tuple(heights[index] for index in candidate),
        )
        if solution is None:
            continue
        values = tuple(dot(solution, ray) for ray in rays)
        if not all(value <= height for value, height in zip(values, heights, strict=True)):
            continue
        active = tuple(
            index
            for index, (value, height) in enumerate(zip(values, heights, strict=True))
            if value == height
        )
        vertices[solution] = active
    return vertices


def codimension_one_faces(cones):
    faces = Counter()
    for cone in cones:
        for removed in cone:
            faces[tuple(index for index in cone if index != removed)] += 1
    return faces


def minimal_nonfaces(number_of_rays, cones):
    cone_sets = tuple(frozenset(cone) for cone in cones)

    def is_face(candidate):
        frozen = frozenset(candidate)
        return any(frozen <= cone for cone in cone_sets)

    answer = []
    for size in range(1, number_of_rays + 1):
        for candidate in combinations(range(number_of_rays), size):
            if is_face(candidate):
                continue
            if all(is_face(candidate[:i] + candidate[i + 1 :]) for i in range(size)):
                answer.append(candidate)
    return tuple(answer)


def qhull_cross_check(rays, heights, exact_vertices):
    """Independent floating-point vertex enumeration using Qhull."""
    import numpy as np
    from scipy.optimize import linprog
    from scipy.spatial import HalfspaceIntersection

    ray_array = np.asarray(rays, dtype=float)
    height_array = np.asarray(heights, dtype=float)
    norms = np.linalg.norm(ray_array, axis=1)

    # Chebyshev centre: maximize the distance r to all supporting planes.
    inequalities = np.hstack((ray_array, norms[:, None]))
    objective = np.r_[np.zeros(ray_array.shape[1]), -1.0]
    centre_result = linprog(
        objective,
        A_ub=inequalities,
        b_ub=height_array,
        bounds=[(None, None)] * ray_array.shape[1] + [(0.0, None)],
        method="highs",
    )
    assert centre_result.success and centre_result.x[-1] > 0.9
    centre = centre_result.x[:-1]

    halfspaces = np.hstack((ray_array, -height_array[:, None]))
    intersections = HalfspaceIntersection(halfspaces, centre).intersections
    exact_array = np.asarray(
        [[float(value) for value in vertex] for vertex in exact_vertices],
        dtype=float,
    )
    assert len(intersections) == len(exact_array)
    max_nearest_error = max(
        min(np.linalg.norm(point - exact, ord=np.inf) for exact in exact_array)
        for point in intersections
    )
    assert max_nearest_error < 1.0e-8
    return centre_result.x[-1], max_nearest_error


def main():
    # Lattice/Cox audit.
    ray_matrix_t = transpose(RAYS)  # 5 x 11
    kernel_product = matmul(Q, transpose(ray_matrix_t))
    assert kernel_product == tuple((0, 0, 0, 0, 0) for _ in range(6))

    maximal_minors = []
    for columns in combinations(range(11), 6):
        minor = tuple(tuple(row[column] for column in columns) for row in Q)
        maximal_minors.append(det_bareiss(minor))
    nonzero_minors = tuple(value for value in maximal_minors if value)
    minors_gcd = 0
    for value in nonzero_minors:
        minors_gcd = gcd(minors_gcd, abs(value))
    # A nonzero 6x6 minor proves rank six.  gcd=1 proves the row lattice is
    # primitive, equivalently every Smith invariant is one.
    assert nonzero_minors and minors_gcd == 1

    determinants = tuple(det_bareiss(tuple(RAYS[i] for i in cone)) for cone in CONES)
    assert len(CONES) == 28 and set(map(abs, determinants)) == {1}

    vertices = enumerate_vertices(RAYS, HEIGHTS)
    assert len(vertices) == 28
    assert set(vertices.values()) == set(CONES)
    assert all(value.denominator == 1 for vertex in vertices for value in vertex)
    gaps = []
    for vertex, active in vertices.items():
        for index, (ray, height) in enumerate(zip(RAYS, HEIGHTS, strict=True)):
            if index not in active:
                gaps.append(Fraction(height) - dot(vertex, ray))
    assert set(gaps) == {1, 2, 3, 4, 5} and min(gaps) > 0

    walls = codimension_one_faces(CONES)
    wall_histogram = Counter(walls.values())
    assert wall_histogram == Counter({2: 60, 1: 20})
    boundary = tuple(sorted(face for face, count in walls.items() if count == 1))

    sr = minimal_nonfaces(11, CONES)
    expected_sr = (
        (0, 6), (0, 7), (1, 4), (2, 3), (5, 6),
        (5, 8), (5, 10), (6, 9), (7, 8), (8, 9),
    )
    assert sr == expected_sr

    # Add the normal at infinity.  Boundary cones are the old fourfold fan.
    completed_rays = RAYS + (INFINITY_RAY,)
    completed_heights = HEIGHTS + (INFINITY_HEIGHT,)
    completed_cones = CONES + tuple(face + (11,) for face in boundary)
    completed_vertices = enumerate_vertices(completed_rays, completed_heights)
    assert len(completed_vertices) == 48
    assert set(completed_vertices.values()) == set(completed_cones)
    completed_dets = tuple(
        det_bareiss(tuple(completed_rays[index] for index in cone))
        for cone in completed_cones
    )
    assert set(map(abs, completed_dets)) == {1}
    completed_walls = codimension_one_faces(completed_cones)
    assert len(completed_walls) == 120 and set(completed_walls.values()) == {2}

    # A strictly positive dependence proves that the completed rays positively
    # span N_R, so the completed support polytope is bounded.
    positive_weights = (5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2)
    weighted_sum = tuple(
        sum(weight * ray[coordinate] for weight, ray in zip(positive_weights, completed_rays, strict=True))
        for coordinate in range(5)
    )
    assert weighted_sum == (0, 0, 0, 0, 0) and min(positive_weights) > 0

    qhull_radius, qhull_error = qhull_cross_check(
        completed_rays, completed_heights, completed_vertices
    )

    # Base character e5*: only p and m have coefficient +1 in the relative
    # fan.  Hence div(z)=D_p+D_m, both with multiplicity one.
    base_orders = tuple(ray[-1] for ray in RAYS)
    assert base_orders == (0,) * 9 + (1, 1)

    print("R63 INDEPENDENT LATTICE/FAN AUDIT: PASS")
    print("Q kernel / rank / gcd maximal minors:", "zero", 6, minors_gcd)
    print("Q maximal minors: total/nonzero:", len(maximal_minors), len(nonzero_minors))
    print("relative cones / |det|:", len(CONES), sorted(set(map(abs, determinants))))
    print("exact support vertices / gaps:", len(vertices), sorted(set(gaps)))
    print("walls internal/boundary:", wall_histogram[2], wall_histogram[1])
    print("minimal SR generators:", sr)
    print("completion cones / paired walls:", len(completed_cones), len(completed_walls))
    print("positive spanning relation:", positive_weights)
    print("Qhull vertices / Chebyshev radius / max error:", len(completed_vertices), f"{qhull_radius:.12g}", f"{qhull_error:.3e}")
    print("base vanishing orders:", base_orders)
    print("VERDICT: SMOOTH COHERENT RELATIVE FAN AND SMOOTH COMPLETE COMPACTIFICATION CONFIRMED")


if __name__ == "__main__":
    main()

