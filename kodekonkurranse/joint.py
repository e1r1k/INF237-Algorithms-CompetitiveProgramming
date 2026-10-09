import math as m

def euclidean(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    return m.sqrt((x2-x1) **2 + (y2-y1) ** 2)
    
def main():
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    print(max(euclidean((x1, y1), (x2, y2)), euclidean((x3,y3), (x4, y4))))

main()