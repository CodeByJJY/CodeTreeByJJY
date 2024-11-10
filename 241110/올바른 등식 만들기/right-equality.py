MIN_M = 0
MAX_M = 40

OFFSET = 20

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
a = [
    0
    for _ in range(n + 1)
]

# dp[i][j] :
# i번째 숫자까지 고려해봤을 때
# 계산 결과가 j가 나오는
# 서로 다른 가짓수
dp = [
    [0 for _ in range(MIN_M, MAX_M + 1)]
    for _ in range(n + 1)
]


def initialize():
    for i in range(n + 1):
        for j in range(MIN_M, MAX_M + 1):
            dp[i][j] = 0
    dp[0][0 + OFFSET] = 1

m += OFFSET

given_seq = list(map(int, input().split()))
a[1:] = given_seq[:]

initialize()

for i in range(1, n + 1):
    for j in range(MIN_M, MAX_M + 1):
        if j + a[i] <= MAX_M:
            dp[i][j] += dp[i - 1][j + a[i]]
        if j - a[i] >= MIN_M:
            dp[i][j] += dp[i - 1][j - a[i]]

print(dp[n][m])