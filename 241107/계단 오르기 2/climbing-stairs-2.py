N = int(input())
A = [0] + list(map(int, input().split()))

dp = [
    [-1] * 4
    for _ in range(N+1)
]

dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(4):
        if i >= 1 and j >= 1 and dp[i-1][j-1] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + A[i])
        if i >= 2 and dp[i-2][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + A[i])

print(max(dp[N]))