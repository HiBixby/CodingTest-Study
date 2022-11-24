# 영재가 몇 개의 상자를 실을 수 있는지 return

from collections import deque

def solution(order):
    container = deque([i + 1 for i in range(len(order))])
    sub_container = []
    cur = 0

    while container:  # 1. 주 컨테이너에서 담을 수 있는 박스의 개수 찾기
        if order[cur] != container[0]:   # 원하는 상자와 주 컨테이너에서 꺼낼 수 있는 상자가 다른 경우
            if sub_container and order[cur] == sub_container[-1]:   # 보조 컨테이너가 비어 있지 않다면 마지막 원소와 같은지 검사
                cur += 1         # 같다면 다음 원하는 상자로 이동
                sub_container.pop()  # 보조 컨테이너에서 제거
            else:                    # 보조 컨테이너가 비어 있는 경우
                sub_container.append(container.popleft())   # 주 컨테이너에서 꺼내서 추가
        else:           # 원하는 상자와 주 컨테이너에서 꺼낼 수 있는 상자가 같다면 바로 꺼내기
            cur += 1
            container.popleft()

    while sub_container:   # 2. 보조 컨테이너에서 담을 수 있는 박스의 개수 찾기
        if order[cur] == sub_container[-1]:  # 보조 컨테이너서 꺼낼 수 있는 박스와 원하는 박스가 같은 경우
            cur += 1
            sub_container.pop()
        else:            # 바로 꺼낼 수 없다면 더이상 진행 불가능
            break
    return cur


print(solution([4, 3, 1, 2, 5]))