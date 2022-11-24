from collections import deque

def solution(operations) :
    que = []
    answer = []

    for o in operations:
        temp, num = o.split(' ')
        if temp == 'D':
            if not que:
                continue
            if num == '1':
                que.sort()
            else:
                que.sort(reverse=True)
            que.pop()
        else:
            que.append(int(num))

    que.sort()
    if len(que) == 0:
        return [0, 0]
    else:
        return [int(que[len(que)-1]), int(que[0])]

#
# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))