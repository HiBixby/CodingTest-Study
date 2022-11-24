def solution(arrayA, arrayB):
    arrayA.sort()
    arrayB.sort()

    checkA = arrayA[0]
    checkB = arrayB[0]

    arrA = [checkA]
    arrB = [checkB]

    result = []

    for i in range(checkA // 2, 1, -1):
        if checkA % i == 0:
            arrA.append(i)

    for i in range(checkB // 2, 1, -1):
        if checkB % i == 0:
            arrB.append(i)

    #     tempA = list(set(arrA) - set(arrB))
    #     tempB = list(set(arrB) - set(arrA))

    #     arrA = sorted(tempA, reverse=True)
    #     arrB = sorted(tempB, reverse=True)

    #     dpA = []
    #     dpB = []

    # for k in arrA:
    #     flag = False
    #     for i in dpA:
    #         if i % k == 0:
    #             flag = True
    #     if not flag:
    #         for i in arrayA:
    #             if i % k != 0:
    #                 break
    #         else:
    #             dpA.append(k)
    #             for i in arrayB:
    #                 if i % k == 0:
    #                     break
    #             else:
    #                 result.append(k)
    #                 break
    #     else:
    #         for i in arrayB:
    #             if i % k == 0:
    #                 dpA.append(k)
    #                 break
    #         else:
    #             result.append(k)
    #             break
    # else:
    #     result.append(0)

    for k in arrA:
        for i in arrayA:
            if i % k != 0:
                break
        else:
            for i in arrayB:
                if i % k == 0:
                    break
            else:
                result.append(k)
                break
    else:
        result.append(0)

    for k in arrB:
        for i in arrayB:
            if i % k != 0:
                break
        else:
            for i in arrayA:
                if i % k == 0:
                    break
            else:
                result.append(k)
                break
    else:
        result.append(0)

    return max(result)