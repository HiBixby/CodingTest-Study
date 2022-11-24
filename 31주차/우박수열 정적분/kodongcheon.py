def solution(k, ranges):
    arr = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        arr.append(k)
    arr2 = []
    for i in range(len(arr)-1):
        area = min(arr[i], arr[i+1]) + abs(arr[i+1] - arr[i]) / 2
        arr2.append(area)
    result = []
    for a, b in ranges:
        if a > len(arr2) + b:
            result.append(-1.0)
        else:
            result.append(sum(arr2[a:len(arr2)+b]))
    return result