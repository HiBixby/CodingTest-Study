from collections import defaultdict
def solution(want, number, discount):
    numberSum = sum(number)
    wantDict = {}
    for i in range(len(want)):
        wantDict[want[i]] = number[i]
    cnt = 0
    for i in range(len(discount)-numberSum+1):
        discountDict = defaultdict(int)
        for j in range(numberSum):
            discountDict[discount[i+j]] +=1
        for s in want:
            if discountDict[s] != wantDict[s]:
                break
        else:
            cnt+=1
    return cnt