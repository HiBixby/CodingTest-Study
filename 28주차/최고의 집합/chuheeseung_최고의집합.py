def solution(n, s):
    answer = []

    if s // n < 1: # n개의 숫자로 s를 만들 수 없는 경우
        answer = [-1]
    else:
        # 정답 리스트 속의 원소 개수가 n개가 되도록 함
        # 최대의 곱을 만들기 위해서는 최대한 균일한 숫자를 분포시켜주는 것이 중요하기 때문
        # s를 자연수 n개로 표현하면서 곱이 가장 큰 수가 되도록 하려면 : n개의 각 자연수 간의 차이가 적어야 한다
        # s//n를 n개만큼 저장하는게 일단 곱이 가장 큰 조합
        s_n = s // n

        for i in range(n):
            answer.append(s_n)

        # 나머지가 남는 경우가 존재
        # 오름차순 정렬이어야 하니까 나머지 숫자만큼 리스트 맨 뒤에서부터 1을 더해주면 된다
        s_p_n = s % n
        idx = len(answer) - 1

        for i in range(s_p_n):
            answer[idx-i] = answer[idx-i] + 1

    return answer

# n = 2 # 집합의 원소의 개수
# s = 9 # 모든 원소들의 합
# answer = solution(n, s)
# print(answer)