from collections import deque
def solution(order):
    order = deque(order)
    stack = []
    cnt = 0
    for i in range(1, len(order)+1):
        if order[0] == i:
            order.popleft()
            cnt += 1
            while stack:
                if order[0] == stack[-1]:
                    cnt+=1
                    order.popleft()
                    stack.pop()
                else:
                    break
        else:
            while stack:
                if order[0] == stack[-1]:
                    cnt+=1
                    order.popleft()
                    stack.pop()
                else:
                    stack.append(i)
                    break
            else:
                stack.append(i)
    return cnt