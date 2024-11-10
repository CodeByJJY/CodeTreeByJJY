import sys

MAX_ANS = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# dp[i] : 지금까지 선택한 수들의 합이 i일 때, 
#         가능한 최소 수열의 길이
dp = [0] * (m + 1)


def initialize():
    for i in range(m + 1):
        dp[i] = MAX_ANS
    dp[0] = 0

   
initialize()

# 각 수들을 선택해봅니다.
for i in range(n):
    for j in range(m, -1, -1):
        if j >= arr[i]:
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

min_len = dp[m]


if min_len == MAX_ANS:
    min_len = -1

print(min_len)