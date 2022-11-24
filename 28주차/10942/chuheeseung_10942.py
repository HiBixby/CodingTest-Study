import sys
input = sys.stdin.readline

n = int(input()) # n : 수열의 크기
numbers = [int(i) for i in input().split()] # n개 숫자 리스트
dp = [[0 for _ in range(n)] for _ in range(n)]
# dp[처음][끝] : 처음 ~ 끝 경우 팰린드롬 여부 확인하는 배열

for i in range(n): # 길이가 1인 경우 -> 팰린드롬
    dp[i][i] = 1

for i in range(n-1): # 길이가 2인 경우
    if numbers[i] == numbers[i + 1]: # 두 문자가 같은 경우 -> 팰린드롬
        dp[i][i+1] = 1

for j in range(2, n): # 길이가 3 이상인 경우
    for i in range(n - j):
        if numbers[i] == numbers[i+j] and dp[i+1][i+j-1] == 1:
            # 처음 문자 == 끝문자 && dp[처음+1][마지막-1]이 1인 경우 -> 팰린드롬
            dp[i][i+j] = 1

m = int(input()) # m : 질문의 개수

for _ in range(m):
    s, e = [int(a) for a in input().split()] # s~e만큼 팰린드롬이 되는지 출력
    print(dp[s-1][e-1])