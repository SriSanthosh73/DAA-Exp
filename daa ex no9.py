def first_fit(items, capacity=1.0):
    bins = []          # Remaining space in each bin
    bin_contents = []  # Items stored in each bin

    for item in items:
        placed = False

        for i, space in enumerate(bins):
            if space >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True
                break

        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def first_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, capacity)


def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)

    bins = []
    bin_contents = []

    for item in sorted_items:
        best_idx = -1
        best_space = float('inf')

        for i, space in enumerate(bins):
            if space >= item and space - item < best_space:
                best_space = space - item
                best_idx = i

        if best_idx >= 0:
            bins[best_idx] -= item
            bin_contents[best_idx].append(item)
        else:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


def display_bins(label, bins):
    print(f"\n{label}: {len(bins)} bins")

    for i, b in enumerate(bins, 1):
        used = sum(b)
        bar = '#' * int(used * 20)

        print(
            f"  Bin {i}: {[round(x, 1) for x in b]} "
            f"| Used: {used:.1f} "
            f"[{bar:<20}]"
        )


# Input items
items = [0.5, 0.7, 0.3, 0.9, 0.2,
         0.6, 0.8, 0.4, 0.1, 0.5]

capacity = 1.0

# Lower bound = ceiling(total size / bin capacity)
lower_bound = -(-sum(items) // capacity)

print(f"Items: {items}")
print(f"Capacity: {capacity}")
print(f"Sum of items: {sum(items)}")
print(f"Lower bound on bins: {int(lower_bound)}")


# Apply algorithms
ff_bins = first_fit(items, capacity)
ffd_bins = first_fit_decreasing(items, capacity)
bfd_bins = best_fit_decreasing(items, capacity)


# Display results
display_bins("First Fit (FF)", ff_bins)
display_bins("First Fit Decreasing (FFD)", ffd_bins)
display_bins("Best Fit Decreasing (BFD)", bfd_bins)
