from collections import defaultdict

N, V = map(int, input().split())
item = []

for _ in range(N):
    a, b = map(int, input().split())
    item.append((a,b))

dp = defaultdict(int) #0초기화된 디셔너리로

for w,v in item:
    if w > V:
        continue

    for in_w, in_v in list(dp.items()):
        temp_w = in_w + w
        if temp_w <= V:
            dp[temp_w] = max(dp[temp_w], in_v + v)

    dp[w] = max(dp[w], v)

dp_l = list(dp.items())
score = 0
for a,b in dp_l:
    if a <= V:
        score = max(score, b)

print(score)