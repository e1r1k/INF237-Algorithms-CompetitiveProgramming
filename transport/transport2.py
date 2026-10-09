from collections import defaultdict, deque
import sys

import time
start_time = time.time()

data = sys.stdin.read().split()
it = iter(data)

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # List of vertices
        self.edges = defaultdict(dict)

    def add_source_sink(self, u, v):
        self.edges[u][v] = 1
        self.edges[v][u] = 0 
    
    def add_edges(self, u, v):
        self.edges[u][v] = 1
        self.edges[v][u] = 1

def level_bfs(graph, start, goal):
    frontier = deque([start])
    parent = {start: None}
    graph.levels[start] = 0

    while frontier:
        current = frontier.popleft()
        for child in graph.edges[current]:
            if graph.edges[current][child] > 0 and child not in parent:
                parent[child] = current
                graph.levels[child] = graph.levels[current] + 1
                frontier.append(child)
    return graph.levels['SINK!']

def dfs(graph, s, t):
    frontier = deque([s])
    parent = {s:None}

    while frontier:
        current = frontier.pop()
        for child in graph.edges[current]:
            if child == t:
                path = [t]
                while parent[current]:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return list(zip(path, path[1:]))
            if graph.levels[child] > graph.levels[current]:
                parent[child] = current
                frontier.append(child)
    return False

def maxflow(graph, s, t):
    flow = 0
    while level_bfs(graph, s, t):
        print("Generating new level graph")
        path = dfs(graph, s, t)
        while path:
            print(path)
            for u, v in path:
                graph.edges[u][v] -= 1
                graph.edges[v][u] += 1
            flow += 1
            path = dfs(graph, s, t)
    return flow

# Read inputs
s = int(next(it))  # Not used in logic
r = int(next(it))
f = int(next(it))
t = int(next(it))

sources = [next(it) for _ in range(r)]
factories = [next(it) for _ in range(f)]

graph = Graph()

# Add source/sink edges
for src in sources:
    graph.add_source_sink('SOURCE!', src)
for fac in factories:
    graph.add_source_sink(fac, 'SINK!')

# Process firm connections
for _ in range(t):
    y = int(next(it))
    firm = [next(it) for _ in range(y)]
    for i in range(len(firm)):
        for j in range(i + 1, len(firm)):
            graph.add_bidirectional_edge(firm[i], firm[j])

level_bfs(graph, 'SOURCE!', 'SINK!')

print(maxflow(graph, 'SOURCE!', 'SINK!'))
print("--- %s seconds ---" % (time.time() - start_time))