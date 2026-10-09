#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>

using namespace std;

struct Point {
    double x, y;
};

struct Solution {
    double delta_squared;  
    pair<Point, Point> pts;
};

bool comp_X(const Point& p1, const Point& p2) {
    if (p1.x != p2.x) {
        return p1.x < p2.x;}
    else {return p1.y < p2.y;}
}

bool comp_Y(const Point& p1, const Point& p2) {
    if (p1.y != p2.y) {return p1.y < p2.y;}
    else {return p1.x < p2.x;}
}

double dist_squared(const Point& p1, const Point& p2) {
    return (p1.x - p2.x) * (p1.x - p2.x) + 
           (p1.y - p2.y) * (p1.y - p2.y);
}

Solution bruteforce(const vector<Point>& points) {
    double min_dist = numeric_limits<double>::max();
    pair<Point, Point> best_pair;
    int n = points.size();

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            double d = dist_squared(points[i], points[j]);
            if (d < min_dist) {
                min_dist = d;
                best_pair = {points[i], points[j]};
            }
        }
    }

    return {min_dist, best_pair};
}

Solution compute_strip(vector<Point> strip, double delta_squared) {
    sort(strip.begin(), strip.end(), comp_Y);  
    double best = delta_squared;
    pair<Point, Point> best_pair;

    for (size_t i = 0; i < strip.size(); i++) {
        for (size_t j = i + 1; j < strip.size() && (strip[j].y - strip[i].y) * (strip[j].y - strip[i].y) < best; j++) {
            double d = dist_squared(strip[i], strip[j]);
            if (d < best) {
                best = d;
                best_pair = {strip[i], strip[j]};
            }
        }
    }

    return {best, best_pair};
}

Solution closest_pair(vector<Point>& X, vector<Point>& Y) {
    int n = X.size();
    if (n <= 18)
        return bruteforce(X);

    int pivot = n / 2;
    double mid_x = X[pivot].x;

    vector<Point> Xl(X.begin(), X.begin() + pivot);
    vector<Point> Xr(X.begin() + pivot, X.end());

    vector<Point> Yl, Yr;
    for (const Point& p : Y) {
        if (p.x <= mid_x)
            Yl.push_back(p);
        else
            Yr.push_back(p);
    }

    Solution leftSol = closest_pair(Xl, Yl);
    Solution rightSol = closest_pair(Xr, Yr);

    Solution best;
    if (leftSol.delta_squared < rightSol.delta_squared) {best = leftSol;} 
    else {best = rightSol;}

    vector<Point> strip;
    for (const Point& p : Y) {
        if ((p.x - mid_x) * (p.x - mid_x) < best.delta_squared)
            strip.push_back(p);
    }

    if (strip.size() > 1) {
        Solution stripSol = compute_strip(strip, best.delta_squared);
        if (stripSol.delta_squared < best.delta_squared)
            best = stripSol;
    }

    return best;
}

Solution closest(const vector<Point>& points) {
    vector<Point> X = points;
    vector<Point> Y = points;

    sort(X.begin(), X.end(), comp_X);
    sort(Y.begin(), Y.end(), comp_Y);
    return closest_pair(X, Y);
}

int main() {
    int n;
    cin >> n;
    while (n > 0) {
        vector<Point> points(n);
        for (int i = 0; i < n; i++) {
            cin >> points[i].x >> points[i].y;
        }

        Solution sol = closest(points);
        pair<Point, Point> pts = sol.pts;
        Point p1 = pts.first;
        Point p2 = pts.second;

        cout << p1.x << ' ' << p1.y << ' ' << p2.x << ' ' << p2.y  << endl;

        cin >> n;
    }
}