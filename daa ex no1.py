import time
import random
import sys


def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm
    Time Complexity: O(log log n) average, O(n) worst case
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        # Prevent division by zero
        if arr[high] == arr[low]:
            break

        # Interpolation formula
        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    """
    Binary Search Algorithm
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    """
    Compare the performance of Interpolation Search
    and Binary Search on arrays of different sizes.
    """
    sizes = [1000, 5000, 10000, 50000, 100000]

    print(
        f"{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} "
        f"{'IS Comparisons':>16} {'BS Comparisons':>16}"
    )
    print("-" * 75)

    for size in sizes:
        # Generate sorted unique array
        arr = sorted(random.sample(range(size * 10), size))

        # Select a random target from the array
        target = arr[random.randint(0, size - 1)]

        # Interpolation Search timing (average of 100 runs)
        start = time.perf_counter()
        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        # Binary Search timing (average of 100 runs)
        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(
            f"{size:>10} "
            f"{is_time:>14.6f} "
            f"{bs_time:>14.6f} "
            f"{comp_is:>16} "
            f"{comp_bs:>16}"
        )


# ---------------- Main Program ----------------

if __name__ == "__main__":

    # Sample array
    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    target = 35

    # Interpolation Search Example
    idx, comps = interpolation_search(arr, target)

    print("Interpolation Search Example")
    print("----------------------------")
    print(f"Array: {arr}")
    print(f"Searching for: {target}")

    if idx != -1:
        print(f"Element found at index: {idx}")
    else:
        print("Element not found")

    print(f"Comparisons: {comps}")
    print()

    # Performance Analysis
    print("Performance Analysis")
    print("====================")
    performance_analysis()