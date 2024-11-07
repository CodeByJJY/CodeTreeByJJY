# 입력
n = int(input())
MOD = 1000000007
dp = [0] * (n + 1)

# 초기화
dp[0] = 1
dp[1] = 2
if n == 1:
    print(dp[1])
else:
    dp[2] = 7

    # 계산
    for i in range(3, n + 1):
        dp[i] = 2*dp[i-1] + 3*dp[i-2]
        for j in range(3, i + 1):
            dp[i] += 2*dp[i-j]

    print(dp[n]%MOD)