import sys

input = list(map(lambda x: int(x), sys.stdin.read().strip().split('\n')))
n = input[0]
costs = input[1:]

matrix = [[float('inf')] * (2*n) for x in range(n)]
matrix[0][0] = 0

for i in range(1, n):
    for j in range(n-1, -1, -1):
        matrix[i][j] = (min([matrix[i-1][j-i], matrix[i][j+i]])) + costs[j]
        
nv = [row[n-1] for row in matrix]
print(min(nv))
