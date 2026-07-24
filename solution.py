def generate_shape(n: int, shape: str) -> list[list[int]]:
    """
    Generates an n x n grid for the given shape.

    Args:
        n     : Grid size (5 <= n <= 51, odd for diamond)
        shape : "checkerboard" or "diamond"

    Returns:
        2D list of 0s and 1s.
    """
    grid = [[0] * n for _ in range(n)]

    if shape == "checkerboard":
        for i in range(n):
            for j in range(n):
                # Cell is filled when (row + col) is odd
                # top-left [0,0]: 0+0=0 -> 0 (empty), as required
                grid[i][j] = (i + j) % 2

    elif shape == "diamond":
        mid = n // 2  # centre row and column index
        for i in range(n):
            for j in range(n):
                # Manhattan distance from centre must be <= mid
                if abs(i - mid) + abs(j - mid) <= mid:
                    grid[i][j] = 1

    return grid


def print_grid(grid: list[list[int]]) -> None:
    """Prints the grid in the required output format."""
    for row in grid:
        print(" ".join(map(str, row)))


# -- Entry point -------------------------------------------------------------
if __name__ == "__main__":
    # Read n and shape from standard input
    n = int(input())
    shape = input().strip()
    result = generate_shape(n, shape)
    print_grid(result)