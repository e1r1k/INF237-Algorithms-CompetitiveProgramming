n = int(input())
clock_a = [int(x) for x in input().split()]
clock_b = [int(x) for x in input().split()]

clock_a.sort()
clock_b.sort()

clock_a_diffs = []
clock_b_diffs = []
for x in range(n):
    clock_a_diffs.append((clock_a[x] - clock_a[x-1]) % 360000)
    clock_b_diffs.append((clock_b[x] - clock_b[x-1]) % 360000)

clock_a_diffs = clock_a_diffs + clock_a_diffs

def longest_prefix_suffix(pattern):
    n, k = 0, len(pattern)
    lps = [0] * k
    idx = 1
    while idx < k:
        if pattern[idx] == pattern[n]:
            n += 1
            lps[idx] = n
            idx += 1
        else:
            if n != 0:
                n = lps[n - 1]
            else:
                lps[idx] = 0
                idx += 1
    return lps

def kmp(text, pattern, lps):
    n, k = len(text), len(pattern)
    txt_idx, pat_idx = 0, 0
    while txt_idx < n:
        if pattern[pat_idx] == text[txt_idx]:
            txt_idx += 1 
            pat_idx += 1
        if pat_idx == k:
            return True

        elif txt_idx < n and pattern[pat_idx] != text[txt_idx]:
            if pat_idx != 0:
                pat_idx = lps[pat_idx - 1]
            else:
                txt_idx += 1 
    return False

lps = longest_prefix_suffix(clock_b_diffs)
if kmp(clock_a_diffs, clock_b_diffs, lps):
    print("possible")
else:
    print("impossible")

"""
clock_a_diffs = []
clock_b_diffs = []
for x in range(n):
    clock_a_diffs.append((clock_a[x] - clock_a[x-1]) % 360000)
    clock_b_diffs.append((clock_b[x] - clock_b[x-1]) % 360000)

clock_a_diffs = clock_a_diffs + clock_a_diffs

for x in range(n):
    if clock_a_diffs[x:x+n] == clock_b_diffs:
        print("possible")
        exit()
print("impossible")





clock_a = clock_a + clock_a  

for x in range(n):
    bad_diff = False
    for y in range(x, x+n):
        if (clock_a[y] - clock_a[y-1]) % 360000 != (clock_b[y-x] - clock_b[y-x-1]) % 360000:
            bad_diff = True
            break
    if not bad_diff:
        print("possible")
        exit()
print("impossible")
"""