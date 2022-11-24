def solution(n, s):
    A = s//n
    B = s%n
    result = [A for i in range(n)]
    i = 0
    for _ in range(B):
        result[i] += 1
        i+=1
        if i == len(result):
            i = 0
    if 0 in result:
        return [-1]
    else:
        return sorted(result)