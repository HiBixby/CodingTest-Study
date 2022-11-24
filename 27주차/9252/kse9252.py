#LCS 2
lcs_list2=[0] + list(input().rstrip())
lcs_list1=[0] + list(input().rstrip())

dp = [[0 for _ in range(len(lcs_list1))] for __ in range(len(lcs_list2))]

for i in range(1, len(lcs_list2)):
    for j in range(1, len(lcs_list1)):
        if lcs_list2[i] == lcs_list1[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1 # 같은 문자가 있을 때 마다 +1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # 다른 문자이면 list1에서의 전 dp 값과 list2에서의 전 dp값을 비교해서 최대갑 넣기

row = len(lcs_list2) - 1 #맨 끝에부터해서 시작
col = len(lcs_list1) - 1
answer = ""

while dp[row][col]: # 맨 끝에 있는 인자부터 해서 줄여나가면서 숫자가 안 겹칠 때 문자를 추가 해준다.
    if dp[row][col] == dp[row - 1][col]:
        row -= 1
    elif dp[row][col] == dp[row][col - 1]:
        col -= 1
    else:
        answer = lcs_list2[row] + answer
        row -= 1
        col -= 1

print(dp[len(lcs_list2) - 1][len(lcs_list1) - 1])
print(answer)