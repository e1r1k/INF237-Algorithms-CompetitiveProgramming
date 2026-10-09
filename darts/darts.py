import math

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def cross(v1, v2):
        return v1.x * v2.y - v1.y * v2.x
    def __sub__(v1, v2):
        return Vec(v1.x - v2.x, v1.y - v2.y)
    def __mul__(v, scalar):
        return Vec(v.x * scalar, v.y * scalar)
    def __repr__(v):
        return f"Vec{(v.x, v.y)}"

def orient(a, b, c):
    return (b - a).cross(c - a)

def dist(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

def leftturn(p1, p2, p3):
    return orient(p1, p2, p3) > 0

def graham(points):
    S, hull = [], [] 
    for p in points:
        while len(S) >= 2 and leftturn(S[-2], S[-1], p):
            S.pop()
        S.append(p)
    hull += S
    S = []
    for p in reversed(points):
        while len(S) >= 2 and leftturn(S[-2], S[-1], p):
            S.pop()
        S.append(p)
    hull += S[1:-1]
    circ = 0
    for x in range(len(hull)):
        circ += dist(hull[x-1], hull[x])
    return 100 * len(points) / (1+circ)

def solve():
    data = list(map(float, input().split()))
    points = []
    for x in range(0, len(data), 2):
        points.append((data[x], data[x+1]))
        
    points.sort()
    vecs = []
    for point in points:
        vecs.append(Vec(point[0], point[1]))
    
    return graham(vecs)

try:
    while True:
        print(solve())
except:
    exit()



