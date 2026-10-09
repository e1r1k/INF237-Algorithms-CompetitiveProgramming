from collections import defaultdict
import heapq
import sys

input = list(map(lambda x: x.split(), sys.stdin.read().strip().split('\n')))
if len(input) < 2:
    print(0)
    exit()
house_count = int(input[0][0])
pos_connections_count = int(input[0][1])
insecure_count = int(input[0][2])

houses = set(range(1, house_count +1))
insecure = set(map(int, input[1]))
insecure_count = len(insecure)
secure = houses - insecure
secure = list(secure)
secure_count = len(secure)
edges = [(int(y[2]), int(y[0]), int(y[1])) for y in input[2:]]

def reverse_edge(edge):
    return (edge[0], edge[2], edge[1])

graph = defaultdict(list)
for edge in edges:
    graph[edge[1]].append(edge)
    graph[edge[2]].append(reverse_edge(edge))

if secure_count == 0:
    if house_count > 0:
        insecure = list(insecure)
        for house in insecure:
            visited = [0]
            for edge in graph[insecure[0]]:
                visited.append(edge[0])
            if len(visited) == house_count:
                print(sum(visited))
                exit()
            else:
                print(visited)
    print("impossible")
    exit()

# Make two frontiers for MST, one secure and one insecure
frontier = []
insecure_frontier = []
heapq.heapify(frontier)
heapq.heapify(insecure_frontier)
visited = set()

#if there are no secure houses, then the task is impossible
if len(secure) > 0:
    start_node = secure[0]
    visited.add(start_node)
else:
    print("impossible")
    exit()

# Generate initial frontier by adding children of start node
for edge in graph[start_node]:
    if edge[2] in visited:
        continue
    if edge[2] in insecure:
        heapq.heappush(insecure_frontier, edge)
    else:
        heapq.heappush(frontier, edge)

visited_count = 1
cost = 0

# Try to create MST including all secure houses.
while visited_count < secure_count and frontier:
    current = heapq.heappop(frontier)

    if current[2] in visited:
        continue  # Skip already visited nodes
    visited.add(current[2])
    visited_count += 1
    cost += current[0]

    for edge in graph[current[2]]:  # Explore the new node's neighbors
        if edge[2] in visited:
            continue
        if edge[2] in insecure:
            heapq.heappush(insecure_frontier, edge)
        else:
            heapq.heappush(frontier, edge)

# If no MST can be made to contain all secure houses, task is impossible
if visited_count < secure_count:
    print("impossible")
    exit()

# If MST can be made between secure houses, add insecure houses until all houses are included. Do not add new edges, as only
# edges from secure houses (or initial houses) can call.
while visited_count < house_count and insecure_frontier:
    current = heapq.heappop(insecure_frontier)

    if current[2] in visited:
        continue
    visited.add(current[2])
    visited_count += 1
    cost += current[0]

# If not all insecure houses can be connected, task is impossible. Else, minimum cost is found.
if visited_count < house_count:
    print("impossible")
else:
    print(cost)
