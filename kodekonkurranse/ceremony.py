import sys

data = map(int, sys.stdin.read().split())
it = iter(data)

n = next(it)
input = []
for _ in range(n):
    input.append(next(it))
input.sort()
    
ops = 0
floors_destroyed = 0
while n > 0:
    if n < input[-1]:
        input.pop(-1)
        n -= 1
    else:
        floors_destroyed += 1
        while (input[0] - floors_destroyed == 0):
            input.pop(0)
            n -= 1
            if n == 0:
                break
    ops += 1
print(ops)

