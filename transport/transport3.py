from collections import defaultdict, deque
import sys

data = sys.stdin.read().split()
it = iter(data)

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # List of vertices
        self.edges = defaultdict(dict)
        self.levels = defaultdict(None)

    def add_source_sink(self, u, v):
        self.edges[u][v] = 1
        self.edges[v][u] = 0 
    
    def add_edges(self, u, v):
        self.edges[u][v] = 1
        self.edges[v][u] = 1

# BFS with the added condition that residual capacity is not 0 (in this case only relevant for source/sink)
def level_bfs(graph, start):
    graph.levels = {}
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
    return 'SINK!' in graph.levels

def dfs(graph, u, t, flow, visited):
    if u == t:
        return flow
    visited.add(u)
    
    for v in graph.edges[u]:
        if graph.edges[u][v] > 0 and graph.levels.get(v, -1) == graph.levels[u] + 1 and v not in visited:
            pushed = dfs(graph, v, t, min(flow, graph.edges[u][v]), visited)
            if pushed > 0:
                graph.edges[u][v] -= pushed
                graph.edges[v][u] += pushed
                return pushed
    return 0

def maxflow(graph, s, t):
    flow = 0
    while level_bfs(graph, s):
        while True:
            pushed = dfs(graph, s, t, float('inf'), set())
            if pushed == 0:
                break
            flow += pushed
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
        
print(maxflow(graph, 'SOURCE!', 'SINK!'))     
