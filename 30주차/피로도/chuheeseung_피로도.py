from itertools import permutations # dungeons 길이 8 -> 순열 사용

def solution(k, dungeons):
    answer = 0
    len_dungeons = len(dungeons)

    for per in permutations(dungeons, len_dungeons): # 순열 -> 경우의 수 생성
        temp_k = k # k를 그대로 냅두기 위해 temp_k 생성
        count = 0 # 던전의 개수

        for p in per:
            if temp_k >= p[0]: # 최소 필요 피로도 만족하는 경우
                temp_k -= p[1] # 소모 피로도 빼기
                count += 1 # 탐색한 던전 수 + 1

        answer = max(answer, count) # 탐험한 던전 수 업데이트
    return answer

# k = 80
# dungeons = [[80, 20], [50, 40], [30, 10]]
# answer = solution(k, dungeons)
# print(answer)