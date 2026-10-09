import sys

data = map(int, sys.stdin.read().split())
it = iter(data)

n = next(it)
pushes = []
for _ in range(n):
    pushes.append(next(it))

push_count = 0
dirtiness = 0
cleans = 0

for day in range(366):
    dirtiness += push_count

    if dirtiness == 20:
        cleans += 1
        push_count = 0
        dirtiness = 0
    elif dirtiness > 20:
        cleans += 1
        push_count = 1 if (day-1) in pushes else 0
        dirtiness = push_count
    
    if day in pushes:
        push_count += 1

if dirtiness > 0:
    cleans += 1

print(cleans)


        
    
    
    