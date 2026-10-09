import sys
from collections import defaultdict



data = map(int, sys.stdin.read().split())
it = iter(data)

n = next(it)

children = defaultdict(list)
cost_list = [0] * n
has_parent = [False] * n

for employee in range(n):
    cost_list[employee]= next(it)
    
    subordinate_count = next(it)
    for _ in range(subordinate_count):
        subordinate = next(it)
        children[employee].append(subordinate)
        has_parent[subordinate] = True  

root = has_parent.index(False) # Only one node will be false, as the most sour excellence or whatever
INFINITE = 10**100 # Big big number
DP = [None] *n

v=list(range(n)) 

def dfs(v):
    # Base case:
    pick = cost_list[v]
    skip_above = 0
    # If the node is a leaf:
    if not children[v]: 
        # Picking the node below is  not allowed, as it does not exist
        skip_below = INFINITE 
        # Cost is the node's cost, or the cost of the node above
        DP[v] = (pick, skip_below, skip_above)
        return
    
    # If the node is not a leaf:
    # Go through each child node
    for c in children[v]:
        # Recursively dfs so that every node below is processed
        dfs(c)
        # Since we are looking for both dominant and independent set, if we pick a node then we can't pick any of its children
        # pick is therefore the sum of skipping every child
        pick += DP[c][2]
        # If we don't pick, then each child node must be dominate from below or picked
        skip_above += min(DP[c][0], DP[c][1]) 

    # We consider every child node as a possible dominator of the current node being processed
    skip_below = INFINITE
    promote = INFINITE
    cost_sum = 0
    for c in children[v]: 
        promote = min(promote, (max(0, DP[c][0] - DP[c][1])))
        cost_sum += min(DP[c][0], DP[c][1])

    skip_below = cost_sum + promote

    DP[v] = (pick, skip_below, skip_above)
        
dfs(root)
   
print(min(DP[root][0], DP[root][1]))
