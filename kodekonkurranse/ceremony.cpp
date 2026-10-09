#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    long long n;
    cin >> n;

    vector<long long> input;
    for (int x = 0; x < n; x++) {
        long long b;
        cin >> b;
        input.push_back(b);
    }
    sort(input.begin(), input.end());
    long long ops = 0;
    long long floors_destroyed = 0;
    while (n > 0) {
        if (n < input.back()) {
            input.erase(input.end());
            n -= 1;
        }
        else {
            floors_destroyed += 1;
            while (input[0] - floors_destroyed  == 0) {
                input.erase(input.begin());
                n -= 1;
                if (n == 0) {
                    break;
                }

            }
        }
        ops += 1;
    }
    cout << ops;
    return 0;
}