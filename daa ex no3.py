import heapq


# ============================================================
# UNION-FIND DATA STRUCTURE FOR KRUSKAL'S ALGORITHM
# ============================================================

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        # If both vertices are already in the same set,
        # adding this edge would create a cycle.
        if rx == ry:
            return False

        # Union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True


# ============================================================
# KRUSKAL'S ALGORITHM
# ============================================================

def kruskal(n, edges):
    """
    Kruskal's Algorithm for Minimum Spanning Tree.

    edges: list of (weight, u, v)

    Time Complexity: O(E log E)
    Space Complexity: O(V)
    """

    # Sort edges according to weight
    edges.sort()

    uf = UnionFind(n)
    mst = []
    cost = 0

    for w, u, v in edges:

        # Add edge only if it does not create a cycle
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w

            # MST contains exactly n - 1 edges
            if len(mst) == n - 1:
                break

    return mst, cost


# ============================================================
# PRIM'S ALGORITHM
# ============================================================

def prim(n, adj, start=0):
    """
    Prim's Algorithm for Minimum Spanning Tree.

    adj: adjacency list {u: [(v, weight), ...]}

    Time Complexity: O(E log V)
    Space Complexity: O(V + E)
    """

    INF = float('inf')

    # Minimum weight required to connect each vertex
    key = [INF] * n

    # Stores the parent of each vertex
    parent = [-1] * n

    # Checks whether a vertex is already in MST
    inMST = [False] * n

    # Start from the given vertex
    key[start] = 0

    # Min-heap
    pq = [(0, start)]

    mst = []
    cost = 0

    while pq:

        w, u = heapq.heappop(pq)

        # Skip if vertex is already included
        if inMST[u]:
            continue

        inMST[u] = True

        # Add edge connecting this vertex to MST
        if parent[u] != -1:
            mst.append((parent[u], u, w))
            cost += w

        # Check all neighbouring vertices
        for v, wt in adj.get(u, []):

            if not inMST[v] and wt < key[v]:

                key[v] = wt
                parent[v] = u

                heapq.heappush(pq, (wt, v))

    return mst, cost


# ============================================================
# GRAPH DEFINITION
# ============================================================

n = 7

edges = [
    (7, 0, 1),
    (5, 0, 3),
    (8, 1, 2),
    (9, 1, 3),
    (7, 1, 4),
    (5, 2, 4),
    (15, 3, 4),
    (6, 3, 5),
    (8, 4, 5),
    (9, 4, 6),
    (11, 5, 6)
]


# ============================================================
# CREATE ADJACENCY LIST FOR PRIM'S ALGORITHM
# ============================================================

adj = {}

for w, u, v in edges:
    adj.setdefault(u, []).append((v, w))
    adj.setdefault(v, []).append((u, w))


# ============================================================
# RUN KRUSKAL'S ALGORITHM
# ============================================================

k_mst, k_cost = kruskal(n, edges[:])


# ============================================================
# RUN PRIM'S ALGORITHM
# ============================================================

p_mst, p_cost = prim(n, adj)


# ============================================================
# DISPLAY KRUSKAL'S RESULT
# ============================================================

print("=== Kruskal's MST ===")

for u, v, w in k_mst:
    print(f"Edge ({u} - {v})  Weight: {w}")

print(f"Total MST Cost: {k_cost}")


# ============================================================
# DISPLAY PRIM'S RESULT
# ============================================================

print("\n=== Prim's MST ===")

for u, v, w in p_mst:
    print(f"Edge ({u} - {v})  Weight: {w}")

print(f"Total MST Cost: {p_cost}")


# ============================================================
# COMPARISON
# ============================================================

print("\n=== Comparison ===")

if k_cost == p_cost:
    print("Both algorithms produce the same minimum cost.")
else:
    print("The MST costs are different.")