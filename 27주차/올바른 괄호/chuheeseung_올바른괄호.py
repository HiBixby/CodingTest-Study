def solution(s):
    OPEN = '('
    CLOSE = ')'
    count = 0

    for char in s:
        if char == OPEN: # 열린 괄호가 나오면 + 1
            count += 1
        if char == CLOSE: # 닫힌 괄호가 나오면 - 1
            count -= 1

        if count < 0: # count가 0보다 작아지면 이미 닫힌 괄호가 먼저 나와서 짝이 맞지 않는다는 뜻 -> 바로 False
            return False

    return count == 0 # True 반환 안함 <- 열린 괄호로 끝나는 경우도 존재하기 때문에 여기서 판단

# s = "()()"
# s = "(()("
# answer = solution(s)
# print(answer)