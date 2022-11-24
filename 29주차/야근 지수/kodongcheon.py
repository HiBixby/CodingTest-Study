def solution(n, works):
    worksSum = sum(works) - n
    if worksSum <= 0:
        return 0
    works.sort(reverse=True)

    while n > 0:
        for i in range(len(works)):
            if n == 0:
                break
            works[i] -= 1
            n -= 1
            if i == len(works) - 1:
                break
            if works[i] >= works[i + 1]:
                break
    result = 0
    for i in range(len(works)):
        result += works[i] ** 2
    return result