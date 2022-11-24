import sys
sys.setrecursionlimit(10 ** 6)

def dfs(i):
    global answer
    visit[i] = True # 방문했다고 체크
    cycle.append(i) # 탐색한 경로 저장
    num = arr[i] # 다음에 방문할 정점 -> num

    if visit[num]: # num을 방문한 경우
        if num in cycle: # 탐색 경로에 다음 방문할 정점이 존재하는 경우
            answer += cycle[cycle.index(num):] # 사이클이 되는 구간부터만 팀으로 만든다
        return
    else:
        dfs(num) # num 탐색 진행

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n = int(input()) # 학생 수

    arr = [0] + list(map(int, input().split())) # 그래프 생성, 0 추가해서 인덱스 접근 편하기 위함
    visit = [False] * (n + 1) # 방문 여부 체크
    answer = [] # 팀을 구성한 학생들을 담는 배열

    for i in range(1, n + 1): # 1번 학생부터 탐색 시작
        if not visit[i]: # 방문하지 않았을 경우에만 탐색
            cycle = [] # 탐색한 경로를 담을 배열
            dfs(i)

    print(n - len(answer)) # 팀을 이루지 않은 인원수를 반환