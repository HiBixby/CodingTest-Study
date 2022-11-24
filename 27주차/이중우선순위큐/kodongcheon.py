from heapq import *
def solution(operations):
    cnt = 0
    h1 = []
    h2 = []
    for operation in operations:
        command, num = operation.split()
        if command == "I":
            cnt+=1
            heappush(h1, int(num))
            heappush(h2, -int(num))
        elif command == "D":
            if cnt <= 1:
                cnt = 0
                h1 = []
                h2 = []
                continue
            cnt -=1
            if num == "1":
                heappop(h2)
            else:
                heappop(h1)
    if cnt == 0:
        return [0, 0]
    else:
        return [-heappop(h2), heappop(h1)]
