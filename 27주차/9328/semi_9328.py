# 상근이가 훔칠 수 있는 문서의 최대 개수를 구하는 프로그램

def unlock(a, b):
    for key in keys:  # 문을 열 수 있는 열쇠가 있는지 확인
        new_key = key.upper()
        if new_key == arr[a][b]:  # 문을 열 수 있다면 열음 처리 후 재탐색
            return True
    return False


def is_distinct():
    for x, y in start:  # 같은 소문자가 여러번 들어가는 경우 방지 => 고쳐야함
        if temp[j] == arr[x][y]:
            return False
    return True


def dfs(a, b):
    global result
    st = [(a, b)]
    visited = [[False for _ in range(w)] for _ in range(h)]  # 방문 배열
    visited[a][b] = True

    if arr[a][b].isupper() and not unlock(a, b):   # 시작이 문일 경우 패스
        return
    elif arr[a][b].islower():   # 시작이 열쇠일 경우 바로 먹기
        keys.append(arr[a][b])
        visited[a][b] = True

    while st:
        x, y = st.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '*' and not visited[nx][ny]:
                if arr[nx][ny] == '.':   # 다음 노드가 빈 공간이면 이동
                    st.append((nx, ny))
                elif 65 <= ord(arr[nx][ny]) <= 90:
                    if unlock(nx, ny):     # 문을 열 수 있는 열쇠가 있는지 확인
                        arr[nx][ny] = '.'
                        st.append((nx, ny))
                elif arr[nx][ny] == '$':        # 문서를 만난 경우, 결과값 증가 후 재탐색
                    result += 1
                    st.append((nx, ny))
                else:              # 열쇠를 만났 다면 주워서 빈 공간 으로 만들고 가지고 있는 열쇠 배열에 추가
                    st.append((nx, ny))  # 새로운 열쇠를 얻었으니 다시 재탐색
                    if arr[nx][ny] in keys:  # 같은 열쇠를 또 얻은 경우는 재 탐색만 하되, 문서의 중복 방문을 막기 위해 방문 배열 초기화 하지 않음
                        arr[nx][ny] = '.'
                        continue

                    visited = [[False for _ in range(w)] for _ in range(h)]  # 방문 배열 초기화(새로운 길이 열리 므로)
                    keys.append(arr[nx][ny])
                    arr[nx][ny] = '.'
                visited[nx][ny] = True


T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    arr = [['' for _ in range(w)] for _ in range(h)]
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    start = []
    result = 0

    for i in range(h):   # 지도
        temp = list(input())
        for j in range(w):
            if i == 0 or j == 0 or i == h-1 or j == w-1:  # 들어갈 수 있는 빈 공간 혹은 방이 있는? 열쇠가 있는 시작점 저장
                if temp[j] == '.':
                    start.append((i, j))
                elif temp[j].isalpha() and is_distinct():   # 같은 소문자가 여러번 들어가는 경우 방지
                    start.append((i, j))
                elif temp[j] == '$':
                    result += 1
            arr[i][j] = temp[j]

    start.sort(key=lambda x: (arr[x[0]][x[1]] == '.', arr[x[0]][x[1]]), reverse=True)  # . -> 소문자 -> 대문자 순서
    keys = list(input())
    for a, b in start:
        dfs(a, b)        # 빈 공간이 없을 경우 열쇠를 먼저 먹기 위해 소문자 => 대문자 정렬
    print(result)