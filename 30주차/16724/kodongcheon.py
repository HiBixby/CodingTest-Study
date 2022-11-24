import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [input().rstrip() for i in range(N)]

def dfs(x, y, arr, visited, cnt, routeArr):
    if visited[x][y]:
        if visited[x][y] != cnt:
            return True, routeArr
        else:
            return False, routeArr
    routeArr.append((x, y))
    visited[x][y] = cnt
    if arr[x][y] == "D":
        return dfs(x+1, y, arr, visited, cnt, routeArr)
    if arr[x][y] == "L":
        return dfs(x, y-1, arr, visited, cnt, routeArr)
    if arr[x][y] == "R":
        return dfs(x, y+1, arr, visited, cnt, routeArr)
    if arr[x][y] == "U":
        return dfs(x-1, y, arr, visited, cnt, routeArr)


cnt = 0
visited = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            routeArr = []
            cnt += 1
            status, routeArr= dfs(i, j, arr, visited, cnt, routeArr)
            if status:
                for route in routeArr:
                    visited[route[0]][route[1]] -= 1
                cnt -=1

print(cnt)