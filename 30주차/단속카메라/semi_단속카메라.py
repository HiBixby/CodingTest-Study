def solution(routes):
    arr = sorted(routes, key=lambda x: x[1])  # 끝나는 시간 기준 오름차순 정렬

    count, latest_camera = 0, 0
    for i in range(len(arr) - 1):
        if i == 0:
            latest_camera = arr[i][1]    # 카메라 초기 위치값 설정
            count += 1

        if latest_camera < arr[i + 1][0]:  # 끝나는 시점과 다음 차량의 시작 시점이 겹치지 않는 경우
            latest_camera = arr[i + 1][1]  # 카메라 위치 갱신 필요
            count += 1      # 필요한 단속 카메라 수 증가

    return count

