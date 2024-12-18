# 1. 수열의 원소들 중 임의로 몇 개를 고른다.
# 2. 순서대로 나열한다.
# 3. 원소들이 계속 증가한다면, "증가 부분 수열"

# N 입력
N = int(input())

# DP 및 수열 배열 선언
dp = [1] * N
arr = list(map(int, input().split()))

# 메인 알고리즘
for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))