from copy import deepcopy

def dfs(k, dungeons, idx, cnt): #현재 나의 피로도, 이제 탐험할 던전, 현재까지 탐험한 던전 수
    global max_value
    global min_value

    if idx == min_value: #탐험 끝 모든 던전 다 돌았을 시.
        max_value = max(cnt, max_value)
        return

    if k >= dungeons[idx][0]: #현재 피로도에 해당하는 던전이면,,
        dfs(k - dungeons[idx][1], dungeons, idx + 1, cnt + 1) # 일단 피로도(dungeons[idx][1]) 깎고 탐험ㄱ

    dfs(k, dungeons, idx + 1, cnt) #현재 던전을 탐험하지 않는 경우 탐험 ㄱ


def solution(k, dungeons):
    global max_value # 내가 탐험한 최대 던전 수
    max_value = 0

    global min_value    # 던전 수
    min_value = len(dungeons)
    dungeons.sort(key = lambda x : x[0]-x[1], reverse = True) #x[0]이 최소 필요 피로도, x[1]이 소모피로도 ㅇ\차이가 가장 큰게 기회가 만호아지므로

    dfs(k, dungeons, 0, 0)

    return max_value
# print(solution(80, [[80, 10], [70, 10], [60, 50], [10, 10]]))
print(solution(80, [[80,20],[50,40],[30,10]]))