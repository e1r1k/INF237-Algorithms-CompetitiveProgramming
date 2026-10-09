from collections import deque, defaultdict
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # List of vertices
        self.edges = defaultdict(dict)
        self.used_edges = []

    """
    Adds an edge and a reverse edge with 0 initial capacity. If a more efficient path is found later, then we 
    can "send flow backwards - in essence keeping flow in the node that is maxed out and sending more to the other side"
    """
    def add_edge(self, u, v):
        self.edges[u][v] = 1
        self.edges[v][u] = 0  # Reverse edge with 0 initial capacity

# BFS with the added condition that residual capacity is not 0
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
                    path.append(0)
                    path.reverse()
                    return list(zip(path, path[1:]))
    return None

"""
    Maxflow finds "augmenting paths" - paths where more flow can be sent and adds these until there are no more edges with 
    residual capacity. If a backwards edge is used, this means that there is a better option for some path. Therefore, in order
    to find the valid targets we construct a new edge list  after running algorithm the first time  where we only include the used edges
    and remove the ones that have been becktracked through.
"""
def maxflow(g):
    flow = 0
    path = bfs(g, 0, 2*n+1)
    paths = []

    while path:
        for x, y in path:
            g.edges[x][y] -= 1 # Decrease capacity for ddownwards edge
            g.edges[y][x] += 1 # Incresase capacity for upwards edge
        flow += 1
        for edge in path:
            g.used_edges.append(edge)
        paths.append(path)
        path = bfs(g, 0, 2*n+1)

    if flow < n:
        print("Impossible")
        exit()
    else:
        return paths

data = map(int, sys.stdin.read().split())
it = iter(data)

n = next(it)
m = next(it)

vertices = [0] + list(range(1, n+1)) + list(range(n+1, n+n+1)) + [2*n+1]
graph = Graph(vertices)
"""
We duplicate the vertices and add two nodes (source and sink) to get the form 
            1  ->  1
    s   ->  2  ->  2 -> t
            3  ->  3 
"""
for _ in range(m):
    a = next(it)
    b = next(it)
    # Add edges between nodes that can see each other
    graph.add_edge(a, b+n)
    graph.add_edge(b, a+n)

    # Add edges from source to first layer, second layer to sink
    graph.add_edge(0, a)
    graph.add_edge(0, b)
    graph.add_edge(a+n, 2*n+1)
    graph.add_edge(b+n, 2*n+1)

maxflow(graph)
graph_ = Graph(vertices)
for (x, y) in graph.used_edges:
    if not (y, x) in graph.used_edges:
        graph_.add_edge(x, y)

paths = maxflow(graph_)
targets = [0] * (n+1)
for path in paths:
    targets[path[1][0]] = path[1][1] - n

for target in targets[1:]:
    print(target)
