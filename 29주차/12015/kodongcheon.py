from bisect import bisect_left

n = int(input())
cases = list(map(int, input().split()))
lis = [0]

for case in cases:
    if lis[-1] < case:
        lis.append(case)
    else:
        i = bisect_left(lis, case)
        lis[i] = case

print(len(lis) - 1)

