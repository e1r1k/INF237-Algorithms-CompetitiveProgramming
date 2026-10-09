import math
import sys

data = map(float, sys.stdin.read().split())
it = iter(data)
case_count = int(next(it))

def euclidean(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    return math.sqrt((x2-x1) **2 + (y2-y1) ** 2)

def compute_centers(point1, point2, diameter):
    (x1, y1) = point1
    (x2, y2) = point2
    r = diameter / 2

    distance = abs(euclidean((x1, y1), (x2, y2)))
    (x3, y3) = (((x1+x2) / 2, (y1 + y2) / 2)) # Midpoint 

    # Theoretical possible centers of circle can be found using pythagorean theorem where radius is the hypotenuse and edge from
    # one mosquito to the midpoint is one (cathetus?)
    a = abs(euclidean((x1, y1), (x3, y3)))
    c = r
    b = math.sqrt(c**2 - a**2)

    # To get the actual vector, we rotate the vector (x2-x1, y2-y1) by 90 degrees by swapping x and y and negating one
    # Then we divide by distance to get a unit vector, and scale by the "unknown" cathetus, and add it to the midpoint
    #         |            X             |              Y              |
    center1 = (x3 + b*(y1-y2) / distance, y3 + b * (x2 - x1) / distance)
    center2 = (x3 - b*(y1-y2) / distance, y3 + b * (x2 - x1) / distance)
    return (center1, center2)


# For any cluster of mosquitoes, there will be two mosquitoes that, if used as edge points for a circle, will encompass
# the whole cluster - or at least as much as the circle size will allow.
def solve_case():
    m = int(next(it))
    diameter = next(it)
    r = diameter/2

    if diameter == 0:
        print(0)
        return
    if m == 1:
        print(1)
        return

    mosquitos = []
    for x in range(m):
        mosquitos.append((next(it), next(it)))
    
    max_mosq = 0
    for i in range(m):
        for j in range(i+1, m):
            (x1, y1) = mosquitos[i]
            (x2, y2) = mosquitos[j]
            distance = abs(euclidean((x1, y1), (x2, y2)))

            # If the distance between mosquitos is larger than diameter of the circle, they are unusable
            if distance > diameter:
                continue
            
            if distance == 0:
                (center1, center2) = ((x1, y1), (x1, y1))
            else:
                (center1, center2) = compute_centers((x1, y1), (x2, y2), diameter)
            sum1 = 0
            sum2 = 0

            # For each theoretical center, check distance to all mosquitos and take max of observed max and the two centers
            for mosquito in mosquitos:
                if euclidean(mosquito, center1) <= r:
                    sum1 += 1
                if euclidean(mosquito, center2) <= r:
                    sum2 += 1
            
            max_mosq = max(max_mosq, sum1, sum2)
    print(max_mosq)

for x in range(case_count):
    solve_case()


