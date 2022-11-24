def collatz(k):
    points = [k]

    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + 1

        points.append(k)

    return points


def solution(k, ranges):
    points = collatz(k)
    answer = []

    for a, b in ranges:
        c = len(points) + b - 1

        if a > c:
            answer.append(-1)
        else:
            temp = 0

            for i in range(a, c):
                temp += (points[i] + points[i + 1]) / 2

            answer.append(temp)
    return answer

# k = 5
# ranges = [[0,0],[0,-1],[2,-3],[3,-3]]
# answer = solution(k, ranges)
# print(answer)