n = int(input())

dp = [0] * (n + 1)

if n == 2 or n == 3:
    print(1)
else:
    dp[2], dp[3] = 1, 1
    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]

    print(dp[n])