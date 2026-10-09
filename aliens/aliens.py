def rabin_karp(s, min_count):
    A = 3
    B = 97
    n = len(s)

    def check(length):
        h = 0
        base_l = pow(A, length, B)
        hashes = {}
        result_index = -1

        for i in range(length):
            h = (h * A + ord(s[i])) % B
        hashes[h] = [0]

        for i in range(1, n - length + 1):
            h = (h * A - ord(s[i - 1]) * base_l + ord(s[i + length - 1])) % B
            h = (h + B) % B  # ensure non-negative

            if h in hashes:
                hashes[h].append(i)
                if len(hashes[h]) == min_count:
                    # First time we've reached `min_count` -> candidate
                    nonlocal_best[0] = i
            else:
                hashes[h] = [i]

        # Return True if we found a valid hash
        return nonlocal_best[0] != -1

    low, high = 0, n
    best_len = 0
    best_index = -1

    while low <= high:
        mid = (low + high) // 2
        nonlocal_best = [-1]  # track best index found for this length
        if check(mid):
            best_len = mid
            best_index = nonlocal_best[0]
            low = mid + 1
        else:
            high = mid - 1

    return best_len, best_index


n = int(input())
while n:
    s = input()
    length, pos = rabin_karp(s, n)
    if length > 0:
        print(length, pos)
    else:
        print("none")
    n = int(input())