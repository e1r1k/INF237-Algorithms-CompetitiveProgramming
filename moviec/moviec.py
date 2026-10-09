import sys

input = list(map(lambda x: [int(y) for y in x.split()], sys.stdin.read().strip().split('\n')))

n = input[0][0]
cases = []
for x in range(1, n+2, 2):
    cases.append([input[x], input[x+1]])

# The following 7 functions are code from the lecture slides on segment trees, 17/02/2025. 

# The tree is a list where the first half is internal nodes and the last half is leaves
# This means indexing can be done through simple multiplication/division 
def left(node):
    return 2 * node
def right(node): 
    return 2 * node + 1
def parent(node):
    return node // 2
def index(tree, node):
    return len(tree) // 2 + node
def fill(tree):
    parents = range(1, len(tree) // 2 )
    for index in reversed(parents): 
        tree[index] = tree[left(index)] + tree[right(index)]
        
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
    if left == right:
        return 0
    else: 
        return sum(query_(tree, left, right))
    
def update(tree, index, value, op=sum):
    tree[index] = value
    index = parent(index)
    while index > 0:
        tree[index] = op((tree[left(index)],
                          tree[right(index)]))
        index = parent(index)
# Stolen code ends here

def solve_case(case):
    m = case[0][0]
    r = case[0][1]

    # Top is the size of parent nodes + initial leaf nodes
    # The positions are a reversed list from m to 1, as the movie labeled 1 will be in index 5 of the leaf-part of the list,
    # the movie labeled to will be in position m-1 and so on. Index 0 is always 0, as we also pad the tree.
    top = 2*m+r
    positions = [0] + list(range(m, 0, -1))

    # We pad the array so that it can potentially fit r requests where we have to update positions for each request
    T = [0] * (m+r) + [1] * m + [0] * r
    tree_size = len(T)
    fill(T)
    print(T)
    results = []
    for request in case[1]:
        # Sum  the movies above it, update the tree so that the top index in tree is 1 (filled), 
        # update position in array and increase top.
        x = query(T, index(T, positions[request]), top)
        results.append(x)
        update(T, top, 1)
        update(T, index(T, positions[request]), 0)
        positions[request] = top - tree_size // 2 +1
        top += 1
        
    print(" ".join(list(map(str, results))))


for case in cases:
    solve_case(case)

