from itertools import permutations
# def solution(k, dungeons):
#     a = [i for i in range(len(dungeons))]
#     permute = list(permutations(a, len(dungeons)))
#     result = 0
#     for num_list in permute:
#         temp_k = k
#         temp_result = 0
#         for num in num_list:
#             if temp_k < dungeons[num][0]:
#                 break
#             temp_k -= dungeons[num][1]
#             temp_result += 1
#         result = max(temp_result, result)

#     return result

def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons, len(dungeons)):
        status = k
        cnt = 0
        for needs, use in i:
            if status >= needs:
                status -= use
                cnt += 1
        answer = max(answer, cnt)
    return answer