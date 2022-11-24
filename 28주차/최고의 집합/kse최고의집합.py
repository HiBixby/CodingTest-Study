def solution(n, s):
    answer = []
    # 될 수 없는 경우
    if n > s:
        return [-1]

    mok = s // n # 4
    na = s % n # 1

    # n - 나머지 만큼 몫 추가
    for _ in range(n - na): #
        answer.append(mok)
    # 나머지 만큼 몫 + 1 추가
    for _ in range(na):
        answer.append(mok+1)

    return answer


print(solution(2, 9))