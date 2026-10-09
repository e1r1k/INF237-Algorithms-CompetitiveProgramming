#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Graph {
    public:
        int V; // Vertex count
        vector<vector<int>> edges;                
        vector<vector<int>> capacity;

        // Constructor, takes list of vertices as input and sets all edges between vertices to -1
        Graph(int vertices) {
            V = vertices;
            edges.assign(V, vector<int>());
            capacity.assign(V, vector<int>(V, 0));
        }

        /*  Changes value of an edge to this edges capacity. Also adds a reverse edge with capacity that increases as 
            capacity of forwards edge decreases. If a more efficient path is found later, then we can "send flow backwards -
            in essence keeping flow in the node that is maxed out and sending more to the other side"
        */
        void add_edge(int u, int v) {
            if (capacity[u][v] == 0 && capacity[v][u] == 0) {
                edges[u].push_back(v);
                edges[v].push_back(u);
            }
            capacity[u][v] += 1;
        }
};

// BFS to find paths
vector<int> bfs(Graph& g, int s, int t, vector<int>& parent) {
    fill(parent.begin(), parent.end(), -1);
    queue<int> q;
    q.push(s);
    parent[s] = -2;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : g.edges[u]) {
            if (g.capacity[u][v] > 0 && parent[v] == -1) {
                parent[v] = u;
                if (v == t) return parent;
                q.push(v);
            }
        }
    }

    return parent; 
}

/* 
Maxflow finds "augmenting paths" - paths where more flow can be sent and adds these until there are no more edges with 
 residual capacity. If a backwards edge is used, this means that there is a better option for some path. Therefore, in order
 to find the valid targets we construct a new edge list  after running algorithm the first time  where we only include the used edges
 and remove the ones that have been becktracked through. 
 */ 
vector<vector<int>> maxflow(Graph& g, int s, int t) {
    vector<vector<int>> flow_paths;
    vector<int> parent(g.V);
    int flow = 0;

    while (true) {
        parent = bfs(g, s, t, parent);
        if (parent[t] == -1) break;

        // Reconstruct path and apply flow
        vector<int> path;
        int cur = t;
        while (cur != s) {
            path.push_back(cur);
            cur = parent[cur];
        }
        path.push_back(s);
        reverse(path.begin(), path.end());
        flow_paths.push_back(path);

        // Send flow = 1 along the path
        for (int i = 0; i < (int)path.size() - 1; ++i) {
            int u = path[i];
            int v = path[i + 1];
            g.capacity[u][v] -= 1;
            g.capacity[v][u] += 1;
        }

        ++flow;
    }

    if (flow < (g.V - 2) / 2) {
        cout << "Impossible\n";
        exit(0);
    }

    return flow_paths;
}

int main() {
    int n, m;
    cin >> n >> m;
    /*
    We duplicate the vertices to get the form and add two nodes (source and sink)
            1  ->  1
    s   ->  2  ->  2 -> t
            3  ->  3 
    */ 
    int total_vertices = 2 * n + 2;

    Graph g(total_vertices);

    // Add edges to the adjacency matrix
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;

        // Original edge between layers
        g.add_edge(a, b + n);
        g.add_edge(b, a + n);

        // Source to first layer
        g.add_edge(0, a);
        g.add_edge(0, b);

        // Second layer to sink
        g.add_edge(a + n, total_vertices-1);
        g.add_edge(b + n, total_vertices-1);
    }

    vector<vector<int>> first_pass_paths = maxflow(g, 0, total_vertices-1);

    // Build new graph only from forward-used edges
    Graph g2(total_vertices);
    for (const auto& path : first_pass_paths) {
        for (size_t i = 0; i + 1 < path.size(); ++i) {
            g2.add_edge(path[i], path[i + 1]);
        }
    }

    // Find actual paths from s to t again in new graph
    vector<vector<int>> final_paths = maxflow(g2, 0, total_vertices-1);

    for (const auto& path : final_paths) {
        // The third node in each path is the target of interest
        int target = path[2] - n;
        cout << target << '\n';
    }

    return 0;
}