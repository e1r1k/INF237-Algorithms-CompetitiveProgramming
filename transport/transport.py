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

# BFS with the added condition that residual capacity is not 0 (in this case only relevant for source/sink)
def bfs(graph, start, goal):
    frontier = deque([start])
    parents = {start:None}
    while frontier:
        current = frontier.popleft()
        for v in graph.edges[current]:
            edge = graph.edges[current][v]
            if (edge > 0) and (v not in parents):
                parents[v] = current
                frontier.append(v)
                if v == goal:
                    path = [goal]
                    while parents[v]:
                        v = parents[v]
                        path.append(v)
                    path.reverse()
                    return list(zip(path, path[1:]))
    return None

def maxflow(g):
    flow = 0
    path = bfs(g, 'SOURCE!', 'SINK!')

    while path:
        for x, y in path:
            g.edges[x][y] -= 1 # We can not travel back to source node, as it is not really a state. 
        flow += 1
        path = bfs(g, 'SOURCE!', 'SINK!')

    return flow

s = int(next(it))
r = int(next(it))
f = int(next(it))
t = int(next(it))

sources = []
for _ in range(r):
    sources.append(next(it))

factories = []
for _ in range(f):
    factories.append(next(it))

vertex_list = ["SOURCE!"] + list(sources) + list(factories) + ["SINK!"]
graph = Graph(vertex_list)

for fact in factories:
    graph.add_source_sink(fact, 'SINK!')
for src in sources:
    graph.add_source_sink('SOURCE!', src)

edges_list = []
for x in range(1, t+1):
    y = int(next(it))
    firm = []
    for _ in range(y):
        firm.append(next(it))
    for u in range(len(firm)-1):
        for v in range(u+1, len(firm)):
            graph.add_edges(firm[u], firm[v])
        
print(maxflow(graph))     



print("--- %s seconds ---" % (time.time() - start_time))