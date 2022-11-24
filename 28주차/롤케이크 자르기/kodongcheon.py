from collections import defaultdict


def solution(topping):
    answer = 0
    A, B = {}, defaultdict(int)
    for t in topping:
        B[t] += 1

    for t in topping:
        if B[t] == 1:
            B.pop(t)
        else:
            B[t] -= 1
        A[t] = 1
        if len(A) == len(B):
            answer += 1
    return answer