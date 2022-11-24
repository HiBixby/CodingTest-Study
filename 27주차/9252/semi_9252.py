# 수열 중 모두의 부분 수열이 되는 최대 길이의 수열 찾기
# 문자열 길이와 문자열 출력, LCS의 길이가 0인 경우에는 둘째 줄을 출력 X
# dp[i][j] = 문자열[i][j] 길이 까지의 최대 공통 부분 수열의 길이
# 문자열 자체를 구하기 => 왼, 위쪽 숫자가 같은 경로로 이동 => 다시 왼, 외쪽 숫자 비교 후 같은 값이 없다면 대각선으로 이동


str1 = input()
str2 = input()
C, R = len(str1), len(str2)
dp = [[0 for _ in range(C+1)] for _ in range(R+1)]  # 열이 첫번째 문자열, 행이 두번째 문자열

# 문자열 길이 구하기
for i in range(1, R+1):
    for j in range(1, C+1):
        if str2[i-1] == str1[j-1]:   # 문자가 같다면
            dp[i][j] = dp[i-1][j-1] + 1   # 이전 문자열 LCS 길이 + 공통된 문자 더하기
        else:                        # 문자가 같지 않다면
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 비교 하려는 두 문자중 하나씩 넣었을 때 LCS 길이가 가장 큰 값 택하기

# 문자열 구하기
i, j = R, C
result = []
while i > 0 and j > 0:
    if dp[i-1][j] == dp[i][j]:   # 위쪽 문자가 같은 경우 위쪽으로 이동
        i = i-1
    elif dp[i][j-1] == dp[i][j]:   # 왼쪽 문자가 같은 경우 왼쪽으로 이동
        j = j-1
    else:      # 둘다 같지 않은 경우 대각선으로 이동
        i, j = i-1, j-1
        if str2[i] == str1[j]:   # 대각선 이동 했을 때 두 문자가 같은 경우에만 결과값에 추가
            result.append(str2[i])

print(dp[R][C])
if dp[R][C] != 0:
    print("".join(list(reversed(result))))


