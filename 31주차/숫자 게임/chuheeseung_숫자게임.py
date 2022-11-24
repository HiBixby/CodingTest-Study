def solution(A, B):
    answer = 0

    A.sort(reverse=True) # 내림차순으로 정렬
    B.sort(reverse=True)

    i = 0
    for a in A:
        if a < B[i]: # B[i]가 A보다 값이 클 때만 answer + 1, 인덱스i + 1
            answer += 1
            i += 1

    return answer

# A = [5, 1, 3, 7]
# B = [2, 2, 6, 8]
# answer = solution(A, B)
# print(answer)