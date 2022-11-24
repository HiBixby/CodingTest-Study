def solution(cards):
    answer = 0
    visited = [0] * len(cards) # 방문 여부를 체크하는 리스트
    temp = []

    for i in range(len(cards)):
        n = 0
        j = i

        while visited[j] == 0: # 아직 방문하지 않은 경우에 while문 반복
            visited[j] = 1 # 방문했다고 표시
            j = cards[j] - 1
            n += 1

        if n != 0:
            temp.append(n)

    temp.sort()

    if len(temp) == 1:
        answer = 0
    else:
        answer = temp[-1] * temp[-2]

    return answer

# cards[i] : i+1번 상자에 담긴 카드에 적힌 숫자
# cards = [8,6,3,7,2,5,1,4]
# answer = solution(cards)
# print(answer)