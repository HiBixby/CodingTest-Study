def solution(s):
    st = []
    for a in s:
        if a == '(':    # 열린 괄호를 만나면 스택에 추가
            st.append(a)
        else:    # 닫힌 괄호를 만나는 경우
            if not st:  # 스택이 비어 있다면
                return False   # 쌍이 없는 잘못된 괄호
            st.pop()

    return False if st else True

print(solution("))))) () "))



