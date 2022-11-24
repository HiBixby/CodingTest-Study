n=int(input())
a_list=list(map(int, input().split(' ')))
# n=4
# a_list=[10,20,30,15]
# a_list=[10,20,10,30,20,50]
temp=[a_list[0]]

for i in range(1, len(a_list)):
    #일단 추가 큰값은 하나씩 추가
    if temp[-1]<a_list[i]:
        temp.append(a_list[i])
        # print(*temp)
    else:
        num=0
        temp_len=len(temp)
        #이분 탐색하기(정렬된 배열에서의 중간 지점을 찾아서 그 부분부터 분별)
        while num <temp_len:
            mid=(num+temp_len)//2
            #만약 그 중간값이 구별하려는 값보다 작으면 대치를 하기 위해서 num에 mid+1을 대입
            #ex) 10,20,30,15 이 있으면 10보다 15가 크다는걸 보고 그 다음 인덱스값인 20과 15를 바꿈
            if temp[mid]<a_list[i]:
                num=mid+1
            else:
                temp_len=mid
        temp[num]=a_list[i] #바꾸기
print(len(temp))