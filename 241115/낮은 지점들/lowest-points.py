# 입력 처리
n = int(input())  # 점의 개수
points = [tuple(map(int, input().split())) for _ in range(n)]  # 각 점의 좌표 입력

# 딕셔너리를 사용하여 동일한 x 좌표에 대해 가장 작은 y 값을 저장
x_to_min_y = {}

for x, y in points:
    # 현재 x 좌표가 딕셔너리에 없다면 추가
    # 이미 존재한다면 최소 y 값만 유지
    if x not in x_to_min_y or y < x_to_min_y[x]:
        x_to_min_y[x] = y

# 남아있는 점들의 y 값의 합 계산
y_sum = sum(x_to_min_y.values())

# 결과 출력
print(y_sum)
