import math
import sys

data = map(int, sys.stdin.read().split())
it = iter(data)

case_count = next(it)

def shoelace(poly):
    N = len(poly)
    fw = sum(poly[i - 1][0] * poly[i][1] for i in range(N))
    poly = list(reversed(poly))
    bw = sum(poly[i - 1][0] * poly[i][1] for i in range(N))
    return abs(fw - bw) / 2.0

# Returns True if numbers k and l are both positive/both negative, else False
def sgn2(k, l): 
    return k * l < 0

# Subtracts x2 from x1 and y2 from y1, for vectors (x1, y1), (x2, y2)
def subtract_vectors(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

# Returns the cross product of two vectors 
def cross_product(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

# Returns a posiitive number if going from a to b to c we turn left, and negative if we turn right.
# This means positive if c is to the left of line (a, b) -> (c, d) and negative if  is to the right
def orient(a, b, c):
    return cross_product((c[0] - a[0], c[1]-a[1]), (b[0] - a[0], b[1]-a[1]))

# Checks if the lines intersect by checking if the end points of lines are on opposite or same sides of other line
# If both lines have the same orientation for both endpoints, None is returned. Else, return the point of intersection
def intersect(line1, line2):
    (a, b), (c, d) = line1, line2
    oa = orient(c, d, a)
    ob = orient(c, d, b)
    oc = orient(a, b, c)
    od = orient(a, b, d)
    if sgn2(oa, ob) and sgn2(oc, od):
        return ((a[0] * ob - b[0] * oa) / (ob - oa), (a[1] * ob - b[1] * oa) / (ob - oa))

def solve_case():
    n = next(it)
    corners = []
    for x in range(n):
        corners.append((next(it), next(it)))

    camera_point = (((corners[0][0] + corners[1][0]) / 2), ((corners[0][1] + corners[1][1]) / 2))
    camera_clockwise_line = (camera_point, corners[0])
    camera_counter_clockwise_line = (camera_point, corners[1])

    line_1 = (camera_point, ((camera_point[0] + math.cos(math.radians(45)))*999999, 
                             (camera_point[1] + math.sin(math.radians(45)))*999999))
    line_2 = (camera_point, ((camera_point[0] + math.cos(math.radians(-45)))*999999, 
                             (camera_point[1] + math.sin(math.radians(-45)))*999999))
    print("Line 1 (left, +45 degrees):", line_1)
    print("Line 2 (right, -45 degrees):", line_2)
    intersect_point_1 = None
    intersect_point_2 = None

    for i in range(len(corners)):
        p1 = corners[i-1]
        p2 = corners[i]  

        x = intersect(line_1, (p1, p2))
        y = intersect(line_2, (p1, p2))
        if x:
            intersect_point_1 = x
        elif y:
            intersect_point_2 = y 

    print("Intersect point 1: ", intersect_point_1)
    print("Intersect point 2: ", intersect_point_2)
    
    visible_corners = []
    for corner in corners:
        if orient(camera_point, intersect_point_1, corner) < 0 and orient(camera_point, intersect_point_2, corner):
            visible_corners.append(p1,p2)

    print(visible_corners)
    
for x in range(case_count):
    solve_case()