from collections import deque

def solution(order):
    n = len(order)
    main = deque([num for num in range(1, n + 1)]) # 메인 컨베이어 벨트, 큐
    sub = [] # 보조 컨베이어 벨트, 스택
    answer = 0 # 실을 수 있는 상자 개수

    for i, box in enumerate(order):
        if sub and sub[-1] == box: # 보조 컨베이어 벨트가 존재하고, 보조 컨베이어 벨트 마지막이 박스랑 같은 경우
            sub.pop() # 컨베이어 벨트에서 박스를 꺼낸다
            answer += 1
        else: # 보조 컨베이어 벨트에 박스가 없거나 마지막이 박스랑 다른 경우
            if not main: # 메인 컨베이어 벨트에 박스가 없으면 패스
                break

            while main:
                b = main.popleft() # 메인 벨트에서는 앞에서 박스를 내릴 수 있다 -> popleft()
                if b == box: # b랑 박스랑 같으면 택배 실을 수 있다
                    answer += 1
                    break
                else: # b랑 박스랑 다르면 b를 보조 컨베이어 벨트로 보낸다
                    sub.append(b)

    return answer


# order = [4, 3, 1, 2, 5]
# solution(order)