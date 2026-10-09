import sys
import math

input = sys.stdin.read().strip().split('\n')
states = list(map(lambda x: [int(x) for x in x.split()], input[1:]))
n = input[0]
temp = []
d = [x[0] for x in states]
total_delegates = sum(d)
max_d = max(d)
constitutional_delegates = 0
federal_delegates = 0
dp =[float('inf')] * max_d + [0] + [float('inf')] * (total_delegates)

for state in states:
    total = sum(state[1:])
    if state[2] < (total / 2):
        cost = int(total/2 - state[1] + 1)
        if  cost > 0:
            temp.append((state[0], cost))
        else:
            temp.append((state[0], 0))
            constitutional_delegates += state[0]
    else:
        federal_delegates += state[0]
states = temp

threshold = math.floor(total_delegates / 2)
if federal_delegates > threshold:
    print('impossible')
    exit()
elif constitutional_delegates > threshold:
    print(0)
    exit()

for state in states:
    for x in range(len(dp)-1, max_d, -1):
        dp[x] = min(dp[x], dp[x - state[0]] + state[1])

solution = min(dp[max_d + threshold+1:])
if solution == float('inf'):
    print("impossible")
else:
    print(solution)
