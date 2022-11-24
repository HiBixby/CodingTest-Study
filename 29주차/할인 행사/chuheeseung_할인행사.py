from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}

    for i in range(len(want)): # Counter를 이용해서 dic을 초기화
        dic[want[i]] = number[i]

    for i in range(len(discount) - 9): # Q. 범위를 왜 이렇게 잡았지?
        if dic == Counter(discount[i:i+10]):
            answer += 1

    return answer

# want = ["banana", "apple", "rice", "pork", "pot"] # 원하는 제품을 나타내는 문자열 배열
# number = [3, 2, 2, 2, 1] # 원하는 제품의 수량을 나타내는 정수 배열
# discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork",
#             "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
# 마트에서 할인하는 제품을 나타내는 문자열 배열
#
# answer = solution(want, number, discount)
# print(answer)