import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    R, G ,B= map(int, input().split())
    arr.append([R,G,B])

result = []

## 1번
dp = []
dp.append([0,0,0])
dp.append([10000000, arr[0][0]+arr[1][1], arr[0][0] + arr[1][2]])

for i in range(2, N):
    select_R = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    select_G = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    select_B = arr[i][2] + min(dp[i-1][0], dp[i-1][1])
    if i == N-1:
        select_R = 10000000
        select_G = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        select_B = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    dp.append((select_R,select_G,select_B))
result.append(min(dp[-1]))

## 2번
dp = []
dp.append([0,0,0])
dp.append([arr[0][1]+arr[1][0], 10000000, arr[0][1] + arr[1][2]])

for i in range(2, N):
    select_R = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    select_G = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    select_B = arr[i][2] + min(dp[i-1][0], dp[i-1][1])
    if i == N-1:
        select_R = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        select_G = 10000000
        select_B = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    dp.append((select_R,select_G,select_B))
result.append(min(dp[-1]))

## 3번
dp = []
dp.append([0,0,0])
dp.append([arr[0][2]+arr[1][0], arr[0][2]+arr[1][1], 10000000])

for i in range(2, N):
    select_R = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    select_G = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    select_B = arr[i][2] + min(dp[i-1][0], dp[i-1][1])
    if i == N-1:
        select_R = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        select_G = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        select_B = 10000000
    dp.append((select_R,select_G,select_B))
result.append(min(dp[-1]))


print(min(result))