d=int(input()) #산책을 시작하고나서 지난 시간

route=[
        [0, 1, 0, 0, 0, 0, 0, 1], #정보과학관
        [1, 0, 1, 0, 0, 0, 0, 1], #전산관
        [0, 1, 0, 1, 0, 0, 1, 1], #신양관
        [0, 0, 1, 0, 1, 0, 1, 0], #진리관
        [0, 0, 0, 1, 0, 1, 0, 0], #학생회관
        [0, 0, 0, 0, 1, 0, 1, 0], #형남공학관
        [0, 0, 1, 1, 0, 1, 0, 1], #한경직기념관
        [1, 1, 1, 0, 0, 0, 1, 0], #미래관
] #행렬 만들어두기

num=1000000007 #나눌값
# d예시 5
def solution(n): # 한번 가는데 1분이니까 n만큼의 변을 거쳐서 갈때 나오는 경우의 수를 구하는 것.
        if n==1:
                return route #1분지나서 도착했다는 것은 걍 출발안한거.
        temp=solution(n//2) #
        if n%2==1:
                return mult(mult(temp,temp), route) #m 행렬을 D번 거듭제곱한거 재귀로 계속 넣어주기
                #5가 예시였다면 (route*route*route)^2
        else:
                return mult(temp,temp)


def mult(a,b): #a, b 두 행렬을 곱한 결과(행렬)을 반환
        spot = [[0] * 8 for _ in range(8)]
        for i in range(8):
                for j in range(8):
                        for x in range(8):
                                spot[i][j]+=a[i][x]*b[x][j]
                        spot[i][j]%=num
        print(spot[0][0])
        return spot #곱한 결과

print(solution(d)[0][0])