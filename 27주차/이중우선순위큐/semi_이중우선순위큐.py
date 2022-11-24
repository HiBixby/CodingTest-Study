# 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어 있지 않으면 [최댓값, 최솟값]을 return

from heapq import heappush, heappop


def solution(operations):
    hq = []
    for op in operations:
        cmd, data = op[0], int(op[2:])

        if cmd == 'I':  # 힙에 푸시
            heappush(hq, data)
        elif hq and cmd == 'D':
            if data == 1:  # 최댓값 삭제
                hq.remove(max(hq))
            else:  # 최솟값 삭제
                heappop(hq)

    return [max(hq), hq[0]] if hq else [0, 0]


print(solution(["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]))


