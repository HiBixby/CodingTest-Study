def solution(routes):
    routes.sort(key = lambda x : x[1])
    check = - 30001
    cnt = 0
    for route in routes:
        if route[0] <= check <= route[1]:
            continue
        else:
            check = route[1]
            cnt += 1

    return cnt