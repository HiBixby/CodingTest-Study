def solution(t):
    for i in range(len(t)-2,-1,-1):
        for j in range(i+1):t[i][j]+=max(t[i+1][j],t[i+1][j+1])
    return t[0][0]