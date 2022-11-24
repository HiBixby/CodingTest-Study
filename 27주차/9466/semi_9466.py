# 텀 프로젝트 : sr-1 -> sr, sr -> s1을 선택하는 경우에만 한 팀이 될 수 있음
# trace = [2 1 3] : next가 3이고, 3을 시작점으로 뒤에 배열이 없기 때문에 팀 결성 X
# trace = [4 7 6] : next가 4이고, 4를 시작점으로 뒤에 3개의 팀이 구성됨

import sys
sys.setrecursionlimit(10 ** 6)


def is_team(x):
    global cnt
    visited[x] = True
    trace.append(x)

    next = arr[x]
    if visited[next]:   # 다음에 방문할 정점이 끝났는지 체크
        if next in trace:    # 다음에 방문할 정점이 탐색 경로에 존재하는 경우에 싸이클이 발생(팀이 구성)
            cnt += len(trace[trace[next]:])
    else:
        is_team(x)     # 방문하지 않았다면 재귀 호출


T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = [0] + list(map(int, input().split()))  # 인덱스 1부터 시작
    visited = [False for _ in range(n + 1)]      # 팀으로 결정된 자들을 재방문 하지 않기 위한 배열
    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            trace = []     # 추적 경로
            is_team(i)
    print(n - cnt)       # 전체 학생 수 - 팀에 속한 학생 수
