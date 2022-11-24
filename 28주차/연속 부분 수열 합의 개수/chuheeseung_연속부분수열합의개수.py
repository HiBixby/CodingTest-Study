def solution(elements):
    result = set() # set -> 중복 제거

    elementLength = len(elements)
    elements = elements * 2 # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]

    for i in range(elementLength):
        for j in range(elementLength):
            result.add(sum(elements[j:j+i+1])) # 부분수열 경우의 수를 돌면서 합을 result에 추가

    return len(result) # result의 개수 = 수열 합으로 만들 수 있는 수의 개수

# elements = [7, 9, 1, 1, 4]
# answer = solution(elements)
# print(answer)