def solution(triangle):
    dp = [[0]+i+[0] for i in triangle] #삼각형 처음과 맨끝에 0을 넣어준다 즉 0으로 감싸준다.

    for x in range(1,len(dp)):
        for y in range(1,len(dp[x])-1):
            dp[x][y]+=max(dp[x-1][y-1],dp[x-1][y])
    print(dp) # 합산된 결과들이 들어가 있는
    return max(dp[-1]) #그 중 맨 마지막에서 가장 큰 값만

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))