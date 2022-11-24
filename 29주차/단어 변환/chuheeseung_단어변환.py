from collections import deque

def solution(begin, target, words):
    if target not in words: # words 리스트에 target이 없으면 0 반환
        return 0

    q = deque()
    q.append([begin, 0])

    while q:
        x, cnt = q.popleft() # 단어랑 개수를 큐에서 뽑는다

        if x == target: # target이 되면 cnt값 반환
            return cnt

        for i in range(0, len(words)):
            diff = 0
            word = words[i] # words 리스트에서 i번째를 word로 둔다

            for j in range(len(x)): # x의 문자열 길이만큼 for문 반복
                if x[j] != word[j]: # x[j]와 word[j] 문자를 비교해 나간다
                    diff += 1

            if diff == 1: # x와 word가 문자 하나만 다른 경우
                q.append([word, cnt + 1]) # q에 word를 추가

    return 0

# begin = "hit"
# target = "cog"
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# answer = solution(begin, target, words)
# print(answer)