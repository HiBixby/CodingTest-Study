T = int(input()) #테스트 케이스의 개수

def dfs(node, e, v):
    temp_node = {}
    now_len = 0
    stack = [node]
    v[node] = True

    while stack:
        now = stack.pop()
        temp_node[now] = now_len
        now_len += 1

        if not v[e[now]]:
            v[e[now]] = True
            stack.append(e[now])

        if e[now] in temp_node:
            return now_len - temp_node[e[now]]

    return 0


for _ in range(T):
    n = int(input())
    #그래프 만들기
    visit = {i + 1: False for i in range(n)} #dic
    edge = [0] + list(map(int, input().rsplit())) #1부터 시작해야 하므로 0번째 ㅇ니덱스 넣어놓기

    temp = 0
    for node in range(1, n + 1):
        if not visit[node]:
            temp += dfs(node, edge, visit) #dfs

    print(n - temp)