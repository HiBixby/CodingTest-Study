def solution(triangle):
    h = len(triangle)
    dp = [[0] * h for _ in range(h)]
    dp[0][0] = triangle[0][0]       # 루트 값 초기화

    for i in range(1, h):
        for j in range(i+1):
            if j == 0:              # 맨 왼쪽인 경우, 오른쪽에서 오는 거만 받기
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif i == j:            # 맨 오른쪽인 경우, 왼쪽에서 오는 거만 받기
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]

            else:                   # 삼각형 내부에 있는 경우, 왼쪽/오른쪽 중에 큰 값을 받기
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[-1])         # 맨 마지막 줄 중에 제일 큰 값 리턴