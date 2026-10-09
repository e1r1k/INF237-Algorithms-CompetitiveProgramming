import sys

INF = float('inf')

def tsp(graph):
    num_nodes = len(graph)
    dp = [[INF] * num_nodes for _ in range(1 << num_nodes)]
    dp[1][0] = 0  # Start at node 0
    parent = [[0] * num_nodes for _ in range(1 << num_nodes)]

    for visited_set in range(1 << num_nodes):
        for last_node in range(num_nodes):
            for next_node in range(num_nodes):
                if visited_set & (1 << next_node) == 0:  # If next_node is not visited
                    new_visited_set = visited_set | (1 << next_node)
                    new_cost = dp[visited_set][last_node] + graph[last_node][next_node]

                    if new_cost < dp[new_visited_set][next_node]:
                        dp[new_visited_set][next_node] = new_cost
                        parent[new_visited_set][next_node] = last_node

    # Backtrack to reconstruct path
    path = []
    current_node = num_nodes - 1
    visited_set = (1 << num_nodes) - 1  # All nodes visited

    while current_node:
        prev_node = parent[visited_set][current_node]
        visited_set -= (1 << current_node)
        current_node = prev_node
        path.append(current_node)

    return path[::-1]  # Reverse path

# Read locations
locations = {}
for _ in range(int(input().strip())):
    name, x, y = input().split()
    locations[name] = complex(round(float(x) * 1e5), round(float(y) * 1e5))

# Process the input to create an adjacency matrix
for line in sys.stdin:
    location_map = {'work': 0, **{name: i + 1 for i, name in enumerate(line.strip().split())}}
    location_list = list(location_map.keys())
    location_map['home'] = len(location_map)
    location_list.append('home')

    # Construct the adjacency matrix
    num_locations = len(location_map)
    distance_matrix = [[INF] * num_locations for _ in range(num_locations)]

    for loc_a in location_map:
        for loc_b in location_map:
            if loc_a < loc_b:
                distance = abs(locations[loc_a] - locations[loc_b])
                distance_matrix[location_map[loc_a]][location_map[loc_b]] = distance
                distance_matrix[location_map[loc_b]][location_map[loc_a]] = distance

    for x in range(len(distance_matrix)):
        print(x, ": ", distance_matrix[x])
    # Run the TSP solver and print the result
    print(" ".join(location_list[i] for i in tsp(distance_matrix)))