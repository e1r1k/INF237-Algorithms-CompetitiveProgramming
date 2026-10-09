from collections import deque

from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = [[] for _ in range(vertices)]
        self.levels = [-1] * vertices

    def add_edge(self, u, v, capacity=1):
        self.edges[u].append([v, capacity, 0, len(self.edges[v])])
        self.edges[v].append([u, 0, 0, len(self.edges[u]) - 1])

def level_bfs(graph, s, t):
    graph.levels = [-1] * graph.V
    queue = deque([s])
    graph.levels[s] = 0
    while queue:
        u = queue.popleft()
        for v, cap, flow, _ in graph.edges[u]:
            if graph.levels[v] == -1 and cap > flow:
                graph.levels[v] = graph.levels[u] + 1
                queue.append(v)
    return graph.levels[t] != -1

def dfs(graph, u, t, flow, next):
    if u == t or flow == 0:
        return flow
    while next[u] < len(graph.edges[u]):
        edge = graph.edges[u][next[u]]
        v, cap, f, rev_idx = edge
        if graph.levels[v] == graph.levels[u] + 1 and cap > f:
            pushed = dfs(graph, v, t, min(flow, cap - f), next)
            if pushed:
                edge[2] += pushed  # update forward edge flow
                graph.edges[v][rev_idx][2] -= pushed  # update reverse edge flow
                return pushed
        next[u] += 1
    return 0

def maxflow(graph, s, t):
    flow = 0
    graph.levels = [-1] * graph.V  
    while level_bfs(graph, s, t):
        next = [0] * graph.V
        pushed = dfs(graph, s, t, float('inf'), next)
        while pushed:
            flow += pushed
            pushed = dfs(graph, s, t, float('inf'), next)
        graph.levels = [-1] * graph.V  
    return flow

s, r, f, t = map(int, input().split())

name_to_int = {}
next_id = 0

# Assign IDs to resources
resources = input().split()
resource_ids = []
for name in resources:
    if name not in name_to_int:
        name_to_int[name] = next_id
        next_id += 1
    resource_ids.append(name_to_int[name])

# Assign IDs to factories
factories = input().split()
factory_ids = []
for name in factories:
    if name not in name_to_int:
        name_to_int[name] = next_id
        next_id += 1
    factory_ids.append(name_to_int[name])

transport = []
for _ in range(t):
    parts = input().split()
    states = parts[1:]
    transport.append(states)
    for name in states:
        if name not in name_to_int:
            name_to_int[name] = next_id
            next_id += 1

state_count = next_id
V = state_count + 2 * t + 2
start = V - 2
goal = V - 1
graph = Graph(V)

for src in resource_ids:
    graph.add_edge(start, src)
for fac in factory_ids:
    graph.add_edge(fac, goal)

resources_set = set(resource_ids)
factory_set = set(factory_ids)

for i, states in enumerate(transport):
    upper_t = state_count + 2 * i
    lower_t = state_count + 2 * i + 1

    graph.add_edge(upper_t, lower_t)

    for name in states:
        state = name_to_int[name]
        if state in resources_set:
            graph.add_edge(state, upper_t)
        elif state in factory_set:
            graph.add_edge(lower_t, state)
        else:
            graph.add_edge(state, upper_t)
            graph.add_edge(lower_t, state)
"""
print(name_to_int)
x = 0
for edge in graph.edges:
    print(x, " : ", edge)
    x += 1
    """

print(maxflow(graph, start, goal))