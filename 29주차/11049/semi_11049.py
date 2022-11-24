N = int(input())
arr = [list((map(int, input().split()))) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]    # DP[i][j] = i행렬부터 j행렬까지 행렬 곱의 최소값

for i in range(1, N):  # 대각선
    for j in range(0, N-i):   # 대각선에서 몇번째 열
        if i == 1:    # 차이가 1밖에 남지 않는 칸
            dp[j][j+i] = arr[j][0] * arr[j][1] * arr[j+i][1]

        dp[j][j+i] = 2**32     # 최댓값
        for k in range(j, j+i):  # k 분할
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j][0] * arr[k][1] * arr[j+i][1])

print(dp[0][N-1])