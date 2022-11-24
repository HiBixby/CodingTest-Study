from collections import Counter
#???

def solution(topping):
    answer = 0
    dic = Counter(topping) #각 토핑의 개수와 토핑을 딕셔너리화
    temp = set()

    for i in topping:
        dic[i] -= 1 # i 토핑의 개수 하나 줄이고
        if dic[i] == 0: # 만약 그때 토핑이 없을 때
            # print("기존 dic: ",*dic)
            dic.pop(i) #그 토핑 빼기
            # print("뺀 dic: ",*dic)
        temp.add(i) #그리고 temp에 넣기
        # print(temp)
        if len(dic) == len(temp):
            answer += 1

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))