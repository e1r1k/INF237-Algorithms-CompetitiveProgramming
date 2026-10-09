from collections import defaultdict
import bisect
import sys

def sieve(n):
    spf = list(range(n)) 
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def get_prime_factors(x, spf):
    factors = set()
    while x > 1:
        factors.add(spf[x])
        x //= spf[x]
    return factors

def converging_range(left, right):
    for i in range(right - left + 1):
        if i % 2 == 0:
            yield left + i // 2
        else:
            yield right - i // 2

def build_tree_stack(n, inorder_array):
    max_val = max(inorder_array)
    spf = sieve(max_val + 2)

    inorder_factors = [get_prime_factors(x, spf) for x in inorder_array]

    factor_indices = defaultdict(list)
    for idx, factors in enumerate(inorder_factors):
        for f in factors:
            factor_indices[f].append(idx)

    parent_dict = {}
    stack = [(0, n - 1, -1)]  

    while stack:
        left, right, parent = stack.pop()
        if left > right:
            continue

        found = False
        for i in converging_range(left, right):
            valid = True
            for fac in inorder_factors[i]:
                indices = factor_indices[fac]
                pos = bisect.bisect_left(indices, i)
                if pos > 0 and left <= indices[pos - 1] <= right:
                    valid = False
                    break
                if pos + 1 < len(indices) and left <= indices[pos + 1] <= right:
                    valid = False
                    break
            if valid:
                parent_dict[i] = parent
                stack.append((i + 1, right, i))
                stack.append((left, i - 1, i))
                found = True
                break

        if not found:
            return None 

    return parent_dict



n = int(input())
if n == 1:
    print("0")
    exit()
inorder_array = list(map(int, input().split()))

parent_dict = build_tree_stack(n, inorder_array)

if parent_dict is None:
    print("impossible")
else:
    result = [-1] * n
    for child, parent in parent_dict.items():
        result[child] = parent + 1
    print(" ".join(map(str, result)))