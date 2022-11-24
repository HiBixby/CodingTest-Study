from heapq import heappush, heappop
N = int(input())
h = []
heappush(h, (0, [N]))
result = 0
resultArr = []
dp = [False] * N
while h:
    cnt, arr = heappop(h)
    if arr[-1]%3 == 0 and not dp[arr[-1]//3]:
        if arr[-1]//3 == 1:
            result = cnt+1
            resultArr = arr + [1]
            break
        dp[arr[-1]//3] = True
        heappush(h, (cnt+1, arr+[arr[-1]//3]))
    if arr[-1]%2 == 0 and not dp[arr[-1]//2]:
        if arr[-1]//2 == 1:
            result = cnt+1
            resultArr = arr + [1]
            break
        dp[arr[-1] // 2] = True
        heappush(h, (cnt+1, arr+[arr[-1]//2]))
    if not dp[arr[-1]-1]:
        if arr[-1]-1 == 1:
            result = cnt+1
            resultArr = arr + [1]
            break
        dp[arr[-1] -1 ] = True
        heappush(h, (cnt+1, arr+[arr[-1]-1]))

print(result)
if result == 0:
    print(1)
else:
    print(*resultArr)
