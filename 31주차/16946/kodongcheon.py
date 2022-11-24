import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().rstrip())) for i in range(N)]

def bfs(x, y, visited, arr, dp, index):
    visited[x][y] = True
    q = deque([(x,y)])

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 1
    dpArr = [(x, y)]
    while q:
        x, y = q.popleft()
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if 0 <= dx < len(arr) and 0 <= dy < len(arr[0]) and arr[dx][dy] == 0 and not visited[dx][dy]:
                visited[dx][dy] = True
                cnt += 1
                q.append((dx, dy))
                dpArr.append((dx, dy))

    for x, y in dpArr:
        dp[x][y] = (cnt, index)

def search(x, y, arr, dp):
    cnt = 0
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    indexCheckArr = []
    for move in moves:
        dx = x + move[0]
        dy = y + move[1]

        if 0 <= dx < len(arr) and 0 <= dy < len(arr[0]) and not dp[dx][dy][1] in indexCheckArr:
            cnt += dp[dx][dy][0]
            indexCheckArr.append(dp[dx][dy][1])
    return (cnt + 1) % 10

visited = [[False] * M for i in range(N)]
dp = [[(0,0)] * M for i in range(N)]
index= 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and not visited[i][j]:
            bfs(i, j, visited, arr, dp, index)
            index +=1

result = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt = search(i, j, arr, dp)
            result[i][j] = cnt

for x in result:
    print(*x, sep= "")



