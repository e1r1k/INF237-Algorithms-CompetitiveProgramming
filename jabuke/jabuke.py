import sys

data = map(int, sys.stdin.read().split())
it = iter(data)

a = (next(it), next(it))
b = (next(it), next(it))
c = (next(it), next(it))

# Compute the area of triangle
def triangle_area(h, i, j):
    return abs((h[0]*(i[1]-j[1]))+(i[0]*(j[1]-h[1]))+(j[0]*(h[1]-i[1]))) / 2

# Create list of trees on the (x, y) form
n_trees = next(it)
trees = []
for x in range(n_trees):
    trees.append((next(it), next(it)))

# Land size is the area of original three points
land_size = triangle_area(a, b, c)
owned_trees = 0
for tree in trees:
    # We use the point to partition the triangle into three smaller triangles. If the sum of these is exactly equal to 
    # the triangle from the original three coordinates, then the point is within the triangle.
    # If it is larger or smaller, then it is outside.
    if ((triangle_area(tree, b, c) + triangle_area(a, tree, c) + triangle_area(a, b, tree)) == land_size):
        owned_trees += 1
    
print(land_size, '\n', owned_trees)



# First intuition was creating three triangles and checking if they were all smaller. That does not really make sense, but
# this approach should work.