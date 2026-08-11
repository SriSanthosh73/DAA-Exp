import heapq
from itertools import permutations


# ============================================================
# CONSTANT
# ============================================================

INF = float('inf')


# ============================================================
# MATRIX REDUCTION
# ============================================================

def reduce_matrix(mat):
    """
    Reduce the cost matrix and return the
    reduced matrix and reduction cost.
    """

    m = [row[:] for row in mat]
    n = len(m)
    cost = 0

    # -------------------------
    # Row Reduction
    # -------------------------

    for i in range(n):

        row_min = min(m[i])

        if row_min != INF and row_min != 0:

            cost += row_min

            m[i] = [
                x - row_min if x != INF else INF
                for x in m[i]
            ]

    # -------------------------
    # Column Reduction
    # -------------------------

    for j in range(n):

        col_min = min(
            m[i][j]
            for i in range(n)
        )

        if col_min != INF and col_min != 0:

            cost += col_min

            for i in range(n):

                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost


# ============================================================
# TSP BRUTE FORCE
# ============================================================

def tsp_brute_force(cost, n):
    """
    Brute-force solution for TSP.

    Time Complexity: O(n!)
    Space Complexity: O(n)
    """

    # Cities other than starting city 0
    cities = list(range(1, n))

    best_cost = INF
    best_path = None

    # Try every possible ordering
    for perm in permutations(cities):

        # Start at city 0 and return to city 0
        path = [0] + list(perm) + [0]

        # Calculate total cost
        current_cost = sum(
            cost[path[i]][path[i + 1]]
            for i in range(n)
        )

        # Update best solution
        if current_cost < best_cost:

            best_cost = current_cost
            best_path = path

    return best_path, best_cost


# ============================================================
# COST MATRIX
# ============================================================

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

n = 5

cities = ['A', 'B', 'C', 'D', 'E']


# ============================================================
# DISPLAY COST MATRIX
# ============================================================

print("=== 5-City TSP - Cost Matrix ===")

print(
    f'{"":>4}',
    ' '.join(f'{c:>5}' for c in cities)
)

for i, row in enumerate(cost):

    r = [
        'INF' if x == INF else str(x)
        for x in row
    ]

    print(
        f'{cities[i]:>4}',
        ' '.join(f'{v:>5}' for v in r)
    )


# ============================================================
# MATRIX REDUCTION
# ============================================================

reduced_matrix, reduction_cost = reduce_matrix(cost)

print("\n=== Reduced Cost Matrix ===")

print(
    f'{"":>4}',
    ' '.join(f'{c:>5}' for c in cities)
)

for i, row in enumerate(reduced_matrix):

    r = [
        'INF' if x == INF else str(x)
        for x in row
    ]

    print(
        f'{cities[i]:>4}',
        ' '.join(f'{v:>5}' for v in r)
    )

print(f"\nReduction Cost: {reduction_cost}")


# ============================================================
# FIND OPTIMAL TSP TOUR
# ============================================================

best_path, best_cost = tsp_brute_force(cost, n)


# ============================================================
# DISPLAY OPTIMAL TOUR
# ============================================================

print(
    f'\nOptimal Tour: '
    f'{" -> ".join(cities[i] for i in best_path)}'
)

print(f'Minimum Cost: {best_cost}')


# ============================================================
# PATH VERIFICATION
# ============================================================

print("\nPath verification:")

total = 0

for i in range(n):

    u = best_path[i]
    v = best_path[i + 1]

    edge_cost = cost[u][v]

    total += edge_cost

    print(
        f'  {cities[u]} -> {cities[v]}: '
        f'cost = {edge_cost}'
    )

print(f'  Total = {total}')