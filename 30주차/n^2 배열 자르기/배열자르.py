# def solution(n, left, right):
#     answer = []
#     arr = [[0] * n for _ in range(n)]
#
#     for x in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if i==x or j==x:
#                     arr[i][j]=x+1
#     list_arr = sum(arr, [])
#     answer=list_arr[left:right+1]
#
#     return answer

def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer