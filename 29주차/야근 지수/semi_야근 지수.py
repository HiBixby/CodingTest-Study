# 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴

import heapq

def solution(n, works):
    hq = []
    res = 0

    if n > sum(works):     # 남은 작업량이 없는 경우
        return 0

    for work in works:
        heapq.heappush(hq, (-1*work, work))    # (우선 순위, 값) 형태로 저장 해서 최대 힙 생성

    for _ in range(n):
        x, y = heapq.heappop(hq)
        heapq.heappush(hq, (x+1, y-1))       # 총 n시간 동안 큰 작업 부터 작업량 감소 시키기

    while hq:
        x, y = heapq.heappop(hq)
        res += (y**2)

    return res

print(solution(4, [4, 3, 3]))



