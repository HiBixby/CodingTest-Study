row,col = map(int, input().split())

arr=[input() for _ in range(row)]
check=[[0 for j in range(col)] for i in range(row)]
visit=[[-1 for j in range(col)] for i in range(row)]
print(check)
result=0

dx=[0,1,0,-1]
dy=[-1,0,1,0]

def dfs(y,x):

    global result
    global check
    global visit

    visit[y][x]=1
    ny=y+dy[check[y][x]]
    nx=x+dx[check[y][x]]

    if visit[ny][nx]==1:
        result+=1
    if visit[ny][nx]==0:
        dfs(ny,nx)
    visit[y][x]=2

for i in range(row):
    for j in range(col):
        if arr[i][j]=='U': check[i][j]=1
        elif arr[i][j]=='R': check[i][j]=2
        elif arr[i][j]=='L': check[i][j]=3

for i in range(row):
    for j in range(col):
        if visit[i][j]==0:
            dfs(i,j)
print(result)

