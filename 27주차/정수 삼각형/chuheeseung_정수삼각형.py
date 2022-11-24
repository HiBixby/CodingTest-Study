def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))] # 거쳐온 숫자들의 합의 최댓값을 저장하는 배열
    dp[0][0] = triangle[0][0]

    # triangle[i][j]에 가는 방법
    # 1. triangle[i-1][j-1] -> triangle[i][j]
    # 2. triangle[i-1][j] -> triangle[i][j]
    # 두가지 중 최댓값을 dp[i][j]에 저장

    for i in range(0, len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

    return max(dp[-1]) # 마지막 줄에서 최댓값 반환

# triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
# answer = solution(triangle)
# print(answer)