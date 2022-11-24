def solution(m, n, puddles):
    dp = [[0] * (m + 1) for i in range(n + 1)]
    arr = [[1] * (m + 1) for i in range(n + 1)]
    for puddle in puddles:
        arr[puddle[1]][puddle[0]] = 0
    result = req(1, 1, dp, arr)
    return dp[1][1] % 1000000007


def req(x, y, dp, arr):
    if x == len(dp) - 1 and y == len(dp[0]) - 1:
        return 1
    if dp[x][y]:
        return dp[x][y]
    cost = 0
    if x + 1 < len(dp) and arr[x + 1][y]:
        cost += req(x + 1, y, dp, arr)
    if y + 1 < len(dp[0]) and arr[x][y + 1]:
        cost += req(x, y + 1, dp, arr)
    dp[x][y] = cost
    return dp[x][y]