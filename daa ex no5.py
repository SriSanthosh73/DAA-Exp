import random


# ============================================================
# GLOBAL COMPARISON COUNTER
# ============================================================

comparison_count = 0


# ============================================================
# DIVIDE AND CONQUER MIN-MAX
# ============================================================

def min_max_dc(arr, low, high):
    global comparison_count

    # Base case: single element
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]

        return arr[high], arr[low]

    # --------------------------------------------------------
    # Divide
    # --------------------------------------------------------

    mid = (low + high) // 2

    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    # --------------------------------------------------------
    # Conquer / Combine
    # --------------------------------------------------------

    # Compare minimum values
    comparison_count += 1

    if lmin < rmin:
        overall_min = lmin
    else:
        overall_min = rmin

    # Compare maximum values
    comparison_count += 1

    if lmax > rmax:
        overall_max = lmax
    else:
        overall_max = rmax

    return overall_min, overall_max


# ============================================================
# NAIVE MIN-MAX METHOD
# ============================================================

def min_max_naive(arr):

    mn = arr[0]
    mx = arr[0]
    comps = 0

    for x in arr[1:]:

        # Compare for minimum
        comps += 1

        if x < mn:
            mn = x

        # Compare for maximum
        comps += 1

        if x > mx:
            mx = x

    return mn, mx, comps


# ============================================================
# DEMONSTRATION ON SMALL ARRAY
# ============================================================

arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

comparison_count = 0

mn, mx = min_max_dc(
    arr,
    0,
    len(arr) - 1
)

dc_comps = comparison_count

_, _, naive_comps = min_max_naive(arr)


print("=== Small Array Demonstration ===")

print(f"Array: {arr}")
print(f"Min: {mn}")
print(f"Max: {mx}")
print(f"D&C Comparisons: {dc_comps}")
print(f"Naive Comparisons: {naive_comps}")


# ============================================================
# PERFORMANCE ANALYSIS
# ============================================================

print(
    f'\n{"Size":>8} '
    f'{"DC Comps":>12} '
    f'{"Naive Comps":>14} '
    f'{"Formula 3n/2-2":>16}'
)

print("-" * 56)


for size in [10, 100, 1000, 10000]:

    # Generate random array
    arr = [
        random.randint(1, 10000)
        for _ in range(size)
    ]

    # Divide and Conquer
    comparison_count = 0

    mn, mx = min_max_dc(
        arr,
        0,
        len(arr) - 1
    )

    dc = comparison_count

    # Naive method
    _, _, naive = min_max_naive(arr)

    # Theoretical formula
    formula = (3 * size // 2) - 2

    print(
        f"{size:>8} "
        f"{dc:>12} "
        f"{naive:>14} "
        f"{formula:>16}"
    )