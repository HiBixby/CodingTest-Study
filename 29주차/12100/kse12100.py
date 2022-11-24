#왜 안 돼

import sys, copy
import queue
from collections import deque

input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

"""
예제를
2 2 4
4 4 4
8 8 2
로 들겠음
"""
def get_max_value(matrix):
    result=0
    for i in range(n):
        for j in range(n):
            result=max(result, matrix[i][j])

    return result


maxValue=0
def move(dir, round, matrix):
    global maxValue
    if round==5:
        return
    board_copy = copy.deepcopy(matrix)

    if dir == 0: # 왼쪽으로 밀었을 때 ex) 스택에 2,2,4 이렇게 들어갈때
        for i in range(n):
            q = deque()
            s=[]
            for j in range(n-1, 0,-1):
                now=board_copy[i][j]
                if not now==0: s.append(now) # 한줄을 스택에 넣어주기
            for j in range(n):
                board_copy[i][j]=0
            while not len(s)==0:
                first=s[-1] #제일 마지막에 들어간 값 빼내오기 (LIFO를 가지는 스택 특 땜시)
                s.pop() #하나 빼기
                if len(s)==0: q.append(first) #만약 하나 뺐는데 비어 있다? 그럼 그 값은 그대로 q에
                else:
                    second=s[-1] #이미 하나 빼왔기 때문에 마지막에서 두번째 값 넣어주기
                    s.pop() #second 로 들어간 값 빼기
                    if first==second:#만약 같으면? 둘이 더해주고 q에 넣어준다.
                        q.append(first+second)
                    else: #만약 같지 않으면? 하나는 q에 넣어주고 두번째거 다시 스택에 넣어서 또 비교하기 준비
                        q.append(first)
                        s.append(second)
            j=0
            while not len(q)==0:
                now=q.popleft()
                board_copy[i][j]=now
                j+=1
    elif dir == 1: # 오른쪽으로 밀었을 때 ex) 스택에 4,2,2 이렇게 들어갈때
        for i in range(n):
            q = deque()
            s=[]
            for j in range(n):
                now=board_copy[i][j]
                if not now==0: s.append(now) # 한줄을 스택에 넣어주기
            for j in range(n):
                board_copy[i][j]=0
            while not len(s)==0:
                first=s[-1] #제일 마지막에 들어간 값 빼내오기 (LIFO를 가지는 스택 특 땜시)
                s.pop() #하나 빼기
                if len(s)==0: q.append(first) #만약 하나 뺐는데 비어 있다? 그럼 그 값은 그대로 q에
                else:
                    second=s[-1] #이미 하나 빼왔기 때문에 마지막에서 두번째 값 넣어주기
                    s.pop() #second 로 들어간 값 빼기
                    if first==second: #만약 같으면? 둘이 더해주고 q에 넣어준다.
                        q.append(first+second)
                    else: #만약 같지 않으면? 하나는 q에 넣어주고 두번째거 다시 스택에 넣어서 또 비교하기 준비
                        q.append(first)
                        s.append(second)
            j=n-1
            while not len(q)==0:
                now=q.popleft()
                board_copy[i][j]=now
                j-=1

    elif dir == 2:  # 위쪽으로 밀었을 때 ex) 스택에 2,4,8 이렇게 들어갈때
        for j in range(n):
            q = deque()
            s=[]
            for i in range(n-1, 0,-1):
                now=board_copy[i][j]
                if not now==0: s.append(now) # 한줄을 스택에 넣어주기
            for i in range(n):
                board_copy[i][j]=0
            while not len(s)==0:
                first=s[-1] #제일 마지막에 들어간 값 빼내오기 (LIFO를 가지는 스택 특 땜시)
                s.pop() #하나 빼기
                if len(s)==0: q.append(first) #만약 하나 뺐는데 비어 있다? 그럼 그 값은 그대로 q에
                else:
                    second=s[-1] #이미 하나 빼왔기 때문에 마지막에서 두번째 값 넣어주기
                    s.pop() #second 로 들어간 값 빼기
                    if first==second: #만약 같으면? 둘이 더해주고 q에 넣어준다.
                        q.append(first+second)
                    else: #만약 같지 않으면? 하나는 q에 넣어주고 두번째거 다시 스택에 넣어서 또 비교하기 준비
                        q.append(first)
                        s.append(second)
            i=0
            while not len(q)==0:
                now=q.popleft()
                board_copy[i][j]=now
                i+=1
    elif dir==3: # 위쪽으로 밀었을 때 ex) 스택에 8,4,2 이렇게 들어갈때
        for j in range(n):
            q = deque()
            s=[]
            for i in range(n):
                now=board_copy[i][j]
                if not now==0: s.append(now) # 한줄을 스택에 넣어주기
            for i in range(n):
                board_copy[i][j]=0
            while not len(s)==0:
                first=s[-1] #제일 마지막에 들어간 값 빼내오기 (LIFO를 가지는 스택 특 땜시)
                s.pop() #하나 빼기
                if len(s)==0: q.append(first) #만약 하나 뺐는데 비어 있다? 그럼 그 값은 그대로 q에
                else:
                    second=s[-1] #이미 하나 빼왔기 때문에 마지막에서 두번째 값 넣어주기
                    s.pop() #second 로 들어간 값 빼기
                    if first==second: #만약 같으면? 둘이 더해주고 q에 넣어준다.
                        q.append(first+second)
                    else: #만약 같지 않으면? 하나는 q에 넣어주고 두번째거 다시 스택에 넣어서 또 비교하기 준비
                        q.append(first)
                        s.append(second)
            i=n-1
            while not len(q)==0:
                now=q.popleft()
                board_copy[i][j]=now
                i-=1

    maxValue=max(maxValue, get_max_value(board_copy))
    for x in range(4):
        move(x, round+1, board_copy)

for i in range(4):
    move(i,0,a)

print(maxValue)