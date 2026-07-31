import time
import random


# ---------------- Interpolation Search ----------------
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            break

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


# ---------------- Binary Search ----------------
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
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


# ---------------- Performance Analysis ----------------
def performance_analysis():
    print("\nPerformance Comparison")
    print("=" * 75)

    sizes = [1000, 5000, 10000, 50000, 100000]

    print(f"{'Size':<10}{'IS Time(ms)':<15}{'BS Time(ms)':<15}"
          f"{'IS Comp':<15}{'BS Comp':<15}")
    print("-" * 75)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)

        start = time.perf_counter()
        for _ in range(100):
            _, is_comp = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        start = time.perf_counter()
        for _ in range(100):
            _, bs_comp = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:<10}{is_time:<15.6f}{bs_time:<15.6f}"
              f"{is_comp:<15}{bs_comp:<15}")


# ---------------- Main Program ----------------
def main():
    print("=" * 50)
    print(" SEARCH ALGORITHM COMPARISON ")
    print("=" * 50)

    arr = list(map(int, input("\nEnter sorted array elements: ").split()))
    target = int(input("Enter target element: "))

    print("\nInterpolation Search")
    print("-" * 25)
    idx1, comp1 = interpolation_search(arr, target)

    if idx1 != -1:
        print(f"Element found at index : {idx1}")
    else:
        print("Element not found.")

    print(f"Comparisons : {comp1}")

    print("\nBinary Search")
    print("-" * 25)
    idx2, comp2 = binary_search(arr, target)

    if idx2 != -1:
        print(f"Element found at index : {idx2}")
    else:
        print("Element not found.")

    print(f"Comparisons : {comp2}")

    performance_analysis()


if __name__ == "__main__":
    main()