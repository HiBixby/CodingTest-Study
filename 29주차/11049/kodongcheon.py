n = int(input())

arr = [list(map(int, input().split()))for i in range(n)]

result = 0

# for _ in range(N-1):
#     temp = []
#     tempI = 0
#     resultTemp = arr[0][0] * arr[0][1] * arr[1][1]
#     for i in range(len(arr)-1):
#         temp.append(arr[i])
#
#
#         if min(arr[i][0], arr[i+1][1]) < min(arr[tempI][0], arr[tempI+1][1]):
#             resultTemp = arr[i][0] * arr[i][1] * arr[i+1][1]
#             tempI = i
#         if arr[i][0] * arr[i+1][1] == arr[tempI][0] * arr[tempI+1][1] and arr[i][1] < arr[tempI][1]:
#             resultTemp = arr[i][0] * arr[i][1] * arr[i+1][1]
#             tempI = i1
#
#     temp.append(arr[-1])
#     result += resultTemp
#
#     # print(temp)
#     temp[tempI+1][0] = temp[tempI][0]
#
#     # print(temp)
#     temp.pop(tempI)
#
#     arr = temp
# print(result)
#
dp = [[0] * n for i in range(n)]
for i in range(1, n):
    for j in range(n - i):
        x = j + i
        dp[j][x] = 2 ** 32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + arr[j][0] * arr[k][1] * arr[x][1])
print(dp[0][n - 1])
