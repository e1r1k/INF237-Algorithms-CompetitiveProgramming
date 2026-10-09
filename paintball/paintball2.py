import sys





def bpm(u, match_to, visited, adj):
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            if match_to[v] == -1 or bpm(match_to[v], match_to, visited, adj):
                match_to[v] = u
                return True
    return False

def max_bipartite_matching(n, adj):
    match_to = [-1] * (2 * n + 2)  # index over right-side clone nodes
    result = []

    for u in range(1, n + 1):  # original left-side nodes
        visited = [False] * (2 * n + 2)
        if bpm(u, match_to, visited, adj):
            continue
        else:
            print("Impossible")
            exit()

    targets = [0] * (n + 1)
    for v in range(n + 1, 2 * n + 1):
        if match_to[v] != -1:
            targets[match_to[v]] = v - n

    return targets[1:]



data = map(int, sys.stdin.read().split())
it = iter(data)

n = next(it)
m = next(it)




adj = [[] for _ in range(2*n + 2)]
for a, b in edges:
    adj[a].append(b+n)
    adj[b].append(a+n)