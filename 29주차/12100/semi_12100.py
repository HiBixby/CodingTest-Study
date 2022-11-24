# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램

# 4
# 2 4 16 8
# 8 4 0 0
# 16 8 2 0
# 2 8 2 0
import copy

def dfs(dir):
    global result
    flag = [[False for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            x, y = a, b  # 복사
            if game[x][y] == 0:   # 애초에 옮기려는 수가 없다면 종료
                continue

            nx, ny = x + dx[dir], y + dy[dir]   # 해당 방향으로 한칸 위로 이동한 위치

            if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 범위 벗어 나는 경우
                continue

            while True:
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break

                if game[x][y] != game[nx][ny] and game[nx][ny] != 0:  # 다른 숫자가 나올때까지 전진 진행
                    break

                if not flag[nx][ny] and game[x][y] == game[nx][ny]:  # 합쳐지지 않았고 숫자가 같은경우 합치기
                    game[nx][ny] += game[x][y]
                    game[x][y] = 0
                    flag[nx][ny] = True     # 합쳐진 경우는 다시 합쳐지지 않도록 설정
                elif game[nx][ny] == 0:     # 빈칸인 경우 그냥 이동
                    game[nx][ny] = game[x][y]
                    game[x][y] = 0

                x, y = nx, ny       # 해당 방향으로 전진
                nx, ny = nx + dx[dir], ny + dy[dir]
    print(dir, game)


def move(depth):
    global game, result
    if depth == 5:
        for k in range(N):
            result = max(result, max(game[k]))  # 이동하고 난 배열의 가장 큰 값 찾기
        print(dir, game)
        return

    arr = copy.deepcopy(game)  # 원본 배열의 상태 유지
    for j in range(4):    # 네 방향 이동
        dfs(j)
        move(depth + 1)
        game = copy.deepcopy(arr)    # 재귀 종료시(한 가지가 끝났을 경우) 원본 배열로 복구


N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = 0
dfs(0)
# move(0)
print(result)