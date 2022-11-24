def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 시작 위치 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue

            if [j, i] in puddles:  # 웅덩이가 존재하면
                continue
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007  # 위쪽에서 온 경우와 왼쪽에서 온 경우 중에 최솟값 갱신

    return dp[n][m]