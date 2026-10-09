#include <iostream>
#include <vector>

using namespace std;

int left(int n) {return (2*n);}
int right(int n) {return 2*n + 1;}
int parent(int n) {return n / 2;}
int index(vector<int>& T, int n) {return T.size() / 2 + n;}
void fill(vector<int>& T) {
    vector<int> parents;
    for (int x = (T.size() / 2)-1; x > 0; x--) {
        parents.push_back(x);
    }
    for (int index : parents) {
        T[index] = (T[left(index)] + T[right(index)]);
    }
}
int query(const vector<int>& T, int l, int r) {
    int result = 0;
    while (l <= r) {  
        if (l % 2 == 1) result += T[l++]; // If l is right child, include it and "jump branches"
        if (r % 2 == 0) result += T[r--]; // If r is left child, include it and "jump branches"
        l = parent(l);
        r = parent(r);
    }

    return result;
}
void update(vector<int>& T, int index, int value) {
    T[index] = value;
    while (index > 1) {
        index = parent(index);
        T[index] = T[left(index)] + T[right(index)];
    }
}

void solve_case() {
    int m, r;
    cin >> m >> r;
    int top = m;
    vector<int> positions;
    positions.push_back(0);  
    for (int i = m; i > 0; i--) {
        positions.push_back(i);
    }

    vector<int> T((m + r), 0);     
    T.insert(T.end(), m, 1);         
    T.insert(T.end(), r, 0);      
    fill(T);
    
    vector<int> results;
    
    for (int x = 0; x < r; x++) {
        int request;
        cin >> request;

        int movies_on_top = query(T, index(T, positions[request]), index(T, top));
        update(T, index(T, top), 1);
        update(T, index(T, positions[request]-1), 0);
        top += 1;
        positions[request] = top;

        cout << movies_on_top << ' ';
    }
    cout << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int case_count;
    cin >> case_count;

    for (int x = 0; x < case_count; x++) {
        solve_case();
    }

    return 0;
}



