N = int(input())

arr  = [list(map(int, input().split())) for i in range(N)]
result = []


def dfs(command, cnt, arr):
    #left
    if command == 0:
        for i in range(len(arr)):
            temp = []
            for j in range(len(arr)):
                if arr[i][j] != 0:
                    temp.append(arr[i][j])
            arr[i] = temp + [0] * (N - len(temp))
            for j in range(len(arr)-1):
                if arr[i][j] == arr[i][j+1]:
                    arr[i][j] = arr[i][j]*2
                    arr[i].pop(j+1)
                    arr[i].append(0)

    #right
    if command == 1:
        for i in range(len(arr)):
            temp = []
            for j in range(len(arr)):
                if arr[i][j] != 0:
                    temp.append(arr[i][j])
            arr[i] = [0] * (N - len(temp)) + temp
            for j in range(len(arr)-1, 0, -1):
                if arr[i][j] == arr[i][j-1]:
                    arr[i][j] = arr[i][j]*2
                    arr[i].pop(j-1)
                    arr[i] = [0] + arr[i]

    #up
    if command == 2:
        for j in range(len(arr)):
            temp = []
            for i in range(len(arr)):
                if arr[i][j] != 0:
                    temp.append(arr[i][j])
            temp = temp + [0] * (N - len(temp))
            for i in range(len(arr)):
                arr[i][j] = temp[i]
            for i in range(len(arr)-1):
                if arr[i][j] == arr[i+1][j]:
                    arr[i][j] = arr[i][j]*2
                    for k in range(i+1, len(arr)-1):
                        arr[k][j] = arr[k+1][j]
                    arr[-1][j] = 0
    #down
    if command == 3:
        for j in range(len(arr)):
            temp = []
            for i in range(len(arr)):
                if arr[i][j] != 0:
                    temp.append(arr[i][j])
            temp = [0] * (N - len(temp)) + temp
            for i in range(len(arr)):
                arr[i][j] = temp[i]
            for i in range(len(arr)-1, 0, -1):
                if arr[i][j] == arr[i-1][j]:
                    arr[i][j] = arr[i][j]*2
                    for k in range(i-1, 0, -1):
                        arr[k][j] = arr[k-1][j]
                    arr[0][j] = 0
    if cnt == 5:
        maxResult = 0
        for i in range(N):
            for j in range(N):
                maxResult = max(maxResult, arr[i][j])
        result.append(maxResult)
        return

    for i in range(4):
        dfs(i, cnt+1, [arr[j][:] for j in range(N)])

for i in range(4):
    dfs(i, 1, [arr[j][:] for j in range(N)])

print(max(result))

