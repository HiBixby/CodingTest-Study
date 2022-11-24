def dfs (i, computers, visited):
    visited[i] = True
    for j, con in enumerate(computers[i]):
        if con and (not visited[j]): # 네트워크가 연결된 노드 중에서 방문 안된 노드 찾기(그러고 찾게되면 재귀함수로 방문한걸로 처리)
            dfs(j, computers, visited)

def solution(n, computers):
    answer = 0
    global visited
    visited = [False]*n
    for i in range(n):
        # print(visited[i])
        if not visited[i]:
            dfs(i, computers, visited)
            answer+=1
    return answer

# print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))