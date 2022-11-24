# 첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)
import sys
sys.setrecursionlimit(10**7)

def drawing_star(n, x, y):
    if n == 3:  # 높이가 3이라면 별을 만들어 출력한다.
        star[y][x] = "*"
        star[y + 1][x - 1] = "*"
        star[y + 1][x + 1] = "*"
        star[y + 2][x - 2] = "*"
        star[y + 2][x - 1] = "*"
        star[y + 2][x] = "*"
        star[y + 2][x + 1] = "*"
        star[y + 2][x + 2] = "*"
    else:
        drawing_star(n // 2, x, y)  # 위의 삼각형 높이와 맨 위꼭대기 좌표를 보낸다.
        drawing_star(n // 2, x - (n // 2), y + (n // 2))  # 왼쪽 하단 삼각형 높이와 맨 위 꼭대기 좌표를 보낸다.
        drawing_star(n // 2, x + (n // 2), y + (n // 2))  # 오른쪽 하단 삼각형 높이와 맨 위 꼭대기 좌표를 보낸다.


N = int(input())
star=[[' ']*(N*2) for _ in range(N)]

drawing_star(N, N-1, 0) #삼각형의 높이와 삼각형 맨 위 꼭지점 좌표를 매개변수로 넘긴다.

for i in star:
    print(''.join(i))

#에러/오류 사항
#RecursionError: maximum recursion depth exceeded in comparison

# PyPy3로 안돌아감 -> 메모리 초과됨/Python38로 해결