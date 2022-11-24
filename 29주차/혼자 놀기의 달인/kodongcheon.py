def solution(cards):
    cards = [0] + cards
    visited = [0] * len(cards)
    result =[]
    for i in range(1, len(cards)):
        if not visited[i]:
            result.append(dfs(i, cards, visited, 0))
    result.sort()
    if len(result) == 1:
        return 0
    else:
        return result[-1] * result[-2]


def dfs(v, arr, visited, cnt):
    if visited[v]:
        return cnt
    else:
        visited[v] = True
        return dfs(arr[v], arr, visited, cnt+1)