import sys

input = list(map(int, sys.stdin.read().strip().split('\n')))
n = input[0]
input = input[1:]

# The following 7 functions are code from the lecture slides on segment trees, 17/02/2025. 
def left(node):
    return 2 * node
def right(node): 
    return 2 * node + 1
def parent(node):
    return node // 2
def index(tree, node):
    return len(tree) // 2 + node -1
def fill(tree, op=sum):
    parents = range(1, len(tree) // 2)
    for index in reversed(parents): 
        tree[index] = op((tree[left(index)],
                        tree[right(index)]))
def query_(tree, l, r):
    # Returns nodes [l, r) - including left, excluding right
    if l >= r:
        return
    yield tree[l]
    while True:
        pl = parent(l)
        pr = parent(r)
        if pl == pr: 
            return
        if l % 2 == 0:
            yield tree[right(pl)] 
        if r % 2 == 1: 
            yield tree[left(pr)] 
        l,r = pl, pr 
def query(tree, left, right):
    # Helper function, in this case runs sum on the retrieved nodes.
        return sum(query_(tree, left, right))
def update(tree, index, value, op=sum):
    tree[index] = value
    index = parent(index)
    while index > 0:
        tree[index] = op((tree[left(index)],
                          tree[right(index)]))
        index = parent(index)
# Stolen code ends here

positions = [0] * (n+1)
x = 1
for i in input:
    positions[i] = x
    x += 1


T = [1] * (len(input) * 2)
fill(T)
l = 1
r = n

for phase in range(1, n+1):
    if phase % 2 == 1:
        swaps = query(T, index(T, 1), index(T, positions[l]))
        update(T, index(T, positions[l]), 0)
        print(swaps)
        l += 1
    else:
        update(T, index(T, positions[r]), 0)
        swaps = query(T, index(T, positions[r]), index(T, n+1))
        update(T, index(T, positions[r]), 0)
        print(swaps)
        r -= 1


"""
for phase in range(1, n+1):
    if phase % 2 == 1:
        print(f"Comparing swaps for {l}, located at index {positions[l]} in the input.")
        print(f"The difference is {positions[l] - l}, and the sum of placed numbers between is {query(T, index(T, 1), index(T, positions[l]))}")
        swaps = abs(positions[l] - l) - query(T, index(T, 1), index(T, positions[l]))
        #print("Phase: ", phase, " Swaps: ", swaps, " Left: ", left, " Right: ", right)
        update(T, index(T, positions[l]), 1)
        print(f"Updating position {positions[l]} to filled")
        print(T)
        print(swaps)
        l += 1
    else:
        print(f"Comparing swaps for {r}, located at index {positions[r]} in the input.")
        print(f"The difference is {r - positions[r]}, and the sum of placed numbers between is {query(T, index(T, positions[r]), index(T, r))}")
        swaps = abs(r - positions[r]) - query(T, index(T, positions[r]), index(T, r))
        #print("Phase: ", phase, " Swaps: ", swaps, " Left: ", left, " Right: ", right)
        update(T, index(T, positions[r]), 1)
        print(f"Updating position {positions[r]} to filled")
        print(T)
        print(swaps)
        r -= 1
"""
