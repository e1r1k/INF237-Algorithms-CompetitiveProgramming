import sys

input = list(map(lambda x: x.split(), sys.stdin.read().strip().split('\n')))
t = int(input[0][0])
sizes = [list(map(int, x)) for x in input[2::2]]
sizes = list(map(lambda x: (list(zip(x[::2], x[1::2]))), sizes))
dolls =list(map(lambda x: int(x[0]), input[1::2]))
cases = list(zip(dolls, sizes))

def solve_case(case):
    sizes = case[1]
    sizes.sort(key = lambda x: (x[0], -x[1]))

    stacks = []

    for doll in sizes:
        stacked = False
        for i in stacks:
            if i[-1][0] < doll[0] and i[-1][1] < doll[1]:
                stacked = True
                i.append(doll)
                break
        if not stacked:
            stacks.append([doll])

    print(stacks)
    return len(stacks)

for x in cases:
    print(solve_case(x))
