n, m = map(int, input().split())
weight, value = [], []
for _ in range(n):
    w, v = tuple(map(int, input().split()))
    weight.append(w)
    value.append(v)

dp = [0] * (m + 1) # dp[i] : 지금까지 고른 보석 무게의 합이 i일 때
                   #         얻을 수 있는 최대 가치
dp[0] = 0


for i in range(1, m + 1):
    for j in range(n):
        if i >= weight[j]:
            dp[i] = max(dp[i], dp[i - weight[j]] + value[j])

ans = 0
for i in range(m + 1):
    ans = max(ans, dp[i])

print(ans)