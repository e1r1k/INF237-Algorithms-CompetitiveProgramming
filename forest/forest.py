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

def edges(P):
    return list(zip(P, P[1:])) + [(P[-1], P[0])]

def inside(vertex, edge):
    if orient(edge[0], edge[1], vertex) < 0:
        return True
    return False

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
    return hull

def line_intersection(edge1, edge2):
    edge1_s, edge1_e = edge1
    edge2_s, edge2_e = edge2
    # Adjust vectors to origo
    dx1, dy1 = edge1_e.x - edge1_s.x, edge1_e.y - edge1_s.y
    dx2, dy2 = edge2_e.x - edge2_s.x, edge2_e.y - edge2_s.y
    #Determinant = 0 means lines do not intersect, break function (will never happen in this case)
    determinant = dx1 * dy2 - dy1 * dx2
    if determinant == 0: 
        return None 

    relative_intsec_p = ((edge2_s.x - edge1_s.x) * dy2 + (edge1_s.y - edge2_s.y) * dx2) / determinant
    abs_intsec_p = edge1_s.x + relative_intsec_p * dx1, edge1_s.y + relative_intsec_p * dy1
    return abs_intsec_p

def solve():
    P, A = list(map(int, input().split()))
    pines = []
    aspens = []
    for _ in range(P):
        x, y = map(float, input().split())
        pines.append(Vec(x, y))
    for _ in range(A):
        x, y = map(float, input().split())
        aspens.append(Vec(x, y))
    
    p_polygon = graham(pines)
    a_polygon = graham(aspens)
    a_edges = edges(a_polygon)
    p_edges = edges(p_polygon)

    intersection = []

    for indx in range(len(a_polygon)):
        start = a_polygon[indx-1]
        end = a_polygon[indx]
        end_inside = True
        start_inside = True
        print("Considering vertices (start, ", start, "), (end, ", end)
        for edge in p_edges:
            if inside(end, edge):
                pass
            else:
                end_inside = False
                break
            if inside(start, edge):
                pass
            else:
                start_inside = False
                break
        if end_inside:
            print(end, " is inside the polygon.")
            if not start_inside:
                print(start, " is NOT inside the polygon - adding end vertex", end, " and intersection point", line_intersection((start, end), edge))
                intersection.append(line_intersection((start, end), edge))
            intersection.append(end)
        elif start_inside:
            print("Start vertex IS inside the polygon, end is not. Adding intersection point ", line_intersection((start, end), edge))
            intersection.append(line_intersection((start, end), edge))
    print(intersection)

solve()




