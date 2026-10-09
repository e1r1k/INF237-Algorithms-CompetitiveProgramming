
n, k, q = map(int, input().split())

def parent(index):
    return ((index-2)//k) + 1

for x in range(q):
    x, y = map(int, input().split())
    steps = 0
    while x != y:
        steps += 1
        if x < y:
            y = parent(y)
        elif y < x:
            x = parent(x)

    print(steps)
