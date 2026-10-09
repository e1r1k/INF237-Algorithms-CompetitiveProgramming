import sys

input = map(lambda x: x.split(), sys.stdin.read().strip().split('\n'))
input = [(x[0], x[1]) for x in input]

def get_cases(input):
    cases = []
    if len(input) >= 1:
        caseend = int(input[0][1])+1
        cases.append(input[:caseend])
        return cases + get_cases(input[caseend:])
    return []

def dfs(graph, start):
    visited = []
    frontier = [start]
    while len(frontier) > 0:
        current = frontier.pop()
        if current not in visited:
            visited.append(current)
            for i in graph:
                if i[0] == current:
                    frontier.append(i[1])
    return visited

def get_opts(input):
    header = input[0]
    rest = input[1:]
    opts = []
    for i in range(len(rest)):
        copy = rest.copy()
        copy[i] = (copy[i][1], copy[i][0])
        opts.append([header] + copy)
    return opts

def check_validity(input):
    header = input[0]
    if header[0] == 1:
        return True
    elif header[0] == 2:
        return False
    rest = input[1:]
    res = []
    for i in range(int(header[0])):
        if int(header[0]) == len(dfs(rest, str(i))):
            res.append(True)
        else:
            res.append(False)
    return all(res)            

cases = get_cases(input)

for i in range(len(cases)):
    m = int(cases[i][0][0])
    n = int(cases[i][0][1])
    if m == 1:
        print(f"Case {i+1}: valid")
    elif n < m or m == 2:
        print(f"Case {i+1}: invalid")
    elif check_validity(cases[i]):
        print(f"Case {i+1}: valid")
    else:
        opts = get_opts(cases[i])
        invalid = True
        for j in range(len(opts)):
            if check_validity(opts[j]):
                invalid = False
                print(f"Case {i+1}: {cases[i][j+1][0]} {cases[i][j+1][1]}")
                break
        if invalid:
            print(f"Case {i+1}: invalid")

