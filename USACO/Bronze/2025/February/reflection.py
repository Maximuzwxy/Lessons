# =============================================================================
# USACO 2025 February Contest, Bronze
# Problem 1. Reflection
# https://usaco.org/index.php?page=viewproblem2&cpid=1491
# =============================================================================

"""
【Problem Description】
- There is an N × N canvas (N is even, 2 ≤ N ≤ 2000)
- The canvas should satisfy the "reflective condition":
  - The top-right quadrant is reflected to all four quadrants
  - This means: for any cell (i, j), it should equal cells that are
    reflections across the center horizontal and vertical lines
- Given the current canvas and U updates (each toggles one cell),
  output the minimum operations needed to satisfy the reflective condition
  before any updates and after each update

【Input】
- First line: N, U
- Next N lines: N characters ('.' or '#') - the canvas
- Next U lines: r, c - positions to toggle (1-indexed)

【Output】
- U+1 lines: minimum operations before updates and after each update

【Example】
Input:
4 5
..#.
##.#
####
..##
1 3
2 3
4 3
4 4
4 4
Output:
4
3
2
1
0
1

【Solution - Symmetry Analysis】
Key Insight: The canvas is divided into 4 quadrants. Due to reflection:
- (i, j) must equal (i, N-1-j)     (horizontal reflection)
- (i, j) must equal (N-1-i, j)     (vertical reflection)
- (i, j) must equal (N-1-i, N-1-j) (both reflections)

For each 2×2 block in the top-left quadrant, we need exactly 3 cells
to match the 4th. We can compute the "cost" of each block:

Let x = number of '#' in the 4 symmetric positions:
- If x == 0 or x == 4: cost = 0 (already all same)
- If x == 1 or x == 3: cost = 1 (need to change 1 cell)
- If x == 2: cost = 2 (need to change 2 cells, since setting both to
  either '#' or '.' requires 2 changes)

Total minimum operations = sum of costs for all blocks.

When updating a cell (r, c), only its own 2×2 block is affected.
We can recalculate just that block's contribution.

Time: O(N² + U)   Space: O(N²)
"""

import sys
# Use readline for better performance with large input
input = sys.stdin.readline

n, u = map(int, input().split())

canvas = []
updates = []

# Read the canvas
for _ in range(n):
    canvas.append(list(input()))

# Read the update queries
for _ in range(u):
    updates.append(list(map(int, input().split())))

def get_cost(x1, x2, x3, x4):
    """
    Calculate the minimum operations needed for a 2x2 symmetric block.
    Returns 0, 1, or 2 operations needed.
    """
    x = 0
    num = 0

    # Count how many '#' are in the 4 symmetric positions
    if x1 == '#':
        x += 1
    if x2 == '#':
        x += 1
    if x3 == '#':
        x += 1
    if x4 == '#':
        x += 1

    # Calculate minimum operations to make all 4 positions match
    if x == 1 or x == 3:
        num = 1  # Change 1 cell to make all 4 match
    elif x == 2:
        num = 2  # Change 2 cells (best case: set all to either '#' or '.')

    return num

def switch(s):
    """Toggle a cell between '#' and '.'"""
    return '.' if s == '#' else '#'

# Calculate initial total operations
cur_num = 0
for i in range(n // 2):
    for j in range(n // 2):
        # The 4 symmetric positions for block (i, j)
        cur_num += get_cost(
            canvas[i][j],
            canvas[i][n - 1 - j],
            canvas[n - 1 - i][j],
            canvas[n - 1 - i][n - 1 - j]
        )

print(cur_num)

# Process each update
for c, d in updates:
    a = c - 1  # Convert to 0-indexed
    b = d - 1

    # Get cost before the toggle
    num_1 = get_cost(
        canvas[a][b],
        canvas[a][n - 1 - b],
        canvas[n - 1 - a][b],
        canvas[n - 1 - a][n - 1 - b]
    )

    # Toggle the cell
    canvas[a][b] = switch(canvas[a][b])

    # Get cost after the toggle
    num_2 = get_cost(
        canvas[a][b],
        canvas[a][n - 1 - b],
        canvas[n - 1 - a][b],
        canvas[n - 1 - a][n - 1 - b]
    )

    # Update total operations
    cur_num += (num_2 - num_1)

    print(cur_num)