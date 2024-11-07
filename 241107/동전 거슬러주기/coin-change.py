# dp[i]: i원을 만들기 위한 최소 동전의 수.

n, m = map(int, input().split())
coin = list(map(int, input().split()))
dp = [-1] * (m + 1)
dp[0] = 0


for i in range(1, m + 1):
    for cost in coin:
        # (i-cost)원을 만드는 최소 동전의 수 + 1
        if i >= cost and dp[i - cost] != -1:
            if dp[i] == -1 or dp[i] > dp[i-cost] + 1:
                dp[i] = dp[i-cost] + 1


print(dp[m])