from math import gcd # 최대공약수 라이브러리

def get_gcd(arr):
    g = arr[0]

    for i in range(len(arr)):
        g = gcd(g, arr[i]) # g, arr[i]의 최대공약수를 리턴

    return g


def solution(arrayA, arrayB):
    answer = 0
    gA, gB = get_gcd(arrayA), get_gcd(arrayB) # arrayA, arrayB의 최대공약수

    for b in arrayB: # 영희 카드
        if not b % gA:
            break
    else: # arrayB가 gA로 모두 나눌 수 없는 경우 answer 갱신
        answer = max(answer, gA) # 가장 큰 a를 리턴해야 하니까 max함수

    for a in arrayA: # 철수 카드
        if not a % gB:
            break
    else: # arrayA가 gB로 모두 나눌 수 없는 경우 answer 갱신
        answer = max(answer, gB)

    return answer

# arrayA = [10, 17] # 철수 카드
# arrayB = [5, 20] # 영희 카드
# answer = solution(arrayA, arrayB)
# print(answer)