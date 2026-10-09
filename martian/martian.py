import sys

input = list(map(lambda x: x.split(), sys.stdin.read().strip().split('\n')))
n =  int(input[0][0])
k = int(input[0][1])
r = int(input[0][2])
strand = [int(x) for x in input[1]]
input = input[2:]

count = {x:0 for x in range(k)} 

required_keys = []
for x in input:
    required_keys.append(int(x[0]))
    count[int(x[0])] = int(x[1])

index = 0
while (r > 0):
    if index >= n:
        print("impossible")
        exit()
    count[strand[index]] -= 1
    if count[strand[index]] == 0 and strand[index] in required_keys:
        r -= 1
    index += 1

smallest = index
for x in range(n):
    if count[strand[x]] > 0 and strand[x] in required_keys:
        print(smallest)
        break
    count[strand[x]] += 1
    smallest -= 1
    