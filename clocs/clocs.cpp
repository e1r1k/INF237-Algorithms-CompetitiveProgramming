#include <iostream>
#include<algorithm>
#include <vector>

using namespace std;

int mod(int a, int m) {
    return (a % m + m) % m;
}

int main() {
    int n;
	cin >> n;
    vector<int> clock_a;
    vector<int> clock_b;
    
    for (int x=0; x < n; x++) {
            int hand;
            cin >> hand;
            clock_a.push_back(hand);
        }
    for (int x=0; x < n; x++) {
            int hand;
            cin >> hand;
            clock_b.push_back(hand);
        }
    
    sort(clock_a.begin(), clock_a.end());
    sort(clock_b.begin(), clock_b.end());
    vector<int> clock_diffs_a;
    vector<int> clock_diffs_b;

    for (int x=0;x<n;x++) {
        clock_diffs_a.push_back(mod(clock_a[x] - clock_a[(x - 1 + n) % n], 360000));
        clock_diffs_b.push_back(mod(clock_b[x] - clock_b[(x - 1 + n) % n], 360000));
    }

    clock_diffs_a.insert(clock_diffs_a.end(), clock_diffs_a.begin(), clock_diffs_a.end());

    bool is_rotation = false;
    for (int i = 0; i < n; ++i) {
        bool match = true;
        for (int j = 0; j < n; ++j) {
            if (clock_diffs_a[i + j] != clock_diffs_b[j]) {
                match = false;
                break;
            }
        }
        if (match) {
            is_rotation = true;
            break;
        }
    }

    if (is_rotation) {
        cout << "possible";
    }
    else {
        cout << "impossible";
    }
	return 0;
}

