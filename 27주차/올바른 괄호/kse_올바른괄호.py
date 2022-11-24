
def solution(s):
    answer = True
    stack=[]
    for i in s:
        if i=="(":
            stack.append(i)
        elif i==")":
            if len(stack)==0:
                return False
            stack.pop()

    if len(stack)==0:
        return True
    return False


"""
채점 결과
정확성: 69.5
효율성: 30.5
합계: 100.0 / 100.0
"""