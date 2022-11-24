# 연산을 사용하는 횟수의 최솟값, N을 1로 만드는 방법에 포함되어 있는 수를 출력

# 1. DFS + 백트래킹 풀이
def dfs(n, depth):
    global result, t, arr

    if depth > result:       # 진행 하다가 이미 최소 depth 넘은 경우 더 진행할 필요가 없기 때문에 리턴
        return

    if n == 1:
        if depth < result:
            result = depth
            arr.append(n)
            t = arr.copy()  # 깊은 복사로 당시의 스택값 보존
            arr.pop()
        return

    arr.append(n)           # 스택에 추가
    if n % 3 == 0:          # 세 가지 갈래로 재귀 연산 수행
        dfs(n // 3, depth + 1)

    if n % 2 == 0:
        dfs(n // 2, depth + 1)

    dfs(n - 1, depth + 1)
    arr.pop()               # 재귀 함수 종료 시 스택에서 제거


N = int(input())
result = float("inf")
arr, t = [], []
dfs(N, 0)

print(result)
print(" ".join(map(str, t)))


# 2. DP 풀이
N = int(input())
dp = [0] * (N + 1)  # dp 배열 : 숫자 1-N이 각각 1이 되는데 필요한 연산의 최소값
result = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1  # 1을 빼는 연산
    result[i] = i - 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:    # 숫자 트랙킹을 위해 기존의 수보다 작은 경우에 대해서만 갱신
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 3으로 나눈 숫자의 연산 최솟값 + 1(방금 1로 나누는 행위)
        result[i] = i // 3

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 2로 나눈 숫자의 연산 최솟값 + 1(방금 2로 나누는 행위)
        result[i] = i // 2

print(dp[N])
print(N, end=" ")

cur = N
while result[cur] != 0:
    print(result[cur], end=" ")  # 숫자 트랙킹을 위한 배열의 각 원소에는 당시의 연산 결과가 들어있음
    cur = result[cur]

