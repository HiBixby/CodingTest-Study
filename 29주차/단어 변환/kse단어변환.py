from collections import deque
def check_words(str1,str2): # 단어 변환 가능 여부
    cnt = len(str1)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt -= 1
        if cnt<len(str1)-1 or str1==str2:
            return False
    else:
        return True

def solution(begin, target, words):
    if target not in words: # 변환 가능한 단어에 target(목표 단어)이 없을 경우
        return 0
    queue = deque()
    queue.append((begin,0)) #시작 단어, 변환 횟수

    while queue:
        word, convert_cnt = queue.popleft() # 현재 단어, 현재 변환 횟수
        if word == target:
            return convert_cnt
        for c_word in words:
            if check_words(word,c_word) :
                queue.append((c_word,convert_cnt+1))
    return 0


print(solution("hit","cog", ["hot", "dot", "dog", "lot", "log", "cog"]))