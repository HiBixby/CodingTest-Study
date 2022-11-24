
def solution(m, n, puddles):
    area=[[0 for j in range(m+1)] for i in range(n+1)] # 지역을 모두 1로 초기화

    area[1][1]=1 # 시작점은 1부터 처리
    for pud in puddles:
        area[pud[1]][pud[0]]=-1 #물 웅덩이 있는 위치를 -1으로

    for i in range(1,n+1): # 좌표로 되어 있어서 1부터 ㄱ
        for j in range(1,m+1):
            if i==1 and j==1: #시작점 처리
                continue
            if area[i][j]==-1: #물 웅덩이 있는지
                area[i][j]=0
            else: #갈 수 있는 경로
                area[i][j]=(area[i-1][j]+area[i][j-1])%1000000007 #최단거리로 갈때마다 그 때의 경우의 수에 나머지 계산
    return area[-1][-1] #도착지점까지 합산한 값

m=4
n=3
puddles=[[2,2]]
print(solution(m, n, puddles))


