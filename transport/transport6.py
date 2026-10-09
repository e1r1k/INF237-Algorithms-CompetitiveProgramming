from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.E = [[] for _ in range(len(vertices))]
        self.R = [[-1] * len(vertices) for _ in range(len(vertices))]
        self.levels = [-1] * len(vertices)

    def add_edge(self, u, v):
        self.R[u].append([v, 1, 0, len(self.R[v])])
        self.R[v].append([u, 0, 0, len(self.R[u]) - 1])

def bfs(graph, s, t):
    q = deque([s])
    parent = {}
    while q:
        v = q.popleft()
        for u in graph.V: # !
            if u in parent:
                continue # seen it before
            if graph.R[v][u] <= 0:
                continue # vu saturated
            parent[u] = v
            q.append(u)
            if u == t:
                return create_path(parent, s, t)

def create_path(parent, s, t):
    path = [t]
    while t != s:
        t = parent[t]
        path.append(t)
    return tuple(reversed(path))

edges = lambda p: zip(p, p[1:])

def maxflow(graph, s, t):
    flow = 0
    while P := bfs(graph, s, t):
        b = min(graph.R[v][u] for (v, u) in edges(P))
        flow += b
        for i in range(1, len(P)):
            v, u = P[i - 1], P[i]
            graph.R[v][u] -= b
            graph.R[u][v] += b
    return flow

s, r, f, t = map(int, input().split())

name_to_int = {}
def get_id(name):
    if name not in name_to_int:
        name_to_int[name] = len(name_to_int)
    return name_to_int[name]

resources = [get_id(name) for name in input().split()]
factories = [get_id(name) for name in input().split()]

transport = []
for _ in range(t):
    c = input().split()
    operates_in = c[1:]
    transport.append(operates_in)
transport_vertices = []

state_count = len(name_to_int)
V = state_count + 2 * t + 2  
start = V - 2
goal = V - 1
graph = Graph(list(range(2*t+2+state_count)))

for src in resources:
    graph.add_edge(start, src)
for fac in factories:
    graph.add_edge(fac, goal)

resources_set = set(resources)
factory_set = set(factories)

for i, states in enumerate(transport):
    upper_t = state_count + 2 * i
    lower_t = state_count + 2 * i + 1
    graph.add_edge(upper_t, lower_t)

    for name in states:
        state = get_id(name)
        if state in resources_set:
            graph.add_edge(state, upper_t)
            graph.add_edge(lower_t, state)
        elif state in factory_set:
            graph.add_edge(lower_t, state)
            graph.add_edge(state, upper_t)
        else:
            graph.add_edge(state, upper_t)
            graph.add_edge(lower_t, state)

for ege in graph.R:
    print(ege)
print(maxflow(graph, start, goal))