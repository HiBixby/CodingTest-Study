def solution(n, left, right):
    answer = []

    for i in range(left, right + 1): # left ~ right까지 범위
        answer.append(max(i//n, i%n) + 1)
        # i를 n으로 나눈 몫과 나머지 중 더 큰 값 + 1
        # 각 자리의 숫자 = 행과 열 중 더 큰 것의 인덱스 + 1
        # i가 계속 커지더라도 나눈 몫 -> 행, 나머지 -> 열로 인식해서 둘 중 더 큰 값만 취하면 됨
    return answer

# n = 3
# left = 2
# right = 5
# answer = solution(n, left, right)
# print(answer)