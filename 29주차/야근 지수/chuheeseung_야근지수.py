import heapq
def solution(n, works):
    answer = 0

    if sum(works) <= n: # 야근할 필요가 없는 경우
        return 0

    works = [-w for w in works]
    # 모든 값에 -를 붙임
    # heapq는 최솟값이 우선 -> -를 붙이면 최댓값을 기준으로 정렬한 효과
    heapq.heapify(works) # works를 heapq 배열로 변환

    while n > 0:
        max_val = heapq.heappop(works) # 최솟값을 뽑아냄
        heapq.heappush(works, max_val + 1) # 1을 더해서 다시 넣어줌
        n -= 1

    for w in works: # 최종적으로 연산된 works에 대해서 제곱합 구해서 반환
        answer += w ** 2

    return answer

# works = [4, 3, 3]
# n = 4
# result = 12
# answer = solution(works, n, result)
# print(answer)