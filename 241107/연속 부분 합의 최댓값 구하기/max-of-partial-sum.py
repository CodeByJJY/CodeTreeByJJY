# dp[i]: i로 끝나는 연속부분수열의 합 중 최대
# dp[i]
# 1. 마지막 원소 혼자 있는 경우
#   - A[i]
# 2. 둘 이상 묶이는 경우.
#   - A[i] + D[i-1]

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    dp[i] = A[i]
    if i>=1 and A[i] + dp[i-1] > dp[i]:
        dp[i] = A[i] + dp[i-1]

print(max(dp))