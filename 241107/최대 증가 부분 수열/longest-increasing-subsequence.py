import sys

INT_MIN = -sys.maxsize

n = 5
dp = [0]*n              # 점프 횟수 기록
a = [2, 3, 0, 1, 4]     # 판

def initialize():
    for i in range(n):
        dp[i] = INT_MIN
    
    dp[0] = 0

initialize()

for i in range(1, n):
    for j in range(0, i):
        if dp[j] == INT_MIN:
            continue

        if j + a[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans)