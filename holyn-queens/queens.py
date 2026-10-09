import sys

data = map(int, sys.stdin.read().split())
it = iter(data)

def solve():
    n = next(it)
    m = next(it)

    # Assuming all test inputs are like the provided, where the last line is 0 0
    if n == 0 and m == 0:
        exit()

    # Solve it like normal with binary search backtracking just with an extra check for if the spot is blocked
    blocked = set()
    for x in range(m):
        blocked.add((next(it), next(it)))

    # Different sets for the columns and diagonals as diagonals are shared for lower rows.
    used_columns = set()
    right_diagonals = set()
    left_diagonals = set()

    # Solutions is a list because they are mutable and can be edited from any level of recursion
    solutions = [0]

    def search(x):
        # If we have reached the last row and placed a queen, then we have found a valid solution.
        if x == n:
            solutions[0] += 1
            return
        
        # Else: go through each column in the row, check if the column is blocked by hole or threatened, and if not - 
        # "place a queen" (update the threatened spots), run the algorithm one row below. After running for all the
        # rows below, remove the blocked positions on the way "up" the tree again.
        for col in range(n):
            if col in used_columns or x+col in left_diagonals or x - col in right_diagonals or (x, col) in blocked:
                continue

            used_columns.add(col)
            right_diagonals.add(x-col)
            left_diagonals.add(x+col)

            search(x+1)

            used_columns.remove(col)
            right_diagonals.remove(x-col)
            left_diagonals.remove(x+col)

    # Start at row 0, print number of solutions at the end.
    search(0)
    print(solutions[0])

while it:
    solve() 
            
            

    
