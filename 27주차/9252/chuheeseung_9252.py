import sys
input = sys.stdin.readline()

# dp의 가장 맨 아래오른쪽 [n-1][m-1]에서 시작
# 대각선에서 +1이 된 경우에만 대각선으로 이동
# 그렇지 않으면 위값, 왼쪽갑 중 큰 값으로 이동해서 계속 탐색

s1 = input()
s2 = input()
n = len(s1) # 세로, \n 포함
m = len(s2) # 가로

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if s1[i-1] == s2[j-1]: # 둘이 같은 위치에서 문자가 같은 경우
            dp[i][j] = dp[i-1][j-1] + 1 # 이전 대각선 값 + 1
        else: # 다른 경우
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 위값, 왼쪽값 중 최댓값

maxLen = dp[n-1][m-1] # 가장 아래오른쪽 값이 최대 길이
print(maxLen)

# 문자열 찾아내는 부분
answer = []
x = m - 1
y = n - 1

while x > 0 and y > 0:
    if dp[y][x-1] == dp[y][x]: # 위값이랑 같은 경우
        x -= 1 # 위로 이동
    elif dp[y-1][x] == dp[y][x]: # 왼쪽값이랑 같은 경우
        y -= 1 # 왼쪽으로 이동
    else: # 둘 다 아닌 경우 : 왼,위값보다 [y][x]값이 커야함 <- 해당하는 경우
        answer.append(s1[y-1]) # 최장공통부분수열에 해당 -> answer에 추가
        x -= 1 # 왼쪽 위 대각선으로 한칸 이동
        y -= 1

for c in answer[::-1]:
    print(c, end="")

print()