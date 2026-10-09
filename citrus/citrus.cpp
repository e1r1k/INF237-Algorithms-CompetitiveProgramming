#include <iostream>
#include <vector>

using namespace std;

class Dp {
    public:
        long long pick, skip_above, skip_below;
    
        Dp(long long pick = 0, long long skip_above = 0, long long skip_below = 0)
            : pick(pick), skip_above(skip_above), skip_below(skip_below) {}
    
        void print() {
            cout << "Pick: " << pick << ", Skip above: " << skip_above << ", Skip below: " << skip_below << endl;
        }
    };
    
class T {
    public:
        vector<int> v;  // List of vertices
        vector<long long> w;  // List of costs
        vector<vector<int>> e;  // Edge adjacency list
        int r;  // Root node
    
        T(vector<int>& vertices, vector<long long>& costs, vector<vector<int>>& edges, int root)
            : v(vertices), w(costs), e(edges), r(root) {}
    };

    void dfs(T& tree, vector<Dp>& DP, int v) {
        //cout << "Visited node " << v << endl;
        const long long INFINITE = 9223372036854775807;
        
        // Base case:
        long long pick = tree.w[v];
        long long skip_above = 0;
        long long skip_below;
    
        // If the node is a leaf:
        if (tree.e[v].empty()) {
            skip_below = INFINITE;  // Picking the node below is  not allowed, as it does not exist
            // Cost is the node's cost, or the cost of the node above
            DP[v] = Dp(pick, skip_above, skip_below);
            return;
        }
    
        // If the node is not a leaf:
        for (int c : tree.e[v]) {
            // Recursively dfs so that every node below is processed
            dfs(tree, DP, c);
    
            // Since we are looking for both dominant and independent set, if we pick a node then we can't pick any of its children
            // pick is therefore the sum of skipping every child
            pick += DP[c].skip_above;
    
            // If we skip the current node, then child must either be picked or dominated from below
            skip_above += min(DP[c].pick, DP[c].skip_below);
        }
    
        // We consider every child node as a possible dominator of the current node being processed:
        skip_below = INFINITE;
        for (int dom : tree.e[v]) {
            long long cost = DP[dom].pick;
    
            // If a child node dominates v, then every other child of v must either be picked or dominated by one of its children
            for (int c : tree.e[v]) {
                if (c == dom) {
                    continue;
                }
                // Sum up the cost for each dominator 
                cost += min(DP[c].pick, DP[c].skip_below);
            }
            // Store the value as skip_below if it's cheaper than picking the current node
            skip_below = min(skip_below, cost);
        }
    
        DP[v] = Dp(pick, skip_above, skip_below);
    }

int main() {
    int n;
    cin >> n;
    vector<vector<int>> children(n);
    vector<long long> cost_list(n);
    vector<bool> has_parent(n, false);
    vector<int> nodes;
    for (int x = 0; x<n; x++) {
        nodes.push_back(x);
    }

    for (int employee = 0; employee<n; employee++) {
        cin >> cost_list[employee];

        int subordinate_count;
        cin >> subordinate_count;

        for (int x=0; x<subordinate_count;x++) {
            int subordinate;
            cin >> subordinate;
            children[employee].push_back(subordinate);
            has_parent[subordinate] = true;
        }
    }
    // Might theoretically be none, but not in this case
    int root = -1;
    for (int i = 0; i < n; ++i) {
        if (!has_parent[i]) {
            root = i;
            break;
        }
    }

    vector<Dp> DP(n);
/*
    for (vector<int> x:children) {
        for (int y:x) {
            cout << y << ' ';
        }
        cout << endl;
    }
*/
    // Construct the tree object
    T tree(nodes, cost_list, children, root);

    // Do DFS from the root node
    dfs(tree, DP, root);

    // Print minimum of picking root node/skipping and picking child
    cout << min(DP[root].pick, DP[root].skip_below) << endl;

    return 0;

}