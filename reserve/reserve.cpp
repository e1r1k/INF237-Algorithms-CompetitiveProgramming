#include <iostream>
#include <vector>
#include <queue>
#include <numeric>

using namespace std;

int main() {
    long long case_count;
    // >> Works kind of like iterator, giving the next item in input. Looks like C++ splits/strips the input automatically
    cin >> case_count;

    vector<vector<vector<long long>>> cases;
    // For as many times as we have cases:
    for (int x = 0; x < case_count; x++) {
        long long n,m,l,s;
        cin >> n >> m >> l >> s;

        // n m l s are the case parameters | n = station count | m = edge count | l = program sizze | s = station count |
        // Create vector for these
        vector<long long> case_params = {n,m,l,s};
        vector<long long> initial_stations;
        
        // Create vector for intial stations
        for (int y = 0; y < s; y++) {
            long long station;
            cin >> station;
            initial_stations.push_back(station);
        }

        // Add vector containing these two vectors to case vector
        cases.push_back({case_params, initial_stations});

        // For each edge, add the edge to this vector as well
        vector<vector<long long>> edges;
        for (int z = 0; z < m; z++) {
            long long c, f, t;
            cin >> c >> f >> t;
            cases[x].push_back({c, f, t});
        }
    }

    // Process cases:
    for (vector<vector<long long>> cse : cases) {
        long long n = cse[0][0];
        long long m = cse[0][1];
        long long prog_size = cse[0][2];

        // Make adjacency list with cost in first index, end-node in second (the start node is the index in graph)
        vector<vector<pair<long long, long long>>> graph(n+1);
        for (int i = 2; i < cse.size(); i++) {
            long long from = cse[i][0];
            long long to = cse[i][1];
            long long cost = cse[i][2];

            graph[from].push_back({cost + prog_size, to});
            graph[to].push_back({cost + prog_size, from});
        }

        // Create two vectors to keep track of the cost of visiting each node and if the nodes have been added
        long long total_cost = 0;
        vector<long long> in_mst(n+1, 0);
        long long visited_count = cse[1].size();

        // Priority queue of pair<int,int>. | "container" - vector<pair<int,int>> is needed as we need to use greater to tell
        // the queue to be a min-heap instead of max heap. Else, this is inferred by the constructor.
        priority_queue<pair<long long, long long>, vector<pair<long long,long long>>, greater<pair<long long,long long>>> frontier;
        
        // cse[1] is the list of initial stations. Add these to mst for free and increase visited count. 
        for (long long station : cse[1]) {
            in_mst[station] = 1;
            for (pair<long long, long long> edge : graph[station]) {
                frontier.push(edge);
            }
        }
/*/  PRINT GRAPH FOR DEBUGGING:
        int index = 0;
        for (auto node : graph) {
            cout << "Node " << index << ": ";
            for (auto edge : node) {
                cout << "[(" << edge.first << ", " << edge.second << ")]";
            }
            index += 1;
            cout << '\n';
        }
/*/

        // While not all nodes are visited (the input is defined so that the graph is fully connected), explore the  cheapest
        // edges first until all nodes are added.
        while (visited_count < n) {
            pair<long long,long long> edge = frontier.top();
            frontier.pop();
            if (!(in_mst[edge.second])) {
                total_cost  += edge.first;
                //cout << "Adding edge: (" << edge.first << ", " << edge.second << "), Cost: " << edge.first + prog_size << '\n';
                in_mst[edge.second] = 1;
                visited_count += 1;
                for (pair<long long,long long> neighbour : graph[edge.second]) {
                    if (!in_mst[neighbour.second]) {
                        frontier.push(neighbour);
                    }
                }
            }
        }
        // C++ does not have a sum function, uses "accumulate" instead  . 
        cout << total_cost << endl;
    }
    return 0;
}