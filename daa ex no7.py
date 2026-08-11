# ============================================================
# N-QUEENS PROBLEM USING BACKTRACKING
# ============================================================


# ============================================================
# CHECK WHETHER A QUEEN CAN BE PLACED SAFELY
# ============================================================

def is_safe(board, row, col):

    # Check all previously placed queens
    for prev_row in range(row):

        placed = board[prev_row]

        # Same column
        if placed == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed - col):
            return False

    return True


# ============================================================
# SOLVE N-QUEENS USING BACKTRACKING
# ============================================================

def solve_n_queens(n):

    # board[row] = column where the queen is placed
    board = [-1] * n

    # Store all solutions
    solutions = []

    # Count number of backtracking steps
    backtrack_count = [0]

    def backtrack(row):

        # All queens have been placed
        if row == n:
            solutions.append(board[:])
            return

        # Try every column in the current row
        for col in range(n):

            # Check whether this position is safe
            if is_safe(board, row, col):

                # Place queen
                board[row] = col

                # Move to next row
                backtrack(row + 1)

                # Remove queen (backtrack)
                board[row] = -1

                # Count backtracking operation
                backtrack_count[0] += 1

    # Start from row 0
    backtrack(0)

    return solutions, backtrack_count[0]


# ============================================================
# DISPLAY CHESS BOARD
# ============================================================

def display_board(solution, n):

    print("  +" + "---+" * n)

    for row in range(n):

        print("  |", end="")

        for col in range(n):

            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()

        print("  +" + "---+" * n)


# ============================================================
# MAIN PROGRAM
# ============================================================

# Solve N-Queens for 4, 6 and 8
for n in [4, 6, 8]:

    solutions, backtracks = solve_n_queens(n)

    print(
        f"N={n}: "
        f"{len(solutions)} solutions, "
        f"{backtracks} backtracks"
    )

    # Show all solutions only for N=4
    if n == 4:

        print(f"\nAll solutions for {n}-Queens:")

        for i, sol in enumerate(solutions, 1):

            print(f"\nSolution {i}: {sol}")

            display_board(sol, n)