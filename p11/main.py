from pathlib import Path
import math

grid = [
    [int(num) for num in line.split()]
    for line in (Path(__file__).parent / "grid.txt").read_text().splitlines()
]

GRID_HEIGHT, GRID_WIDTH = len(grid), len(grid[0])

# horizontal rows
s1 = max(
    [
        math.prod(grid[row_ix][col_ix : col_ix + 4])
        for row_ix in range(GRID_HEIGHT)
        for col_ix in range(GRID_WIDTH - 3)
    ]
)

# vertical columns
s2 = max(
    [
        math.prod(
            [
                grid[row_ix][col_ix],
                grid[row_ix + 1][col_ix],
                grid[row_ix + 2][col_ix],
                grid[row_ix + 3][col_ix],
            ]
        )
        for row_ix in range(GRID_HEIGHT - 3)
        for col_ix in range(GRID_WIDTH)
    ]
)

# diagonal \
s3 = max(
    [
        math.prod(
            [
                grid[row_ix][col_ix],
                grid[row_ix + 1][col_ix + 1],
                grid[row_ix + 2][col_ix + 2],
                grid[row_ix + 3][col_ix + 3],
            ]
        )
        for row_ix in range(GRID_HEIGHT - 3)
        for col_ix in range(GRID_WIDTH - 3)
    ]
)

# diagonal /

s4 = max(
    [
        math.prod(
            [
                grid[row_ix][col_ix],
                grid[row_ix + 1][col_ix - 1],
                grid[row_ix + 2][col_ix - 2],
                grid[row_ix + 3][col_ix - 3],
            ]
        )
        for row_ix in range(GRID_HEIGHT - 3)
        for col_ix in range(3, GRID_WIDTH)
    ]
)

print(max(s1,s2,s3,s4))
