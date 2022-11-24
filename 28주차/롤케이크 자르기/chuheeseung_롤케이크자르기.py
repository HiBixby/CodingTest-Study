from collections import Counter

def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    result = 0

    for i in topping: # dic에서 빼서 set_dic으로 이동해서 나눔
        dic[i] -= 1
        set_dic.add(i)

        if dic[i] == 0:
            dic.pop(i)

        if len(dic) == len(set_dic): # 토핑의 수가 같은 경우 result + 1
            result += 1

    return result

# topping = [1, 2, 1, 3, 1, 4, 1, 2]
# answer = solution(topping)
# print(answer)