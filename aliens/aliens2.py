from collections import defaultdict

def check_length(str, length, count):
    hashes = defaultdict(list)
    A = 73
    B = 100000000000
    n = len(text)
    
    h = 0
    first_mult = pow(A, length - 1, B) 
    for i in range(length):
        h = (h * A + ord(text[i])) % B
    hashes[h].append(0)
    
    for i in range(1, n - length + 1):
        left_char = ord(text[i - 1])
        right_char = ord(text[i + length - 1])
        
        h = (h - left_char * first_mult) % B
        h = (h * A + right_char) % B
        hashes[h].append(i)

    rightmost = -1
    for positions in hashes.values():
        if len(positions) >= count:
            rightmost = max(rightmost, positions[-1])  

    if rightmost == -1:
        return None
    return (length, rightmost)


def solve(n, text):
    left = 1
    right = len(text) + 1
    best = -1
    while left < right:
        mid = (left + right) // 2
        sol = check_length(text, mid, n)
        if sol:
            best = sol 
            left = mid + 1
        else:
            right = mid 
    return best

n = int(input())
while n != 0:
    text = input()
    sol = solve(n, text)
    if sol != -1:
        print(sol[0], sol[1])
    else:
        print("none")
    n = int(input())



