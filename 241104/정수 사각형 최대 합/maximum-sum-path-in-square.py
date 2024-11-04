import sys

# 입력
N = int(input())

INT_MIN = -sys.maxsize

# 격자 입력
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
dp = [
    [0 for _ in range(N)]
    for _ in range(N)
]

def initialize():
    dp[0][0] = grid[0][0]

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, N):
        dp[0][i] = dp[0][i-1] + grid[0][i]

initialize()

for i in range(2, N):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

ans = INT_MIN
for i in range(N):
    ans = max(ans, dp[N-1][i])
print(ans)