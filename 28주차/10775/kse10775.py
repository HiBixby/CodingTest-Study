g = int(input().rstrip())
p = int(input().rstrip())

count = 0
gi = []
for i in range(p):
    gi.append(int(input().rstrip()))

plane_parent = [i for i in range(g+1)]

def find(num):
    # print(plane_parent[num])
    if plane_parent[num] == num: # 이미 채워져있을 경우 다른 값으로 구분되기 때문에 같은 값이라면 채워져있지 않다는 뜻
        return num
    plane_parent[num] = find(plane_parent[num])
    return plane_parent[num]

for plane in gi:
    temp = find(plane)
    if temp == 0:
        break
    plane_parent[temp] = plane_parent[temp-1]  # 여기엔 이미 비행기가 지정되었으므로 다른 값으로 채워줌
    count += 1

print(count)