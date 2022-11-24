import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))


M = int(input())
dp = [[0]* (N+1) for i in range(N+1)]

for i in range(N):
    start = i
    end = i
    start2 = i
    end2 = i+1
    flag1 = False
    flag2 = False
    while start >= 0 and end < N:
        if flag1:
            dp[start][end] = 0
        else:
            if arr[start] == arr[end]:
                dp[start][end] = 1
            else:
                dp[start][end] = 0
                flag1 = True
        start -=1
        end +=1
    while start2 >= 0 and end2 < N:
        if flag2:
            dp[start2][end2] = 0
        else:
            if arr[start2] == arr[end2]:
                dp[start2][end2] = 1
            else:
                dp[start2][end2] = 0
                flag2 = True
        start2 -=1
        end2 +=1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])