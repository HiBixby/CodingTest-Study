import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
q.append([n])
answer = []

while q:
    a = q.popleft()
    x = a[0]

    if x == 1:
        answer = a
        break

    if x % 3 == 0:
        q.append([x//3] + a) # 마지막 출력할 때 수를 모두 출력하기 위해 더해줌

    if x % 2 == 0:
        q.append([x//2] + a)


    q.append([x-1] + a)

print(len(answer) - 1)
print(*answer[::-1])