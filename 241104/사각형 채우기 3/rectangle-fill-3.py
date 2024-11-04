# 입력
n = int(input())

# Bottom-up
dp = [0] * (n + 1)

if n == 1:
    print(2)
    exit()
elif n == 2:
    print(7)
    exit()

dp[1], dp[2] = 2, 7
for i in range(3, n + 1):
    dp[i] = 2 * dp[i-1] + dp[i-2]

print(dp[n] % 1000000007)