def solution(elements):
    sum_elements = [sum(elements)] #우선 이 elements를 다 더한 값을 sum에 넣는다.
    #예제로 따지자면 길이가 5인 연속 부분 수열의 합

    for i in range(len(elements)):
        num = elements[i]
        # 길이가 1인 연속 부분 수열의 합 -> 1,4,7,9를 넣어준다.
        sum_elements.append(num)

        for j in range(len(elements) - 1): # 이외의 부분수열의 합
            if i + 1 >= len(elements): # 최대 길이를 넘어 서면 i를 0으로 만들어준다. 초기화
                i = len(elements) - i - 1
            else:
                i += 1
            num += elements[i]
            sum_elements.append(num)
            # print(sum_elements)

    result = set(sum_elements) # 예제의 1, 모두를 더한 22 등의 중복된 숫자때문에 집합을 써기

    return len(result)

# print(solution([7,9,1,1,4]))