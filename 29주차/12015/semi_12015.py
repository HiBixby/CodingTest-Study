# 첫째 줄에 수열 A의 가장 긴 증가 하는 부분 수열의 길이를 출력

def find_place(target):
    l, h = 0, len(lis) - 1

    while l < h:
        mid = (l + h) // 2

        if lis[mid] < target:     # 들어가려는 수보다 현재 배열에 있는 중간값이 같거나 작다면 이분 탐색 통해서 넣어주기
            l = mid + 1
        else:
            h = mid               # 들어가려는 수보다 현재 배열의 중간값이 크다면 그 자리로 들어 가기
    return h


N = int(input())
arr = list(map(int, input().split()))
lis = [0]

for num in arr:
    if lis[-1] < num:    # 배열의 가장 큰 수보다 크다면 바로 끝에 삽입
        lis.append(num)
    else:                # 작은 수의 경우는 이분 탐색을 통해 위치 결정 후 삽입
        lis[find_place(num)] = num    # 큰 값을 작은 값으로 덮어 씌우기
    print(lis)

print(len(lis) - 1)
