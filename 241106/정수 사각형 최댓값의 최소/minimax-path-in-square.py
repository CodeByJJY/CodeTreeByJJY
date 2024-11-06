import sys

# 입력
N = int(input())

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
        dp[i][0] = max(dp[i-1][0], grid[i][0])
    for i in range(1, N):
        dp[0][i] = max(dp[0][i-1], grid[0][i])

initialize()

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[N-1][N-1])