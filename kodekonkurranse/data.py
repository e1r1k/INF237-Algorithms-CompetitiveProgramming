import heapq
from collections import deque

def sovle(N):
    heap = []
    queue = deque([])
    stack = []
    data = [True, True, True]
    if N == 0:
        return
    for _ in range(N):
        a, b = map(int, input().split())
        if (a == 1):
            if data[0] == True:
                heapq.heappush(heap, -b)
            if data[1] == True:
                queue.append(b)
            if data[2] == True:
                stack.append(b)
        else:
            if data[0] == True:
                if len(heap) == 0 or -heapq.heappop(heap) != b:
                    data[0] = False
            if data[1] == True:
                if len(stack) == 0 or stack.pop() != b:
                    data[1] = False
            if data[2] == True:
                if len(queue) == 0 or queue.popleft() != b:
                    data[2] = False

    if data[0] == True and sum(data) == 1:
        print("priority queue")
        return

    if data[1] == True and sum(data) == 1:
        print("stack")
        return

    if data[2] == True and sum(data) == 1:
        print("queue")
        return

    if sum(data) == 0:
        print("impossible")
        return
    
    print("not sure")
    

def main():
    try:
        line = input()
        N = int(line)
        while True:
            sovle(N)
            line = input()
            N = int(line)
    except:
        pass

    
main()