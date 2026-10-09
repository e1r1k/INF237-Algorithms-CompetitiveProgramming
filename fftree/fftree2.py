from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

def sieve(n):
    prime = [False] * n
    prime[0] = prime[1] = 0
    for i in range(2, n):
        if not prime[i]:
            for j in range(i, n, i):
                if prime[j] == 0:
                    prime[j] = i
    return prime

n = int(input())
if n == 1:
    print("0")
    exit()
inorder_array = list(map(int, input().split()))

max_val = max(inorder_array)
primes = sieve(max_val+1)
parent_dict = {}

def get_prime_factors(x):
    factors = set()
    while x > 1:
        factors.add(primes[x])
        x //= primes[x]
    return factors

def converging_range(left, right):
    for i in range((right - left) + 1):
        if i % 2 == 0:
            yield left + (i // 2)
        else:
            yield right - (i // 2)

def binary_search(x, array):
    n = len(array)
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            left = mid+1
        else:
            right = mid 
    return None

inorder_factors = [get_prime_factors(x)  for x in inorder_array]
factor_indices = defaultdict(list)
for index in range(len(inorder_array)):
    for fac in inorder_factors[index]:
        factor_indices[fac].append(index)

def check_subtree(left, right):
    if left > right:
        return None
    for i in converging_range(left, right):
        facs = get_prime_factors(inorder_array[i])
        valid_i = True

        for fac in facs:
            indices = factor_indices[fac]
            fac_indx = binary_search(i, indices)
            if fac_indx is not None:
                if fac_indx > 0:
                    left_neighbor = indices[fac_indx - 1]
                    if left_neighbor >= left and left_neighbor <= right:  
                        valid_i = False
                        break
                if fac_indx < len(indices) - 1:
                    right_neighbor = indices[fac_indx + 1]
                    if right_neighbor >= left and right_neighbor <= right:
                        valid_i = False
                        break

        if valid_i:
            left_child = check_subtree(left, i - 1)
            right_child = check_subtree(i + 1, right)
            if left_child is not False:
                if left_child is not None:
                    parent_dict[left_child] = i
                if right_child is not False:
                    if right_child is not None:
                        parent_dict[right_child] = i
                    return i  
    return False  


root = check_subtree(0, n - 1)
if root is False:
    print("impossible")
else:
    parent_dict[root] = -1 
    for key in sorted(parent_dict.keys()):
        print(parent_dict[key]+1, end=" ")
