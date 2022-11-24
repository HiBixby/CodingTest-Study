import sys
input = sys.stdin.readline

n = int(input()) # 행렬의 개수
matrix = [list(map(int, input().split())) for _ in range(n)] # 행렬들의 크기를 담은 배열
dp = [[0] * n for _ in range(n)] # 행렬을 곱하는데 필요한 곱셈의 최소 횟수를 담은 배열
# dp[i][j] : matrix[i]에서 matrix[j]까지 행렬을 곱하는데 필요한 곱셈의 최소 횟수

for size in range(1, n): # 범위가 1부터인 이유 : dp[i][i] = 0이니까
    for i in range(0, n - size): # dp에서 대각선 기준으로 우측만 사용하니까 범위 저렇게 잡음
        j = i + size # 현재 대각선에서 몇번째 원소인지 나타냄

        if size == 1: # 차이가 1밖에 나지 않는 경우 = 대각선 바로 오른쪽인 경우
            # 행렬 2개를 그냥 곱해주는 것과 같음
            # [i*j] * [j*k] -> [i*j], 곱셈 횟수 : i*j*k
            dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
            continue

        dp[i][j] = float("inf")
        for k in range(i, j): # k의 값으로 최적 분할을 찾음
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] +
                           matrix[i][0] * matrix[k][1] * matrix[j][1])
            # 각 분할의 곱셈 횟수 = 각 부분행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
            # dp[1][k] : 배열1부터 배열k까지의 곱셈 횟수
            # dp[k+1][n] : 배열k+1부터 배열n까지의 곱셈 횟수
            # i*j*k : 두 행렬의 곱셈 횟수

print(dp[0][n-1])