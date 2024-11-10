import sys

# 큰 음수로 초기화
INT_MIN = -sys.maxsize

# n과 m을 입력받음 (n은 일의 수, m은 고려할 최대 일수)
n, m = map(int, input().split())

# s, e, v 배열 초기화 (시작일, 종료일, 가치)
s = [0] * (n + 1)
e = [0] * (n + 1)
v = [0] * (n + 1)

# dp 배열 초기화
dp = [[0] * (n + 1) for _ in range(m + 1)]

# s, e, v 입력받음
for i in range(1, n + 1):
    s[i], e[i], v[i] = map(int, input().split())

# dp 초기화 함수
def initialize():
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[j] == 1:  # 시작일이 1일 경우
                dp[i][j] = 0

initialize()

# dp 계산
for i in range(2, m + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if s[k] <= i - 1 <= e[k] and s[j] <= i <= e[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(v[j] - v[k]))

# 결과 계산 및 출력
ans = max(dp[m][1:n + 1])
print(ans)