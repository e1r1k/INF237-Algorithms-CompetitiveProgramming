from collections import deque
import sys

data = sys.stdin.read().split()
it = iter(data)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.edges[u].append([v, 1])
        self.edges[v].append([u, 0])  

def bfs(graph, s, t, parent):
    visited = [False] * graph.V
    queue = deque([s])
    visited[s] = True
    parent[s] = (-1, -1)
    while queue:
        u = queue.popleft()
        for idx, (v, cap) in enumerate(graph.edges[u]):
            if not visited[v] and cap > 0:
                parent[v] = (u, idx)
                if v == t:
                    return True
                visited[v] = True
                queue.append(v)
    return False

def maxflow(graph, s, t):
    flow = 0
    parent = [(-1, -1)] * graph.V
    while bfs(graph, s, t, parent):
        v = t
        while v != s:
            u, idx = parent[v]
            graph.edges[u][idx][1] -= 1
            for rev in graph.edges[v]:
                if rev[0] == u:
                    rev[1] += 1
                    break
            v = u
        flow += 1
    return flow

s = int(next(it))
r = int(next(it))
f = int(next(it))
t = int(next(it))

name_to_int = {}
def get_id(name):
    if name not in name_to_int:
        name_to_int[name] = len(name_to_int)
    return name_to_int[name]

resources = [get_id(next(it)) for _ in range(r)]
factories = [get_id(next(it)) for _ in range(f)]

transport = []
for _ in range(t):
    n = int(next(it))
    operates_in = [next(it) for _ in range(n)]
    transport.append(operates_in)

state_count = len(name_to_int)+1
V = state_count + 2 * t + 2
start = V - 2
goal = V - 1

graph = Graph(V)

resources_set = set(resources)
factory_set = set(factories)

for src in resources:
    graph.add_edge(start, src)
for fac in factories:
    graph.add_edge(fac, goal)

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

print(maxflow(graph, start, goal))