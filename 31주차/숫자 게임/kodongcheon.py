from collections import deque
def solution(A, B):
    A.sort()
    B.sort()
    q = deque(B)
    cnt = 0
    for i in A:
        while q:
            num = q.popleft()
            if num > i:
                cnt +=1
                break
    return cnt