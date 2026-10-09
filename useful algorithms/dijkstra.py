def dijkstra(s, edges, n):
    unvisited = set(range(n))
    visited = set()

    distances =  [float('inf')] * n
    distances[s] = 0
    previous_node = [None] * n

    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])

        print("Distances: ", distances)
        print("Current: ", current)
        print("Visited node: ", visited)
        print("Unvisited: ", unvisited)
        for child in edges[current]:
            cost = child[0] + distances[current]
            v = child[1]
            if cost < distances[v]:
                distances[v] = cost
                previous_node[v] = current 
        
        unvisited.remove(current)
        visited.add(current)

    return distances, previous_node