import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]
lis = [a[0]]

def findPlace(e):
    start = 0
    end = len(lis) - 1

    while start <= end:
        mid = (start + end) // 2

        if lis[mid] == e:
            return mid
        elif lis[mid] < e:
            start = mid + 1
        else:
            end = mid - 1

    return start # e보다 크거나 같은 원소를 처음 만났을 때의 인덱스 반환

for item in a:
    if lis[-1] < item: # item이 lis의 마지막 원소보다 큰 경우
        lis.append(item) # 바로 lis에 item을 추가
    else: # item이 lis의 마지막 원소보다 작거나 같은 경우
        idx = findPlace(item) # findPlace()로 item을 넣을 인덱스를 찾아서 거기에 넣는다
        lis[idx] = item # 가장 긴 수열을 찾아야 하기 때문에 인덱스에 값을 넣어줌

print(len(lis)) # for문을 다 돌고 나서 lis리스트의 길이를 출력