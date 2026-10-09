import itertools
from queue import PriorityQueue
import sys

data = map(int, sys.stdin.read().split())
it = iter(data)

case_count = next(it)
cases = []

for x in range(case_count):
    n, m, l, s = list(itertools.islice(it, 4))
    k = list(itertools.islice(it, s))
    edges = list(itertools.islice(it, 3 * m))
    print(edges)
    edges = [edges[i:i+3] for i in range(0, len(edges), 3)] 
    cases.append([[n, m, l, s], k] + edges)

print(cases)

def solve_case(case):
    n = case[0][0]
    prog_size = case[0][2]
    edges = case[2:]

    graph = [[] for x in range(n+1)]

    for edge in edges:
        graph[edge[0]].append((edge[2], edge[0], edge[1]))
        graph[edge[1]].append((edge[2], edge[1], edge[0]))

    visited = [0] * (n+1)
    in_mst = [False] * (n+1)
    visited_count = 0
    frontier = PriorityQueue()

    for station in case[1]:
        visited[station] = 0
        in_mst[station] = True
        visited_count += 1
        for edge in graph[station]:
            frontier.put(edge)

    while visited_count < n:
        (cost, start, end) = frontier.get()
        if not in_mst[end]:
            visited[end] = cost + prog_size
            in_mst[end] = True
            visited_count += 1
            for edge in graph[end]:
                if not in_mst[edge[2]]:
                    frontier.put(edge)
    return sum(visited)

for x in cases:
    print(solve_case(x))