def solution(elements):
    elements = elements + elements
    arr = []
    for i in range(1, len(elements)//2+1):
        for j in range(len(elements)//2):
            arr.append(sum(elements[j:j+i]))
    return len(set(arr))