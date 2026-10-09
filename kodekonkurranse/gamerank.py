import sys

hist = sys.stdin.read().strip()

rqs = {}
for x in range(1, 11):
    rqs[x] = 5
for x in range(11, 16):
    rqs[x] = 4
for x in range(16, 21):
    rqs[x] = 3
for x in range(21, 26):
    rqs[x] = 2

rank = 25
stars = 0
streak = 0
for c in hist:

    if rank <= 5:
        if c == "L":
            streak = 0
            if stars < 0:
                rank += 1
                stars = rqs[rank] - 1
        elif c == "W":
            streak += 1
            stars += 1
            if stars > rqs[rank]:
                rank -= 1
                stars = 1

    elif 5 < rank < 20:
        if c == "L":
            streak = 0
            stars -= 1
            if stars < 0:
                rank += 1
                stars = rqs[rank] - 1
        elif c == "W":
            streak += 1
            if streak >= 3:
                stars += 1
            if stars > rqs[rank]:
                rank -= 1
                stars = 1
            stars += 1
            if stars > rqs[rank]:
                rank -= 1
                stars = 1

    elif rank > 20 :
        if c == "L":
            streak = 0
        if c == "W":
            streak += 1
            if streak >= 3:
                stars += 1
            if stars > rqs[rank]:
                rank -= 1
                stars = 1
            stars += 1
            if stars > rqs[rank]:
                rank -= 1
                stars = 1

    elif rank == 20:
        if c == "L":
            streak = 0
            if stars > 0:
                stars -= 1
        if c == "W":
            streak += 1
            if streak >= 3:
                stars += 1
            if stars > rqs[rank]:
                rank -= 1
                stars = 1
            stars += 1
            if stars > rqs[rank]:
                rank -= 1
                stars = 1

    if rank == 0:
        print("Legend")
        exit()

print(rank)
    
