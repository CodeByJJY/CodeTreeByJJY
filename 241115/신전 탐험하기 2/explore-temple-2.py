n = int(input())
treasures = [list(map(int, input().split())) for _ in range(n)]

# DP 배열 초기화
dp = [[0] * 3 for _ in range(n)]
dp[0][0] = treasures[0][0]
dp[0][1] = treasures[0][1]
dp[0][2] = treasures[0][2]

# 1층부터 n층까지 DP 테이블 채우기
for i in range(1, n):
    dp[i][0] = treasures[i][0] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = treasures[i][1] + max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = treasures[i][2] + max(dp[i-1][0], dp[i-1][1])

# 마지막 층에서 첫 번째 층의 선택과 같은 방을 제외하고 최대값 찾기
result = 0
result = max(dp[n-1][0], dp[n-1][1], dp[n-1][2])

print(result)
