def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1 # 집 좌표

    for i, j in puddles: # 웅덩이가 있는 곳 -> -1 표시
        dp[j][i] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1: # 웅덩이인 경우
                dp[i][j] = 0 # 이후 값에 영향 안주기 위해서 0으로 바꿈
                continue # 건너뜀

            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % 1000000007
            # 왼쪽에서 오는 경우 [i-1][j] + 위쪽에서 오는 경우 [i][j-1] 더해줌
            # 1~~~7로 나누라고 했으니까 나눠줌

    return dp[n][m]

# m = 4
# n = 3
# puddles = [[2, 2]]
# answer = solution(m, n, puddles)
# print(answer)