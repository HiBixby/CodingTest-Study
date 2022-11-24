def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        a = i // n
        b = i % n
        result = max(a, b) + 1
        answer.append(result)

    return answer