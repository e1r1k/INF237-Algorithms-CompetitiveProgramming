import sys
from collections import deque

input = list(map(lambda x: x.split(), sys.stdin.read().strip().split('\n')))
n = int(input[0][0])
k = int(input[0][1])
heights = list(map(int, input[1]))
min_diff = 100

tallest = deque([0])
shortest = deque([0])

# Make start-window
for x in range(1, k):
    # If a big value enters the queue, then all smaller values befoore will never result in new max
    while tallest and (heights[x] > heights[tallest[-1]]):
        #print(heights[x], " is bigger than ", heights[tallest[-1]], ". Popping last element")
        tallest.pop()
    tallest.append(x)
    # Minimum is the same
    while shortest and (heights[x] < heights[shortest[-1]]):
        #print(heights[x], " is smaller than ", heights[shortest[-1]], ". Popping last element")
        shortest.pop()
    shortest.append(x) 
#print(f"Min diff: Tallest, {heights[tallest[0]]} - shortest, {heights[shortest[0]]} vs. {min_diff} = {min(heights[tallest[0]]-heights[shortest[0]], min_diff)}")
min_diff = min(heights[tallest[0]] - heights[shortest[0]], min_diff)

# Process the rest of the array as sliding window, same principle
for x in range(k,n):
    if tallest[0] < x - (k-1):
        tallest.popleft()
    if shortest[0] < x - (k-1):
        shortest.popleft()
    while tallest and heights[x] > heights[tallest[-1]]:
        tallest.pop()
    tallest.append(x)
    while shortest and heights[x] < heights[shortest[-1]]:
        shortest.pop()
    shortest.append(x) 
    min_diff = min(heights[tallest[0]] - heights[shortest[0]], min_diff)

print(min_diff)
