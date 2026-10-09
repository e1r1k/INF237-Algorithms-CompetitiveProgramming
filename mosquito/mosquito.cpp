#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

float euclidean(vector<float> point1, vector<float> point2) {
    float x1 = point1[0];
    float y1 = point1[1];
    float x2 = point2[0];
    float y2 = point2[1];
    float dist = sqrt(((x2-x1) * (x2-x1)) + ((y2-y1) * (y2-y1)));
    return dist;
}

vector<vector<float>> compute_centers(vector<float> point1, vector<float> point2, float d) {
    float x1 = point1[0];
    float y1 = point1[1];
    float x2 = point2[0];
    float y2 = point2[1];
    float r = d / 2;
    float distance = fabs(euclidean(point1, point2));
    float x3 =  (x1+x2) / 2;
    float y3 = (y1 + y2) / 2;

    float a = fabs(euclidean({x1, y1}, {x3, y3}));
    float c = r;
    float b = sqrt(c*c - a*a);

    vector<float> center1 = {x3 + b*(y1-y2) / distance, y3 + b * (x2 - x1) / distance};
    vector<float> center2 = {x3 - b*(y1-y2) / distance, y3 + b * (x2 - x1) / distance};
    return {center1, center2};
}

void solve_case() {
    float  m, d;
    cin >> m >> d;
    
    float r = d/2;

    if (m == 1) {
        cout << 1;
        return;
    }

    vector<vector<float>> mosquitos;
    for (int a = 0; a < m; a++) {
        float x, y;
        cin >> x >> y;
        mosquitos.push_back({x, y});
    }

    long long max_mosq = 1;

    for (int i = 0; i < m; i++) {
        for (int j = i+1; j < m; j++) {
            float x1 = mosquitos[i][0];
            float y1 = mosquitos[i][1];
            float x2 = mosquitos[j][0];
            float y2 = mosquitos[j][1];

            vector<float> center1;
            vector<float> center2;
            float distance = fabs(euclidean({x1, y1}, {x2, y2}));
            if (distance == 0) {
                center1 = {x1, y1};
                center2 = {x2, y2};
            }
            else {
                vector<vector<float>> centers = compute_centers({x1, y1}, {x2, y2}, d);
                center1 = centers[0];
                center2 = centers[1];
            }

            long long sum1 = 0;
            long long sum2 = 0;
            long long best_center = 0;
            
            for (vector<float> mosquito : mosquitos) {
                if ((euclidean(mosquito, center1) - r) <= 1e-6) {
                    sum1 += 1;
                }
                if ((euclidean(mosquito, center2) - r) <= 1e-6) {
                    sum2 += 1;
                }
            }
            best_center = max(sum1, sum2);
            max_mosq = max(max_mosq, best_center);
        }
    }
    cout << max_mosq << endl;
}


int main() {
    int case_count;
    cin >> case_count;
    for (int x = 0; x < case_count; x++) {
        solve_case();
    }
}