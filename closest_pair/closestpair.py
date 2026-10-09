import math
import itertools as IT
from collections import namedtuple as T

Point = T("Point", "x y")
Sol = T("Sol", "delta pair")
def dist(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)
def bruteforce(points):
    return min(Sol(dist(a, b), (a, b)) for (a, b) in IT.combinations(points, 2))
def compute_strip(points):
    return min(bruteforce(IT.islice(points[i:], 6)) for i in range(len(points) - 1))

def closest(points):
    X = sorted(points)
    Y = sorted(points, key=lambda p: (p.y, p.x))
    return closest_pair(X, Y)

def closest_pair(X, Y):
    if len(X) <= 18:
        return bruteforce(X)
    pivot = len(X) // 2
    Xl = [p for (i, p) in enumerate(X) if i < pivot] # N/2 many points on the left
    L = set(Xl) # expected O(1) lookup
    Xr = [p for p in X if p not in L]
    Yl = [p for p in Y if p in L]
    Yr = [p for p in Y if p not in L]
    OPT = min(closest_pair(Xl, Yl), closest_pair(Xr, Yr))
    line = X[pivot].x
    S = [p for p in Y if abs(p.x - line) < OPT.delta]
    if len(S) > 1:
        OPT = min(OPT, compute_strip(S))
    return OPT

def solve():
    points = []
    n = int(input())
    for _ in range(n):
        x, y = map(float, input().split())
        points.append(Point(x, y))
    a, b = closest(points).pair
    print(a.x, " ", a.y, " ", b.x, " ", b.y, )

try:
    while True:
        solve()
except:
    exit()