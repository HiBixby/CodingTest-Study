def solution(routes):
    routes.sort(key = lambda x: x[1]) # 고속도로를 나간 지점을 기준으로 정렬
    # 처음으로 빠져나가는 차량 시간에 카메라 설치 -> 이 시간 사이에 있는 차량은 볼 필요 없어짐
    camera = [routes[0][1]]

    for k in range(1, len(routes)): # 첫번째 차량은 봤으니까 1부터 시작
        if routes[k][0] <= camera[-1] and routes[k][1] >= camera[-1]:
            # routes 시간이 camera 배열 사이에 있으면 패스 (카메라 추가할 필요 없음)
            continue
        else:
            camera.append(routes[k][1])

    return len(camera) # 카메라 리스트의 원소 개수를 출력

# routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
# answer = solution(routes)
# print(answer)

# routes[i][0] : i번째 차량이 고속도로에 진입한 지점
# routes[i][1] : i번째 차량이 고속도로에서 나간 지점