import heapq

def solution(operations):
    answer = []
    heap = []

    for data in operations:
        if data[0] == "I": # 연산이 I인 경우 : 공백 뒤의 숫자를 힙에 넣는다
            heapq.heappush(heap, int(data[2:]))
        else: # 연산이 D인 경우
            if len(heap) == 0:
                pass
            elif data[2] == "-": # 공백 뒤가 -인 경우 : 최소힙 제거
                heapq.heappop(heap)
            else: # 공백 뒤가 아무것도 아닌 경우 : 힙에서 가장 큰 수를 제외하고 다시 힙에 넣음
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

    if heap: # 힙 안비어있는 경우 최대, 최소 반환
        answer.append(max(heap))
        answer.append(min(heap))
    else: # 힙 비어 있는 경우 : 0, 0 반환
        answer.append(0)
        answer.append(0)

    return answer

# operation = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# operation = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# answer = solution(operation)
# print(answer)