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
inorder_array = list(map(int, input().split()))
max_val = max(inorder_array)
primes = sieve(max_val+1)
parent_dict = {}

def iter_sides(left, right):
    for i in range((right - left) + 1):
        if i % 2 == 0:
            yield left + (i // 2)
        else:
            yield right - (i // 2)

def get_prime_factors(x):
    factors = set()
    while x > 1:
        factors.add(primes[x])
        x //= primes[x]
    return factors

def check_subtree(left, right, used_primes):
    if left > right:
        return None 

    for i in iter_sides(left, right):
        val = inorder_array[i]
        prime_factors_i = get_prime_factors(val)

        if prime_factors_i.isdisjoint(used_primes):
            left_child = check_subtree(left, i - 1, used_primes.union(prime_factors_i))
            right_child = check_subtree(i + 1, right, used_primes.union(prime_factors_i))
            
            if left_child is not False:
                if left_child is not None:
                    parent_dict[left_child] = i
                if right_child is not False:
                    if right_child is not None:
                        parent_dict[right_child] = i
                    return i  
    return False  

root = check_subtree(0, n - 1, set())
if not root:
    print("impossible")
else:
    parent_dict[root] = -1 
    for key in sorted(parent_dict.keys()):
        print(parent_dict[key]+1, end=" ")