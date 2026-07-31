import time
import random


# ---------------- Naive String Search ----------------
def naive_search(text, pattern):
    n, m = len(text), len(pattern)

    if m == 0:
        return [], 0

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


# ---------------- KMP LPS Calculation ----------------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


# ---------------- KMP Search ----------------
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)

    if m == 0:
        return [], 0

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:

        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


# ---------------- Rabin-Karp Search ----------------
def rabin_karp(text, pattern, q=101):

    n, m = len(text), len(pattern)

    if m == 0 or m > n:
        return [], 0

    d = 256
    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0

    matches = []
    comparisons = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for s in range(n - m + 1):

        if p_hash == t_hash:

            for j in range(m):
                comparisons += 1

                if text[s + j] != pattern[j]:
                    break

            else:
                matches.append(s)

        if s < n - m:
            t_hash = (
                d * (t_hash - ord(text[s]) * h)
                + ord(text[s + m])
            ) % q

    return matches, comparisons


# ---------------- Algorithm Comparison ----------------
def compare_algorithms(text, pattern):

    algorithms = [
        ("Naive", naive_search),
        ("KMP", kmp_search),
        ("Rabin-Karp", rabin_karp)
    ]

    print("\nAlgorithm Comparison")
    print("=" * 75)
    print(f"{'Algorithm':<15}{'Matches':<25}"
          f"{'Comparisons':<15}{'Time(ms)':<10}")
    print("-" * 75)

    for name, algorithm in algorithms:

        start = time.perf_counter()

        matches, comparisons = algorithm(text, pattern)

        end = time.perf_counter()

        execution_time = (end - start) * 1000

        print(
            f"{name:<15}"
            f"{str(matches):<25}"
            f"{comparisons:<15}"
            f"{execution_time:.5f}"
        )


# ---------------- Performance Testing ----------------
def performance_test():

    text = ''.join(random.choices("ABCD", k=20000))

    patterns = [
        "AB",
        "ABCD",
        "ABCDAB",
        "ABCDABCD"
    ]

    print("\nLarge Text Performance Test")
    print("=" * 60)

    for pattern in patterns:

        print(f"\nPattern: {pattern}")

        for name, algorithm in [
            ("Naive", naive_search),
            ("KMP", kmp_search),
            ("Rabin-Karp", rabin_karp)
        ]:

            start = time.perf_counter()

            _, comparisons = algorithm(text, pattern)

            end = time.perf_counter()

            print(
                f"{name:<12} "
                f"Comparisons: {comparisons:<10} "
                f"Time: {(end-start)*1000:.5f} ms"
            )


# ---------------- Main Program ----------------
def main():

    print("=" * 60)
    print(" STRING MATCHING ALGORITHM ANALYZER ")
    print("=" * 60)

    text = input("\nEnter text: ")
    pattern = input("Enter pattern: ")

    compare_algorithms(text, pattern)

    choice = input(
        "\nRun large performance test? (y/n): "
    )

    if choice.lower() == "y":
        performance_test()


if __name__ == "__main__":
    main()