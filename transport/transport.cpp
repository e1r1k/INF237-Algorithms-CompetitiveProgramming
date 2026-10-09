#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <unordered_set>
#include <deque>

using namespace std;


vector<pair<int, int>> bfs(vector<vector<int>>& graph, int s, int t) {
    deque<int> frontier;
    int vertex_count = graph.size();
    frontier.push_back(s);
    vector<int> parents(vertex_count, -1);
    vector<pair<int, int>> path;
    
    while (frontier.size() > 0) {
        int current = frontier.front();
        frontier.pop_front();
        
        for (int v = 1; v < vertex_count; v++) {
            int capacity = graph[current][v];
            if ((capacity > 0) && (parents[v] == -1)) {
                parents[v] = current;
                frontier.push_back(v);
                if (v == t) {
                    while (parents[v] >= 0) {
                        path.push_back(make_pair(parents[v], v));
                        v = parents[v];
                    }
                    reverse(path.begin(), path.end());
                    return path;
                }
            }
        }
    }
    return path;
}

int maxflow(vector<vector<int>>& graph, int s, int t) {
    int flow = 0;
    vector<pair<int, int>> path = bfs(graph, s, t);

    while (path.size() > 0) {
        for(pair<int, int> edge : path) {
            int u = edge.first;
            int v = edge.second;

            graph[u][v] -= 1;
        }
        flow += 1;
        path = bfs(graph, s, t);
    }
    return flow;
}

int main () {
    int s, r, f, t;
    cin >> s >> r >> f >> t;
    vector<string> materials;
    vector<string> factories;
    vector<string> other;
    for (int x = 0; x < r; x++) {
        string state;
        cin >> state;
        materials.push_back(state);
    }
    for (int x = 0; x < f; x++) {
        string state;
        cin >> state;
        factories.push_back(state);
    }
    vector<unordered_set<string>> operates_in_list;
    for (int x = 0; x < t; x++) {
        int n;
        cin >> n;
        unordered_set<string> operates_in;
        for (int x = 0; x < n; x++) {
            string state;
            cin >> state;
            if ((find(factories.begin(), factories.end(), state) == factories.end()) && (find(materials.begin(), materials.end(), state) == materials.end())) {
                other.push_back(state);
            }
            operates_in.insert(state);
        }
        operates_in_list.push_back(operates_in);
    }

    vector<vector<int>> edges(s+2, vector<int>(s+2, -1));
    for (unordered_set<string>& operates_in : operates_in_list) {
        for (int x = 0; x < materials.size(); x++) {
            if (operates_in.count(materials[x]) == 0) continue;
    
            edges[0][x+1] = 1;
            edges[x+1][0] = 0;
    
            for (int y = 0; y < factories.size(); y++) {
                if (operates_in.count(factories[y]) == 0) continue;
    
                edges[x+1][y+r+1] = 1;
                edges[y+r+1][x+1] = 1;
    
                edges[y+r+1][s+1] = 1;  
                edges[s+1][y+r+1] = 0;
            }
        }
    
        for (int x = r+f+1; x <= s; x++) {
            if (operates_in.count(other[x-f-r-1])  == 0) continue;
            for (int y = 0; y < factories.size(); y++) {
                if (operates_in.count(factories[y]) == 0) continue;
    
                edges[x][y+r+1] = 1;
                edges[y+r+1][x] = 1;
            }
        }
    }
    cout << maxflow(edges, 0, edges[0].size()-1);
    
}

