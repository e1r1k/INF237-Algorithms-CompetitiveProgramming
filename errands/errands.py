from collections import defaultdict
import math
import sys

def euclidean(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    return math.sqrt((x2-x1) **2 + (y2-y1) ** 2)

input = list(map(lambda x: x.split(), sys.stdin.read().strip().split('\n')))
n = int(input[0][0])

num_to_labels = {}
labels_to_num = {}
nodes = []

for x in range(1, n+1):
    name = input[x][0]
    num_to_labels[x-1] = name
    labels_to_num[name] = x-1
    # Nodes are positions in x, y coordinate space
    nodes.append((float(input[x][1]), float(input[x][2])))


def solve(subset):
    stops = []
    # The input, "subset" is a list of string names. We convert them to integers for easy indexing and go back at end
    stops.append(nodes[labels_to_num['work']])
    for x in subset:
        stops.append(nodes[labels_to_num[x]])
    stops.append(nodes[labels_to_num['home']])

    # Edges is a 2d distance matrix
    edges = [[None] * n for _ in range(n)]
    for x in range(len(stops)):
        for y in range(len(stops)):
            dist = euclidean(stops[x], stops[y])
            edges[x][y] = dist
            edges[y][x] = dist

    INF = 10**100
    len_subset = len(stops)

    # The DP setup is we have 2^n possible subset of nodes, and could possibly end the subset at n different nodes
    # so the cost of having a path starting at 0, ending at -col- and having visited the subset -row- is store in DP[row][col]
    DP = [[INF for _ in range(len_subset)] for _ in range(2**len_subset)]
    # Base case is we are at work (0)
    DP[1][0] = 0
    # Parents are stored in the same way
    parents = [[0] * len_subset for _ in range(2**len_subset)]

    # Go through each possible subset using bitmask to represent the subsets. Think of it like a list of truth values, where 0
    # is all the way to the right. 0001 would be a subset of four nodes where 0 is visite but the rest are unvisited.
    # through magic this is the same as iterating through a range of numbers from 0 to n
    for visited in range(2**len_subset):
        # Given a subset (visited), this is the subset ending in the node current with -visited- nodes.
        for current in range(len_subset):
            # Given a path ending in the node -current- having visited -visited- nodes, compute the cost of moving to all possible
            # next nodes that are not visited yet.
            for next in range(len_subset):
                if visited & (1 << next) == 0:
                    # We may end up in cases where the candidate set has already been visited, so we check what the cost would
                    # be moving from the current set to the next node, and compare to the stored value
                    candidate_set = visited | (1 << next)
                    candidate_cost = DP[visited][current] + edges[current][next]
                    # Only if they are less we update candidate set and  -- !!! parent value
                    if candidate_cost < DP[candidate_set][next]:
                        DP[candidate_set][next] = candidate_cost
                        parents[candidate_set][next] = current
    
    path = []
    current = len_subset-1
    visited_set = (1 << len_subset) - 1

    while current:
        parent = parents[visited_set][current]
        visited_set -= (1 << current)
        current = parent
        path.append(current)
    del path[-1]

    return ' '.join(list(reversed([subset[x-1] for x in path])))

for subset in input[n+1:]:
    print(solve(subset))
