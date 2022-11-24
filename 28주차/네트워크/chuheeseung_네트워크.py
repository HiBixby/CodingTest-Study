def solution(n, computers):
    answer = 0 # 네트워크의 개수
    visited = [False for i in range(n)] # 방문 여부 체크하는 리스트

    for i in range(n):
        if visited[i] == False: # 방문하지 않은 경우 dfs 탐색
            DFS(n, computers, i, visited)
            answer += 1 # 탐색이 끝난거면 하나의 네트워크가 만들어졌다는 뜻 -> answer + 1

    return answer

def DFS(n, computers, c, visited):
    visited[c] = True # 방문했다고 True 값으로 변경

    for i in range(n):
        if i != c and computers[c][i] == 1: # 연결된 컴퓨터인 경우 아직 방문 안했으면 이어서 탐색
            if visited[i] == False:
                DFS(n, computers, i, visited)

# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# answer = solution(n, computers)
# print(answer)