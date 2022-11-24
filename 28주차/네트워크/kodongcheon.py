def dfs(graph, v, visited):
    visited[v] = True
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)
def solution(n, computers):
    visited = [False]*n
    result = 0
    for j in range(len(computers)):
        if visited[j] == False:
            dfs(computers, j, visited)
            result+=1
    return result