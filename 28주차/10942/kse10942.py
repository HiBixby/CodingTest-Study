n=int(input()) #수열의 크기
num_list= list(map(int, input().split())) # 홍준이가 칠판에 적은 수
m=int(input()) # 홍준이가 한 질문의 개수

dp = [[0] * n for _ in range(n)]
for num in range(n):
    for i in range(n-num):
        j = i + num
        if i == j: # 원소가 하나일때
            dp[i][j] = 1
        elif num_list[i] == num_list[j]: #처음과 끝이 같을 때
            # 원소가 두개일 때
            if j - i == 1:
                dp[i][j] = 1
            else: # 가운데 확인
                if dp[i+1][j-1] == 1:
                    dp[i][j] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
# n=int(input()) #수열의 크기
# num_list= list(map(int, input().split())) # 홍준이가 칠판에 적은 수
# m=int(input())
# se_list=[]*m
# for _ in range(m):
#     se_list.append(list(map(int, input().split()))) # 홍준이가 명우에게 한 질문 SE
#
# def _palindrome(num_list):
#     reversed_list=num_list[::-1]
#     if num_list == reversed_list:
#         return 1
#     else:
#         return 0
#
# answer_list=[] # 회문인지 아닌지 구분
#
# for temp in se_list:
#     temp_str=num_list[temp[0]-1:temp[1]]
#     if len(temp_str)==1:
#         answer_list.append(1)
#     elif temp_str[0] == temp_str[-1]:
#         if len(temp_str)==2:
#             answer_list.append(1)
#         else:
#             answer_list.append(_palindrome(temp_str))
#     else:
#         answer_list.append(_palindrome(temp_str))
#     # print(temp_str)
#
# print(*answer_list, sep='\n')