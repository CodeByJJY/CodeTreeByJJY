n = int(input())

dp = [0] * (n + 1)

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()

# 점화식
dp[1], dp[2] = 1, 2
for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n]%10007)