import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, M = map(int, input().split())

arr = [list(input().rstrip()) for i in range(N)]


def rec(arr, command, cnt):
    if cnt == 10:
        return -1
    tempArr = [arr[i][:] for i in range(len(arr))]
    tempArr = move(command, tempArr)
    redX, redY = find("R", tempArr)
    blueX, blueY = find("B", tempArr)
    if blueX == -1:
        return -1
    if redX == -1:
        return cnt+1
    flag = False
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if tempArr[i][j] != arr[i][j]:
                flag=True
                break
        if flag:
            break
    if flag:
        result = []
        if command == 0 or command == 1:
            result.append(rec(tempArr, 2, cnt + 1))
            result.append(rec(tempArr, 3, cnt + 1))
        else:
            result.append(rec(tempArr, 0, cnt + 1))
            result.append(rec(tempArr, 1, cnt + 1))
        tempResult = []
        for i in range(2):
            if result[i] != -1:
                tempResult.append(result[i])
        if tempResult:
            return min(tempResult)
        else:
            return -1
    else:
        return -1


def move(command, arr):
    redX, redY = find("R", arr)
    blueX, blueY = find("B", arr)
    q = deque()
    #left
    if command == 0:
        if redY < blueY:
            q.append((redX,redY))
            q.append((blueX,blueY))
        else:
            q.append((blueX, blueY))
            q.append((redX, redY))
        while q:
            x, y = q.popleft()
            for i in range(y-1, -1, -1):
                if arr[x][i] == ".":
                    continue
                else:
                    if arr[x][i] == "#" or arr[x][i] == "R" or arr[x][i] == "B":
                        arr[x][i+1], arr[x][y] = arr[x][y], arr[x][i+1]
                        break
                    if arr[x][i] == "O":
                        arr[x][y] = "."
                        break

    #right
    if command == 1:
        if redY < blueY:
            q.append((blueX, blueY))
            q.append((redX, redY))
        else:
            q.append((redX, redY))
            q.append((blueX, blueY))
        while q:
            x, y = q.popleft()
            for i in range(y+1, len(arr[0])):
                if arr[x][i] == ".":
                    continue
                else:
                    if arr[x][i] == "#" or arr[x][i] == "R" or arr[x][i] == "B":
                        arr[x][i-1], arr[x][y] = arr[x][y], arr[x][i-1]
                        break
                    if arr[x][i] == "O":
                        arr[x][y] = "."
                        break
    #up
    if command == 2:
        if redX < blueX:
            q.append((redX,redY))
            q.append((blueX,blueY))
        else:
            q.append((blueX, blueY))
            q.append((redX, redY))
        while q:
            x, y = q.popleft()
            for i in range(x-1, -1, -1):
                if arr[i][y] == ".":
                    continue
                else:
                    if arr[i][y] == "#" or arr[i][y] == "R" or arr[i][y] == "B":
                        arr[i+1][y], arr[x][y] = arr[x][y], arr[i+1][y]
                        break
                    if arr[i][y] == "O":
                        arr[x][y] = "."
                        break
    #dowm
    if command == 3:
        if redX < blueX:
            q.append((blueX, blueY))
            q.append((redX, redY))
        else:
            q.append((redX, redY))
            q.append((blueX, blueY))
        while q:
            x, y = q.popleft()
            for i in range(x+1, len(arr)):
                if arr[i][y] == ".":
                    continue
                else:
                    if arr[i][y] == "#" or arr[i][y] == "R" or arr[i][y] == "B":
                        arr[i-1][y], arr[x][y] = arr[x][y], arr[i-1][y]
                        break
                    if arr[i][y] == "O":
                        arr[x][y] = "."
                        break
    return arr

def find(color, arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == color:
                return (i, j)
    else:
        return (-1, -1)


result = []
for i in range(4):
    cnt = rec(arr, i, 0)
    if cnt != -1:
        result.append(cnt)
if result:
    print(min(result))
else:
    print(-1)

