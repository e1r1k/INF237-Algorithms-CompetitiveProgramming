import sys

input = list(map(lambda x: x.split(), sys.stdin.read().strip().split('\n')))
n =  int(input[0][0])
k = int(input[0][1])
r = int(input[0][2])
strand = list(map(int, input[1]))
input = input[2:]

count = [0] * k
required_keys = set()
for x in input:
    required_keys.add(int(x[0]))
    count[int(x[0])] = int(x[1])

smallest = 200001
index = 0
left = 0

while index < n:
    while r > 0 and index < n:
        count[strand[index]] -= 1
        if count[strand[index]] == 0 and strand[index] in required_keys:
            r -= 1
        index += 1
        if index > n and r > 0:
            print("impossible")
            exit()

    while r == 0 and left <= index:
        if index - left < smallest:
            smallest = index - left
        count[strand[left]] += 1
        if count[strand[left]] == 1 and strand[left] in required_keys:
            r += 1
        left += 1
if smallest == 200001:
    print("impossible")
else:
    print(smallest)
