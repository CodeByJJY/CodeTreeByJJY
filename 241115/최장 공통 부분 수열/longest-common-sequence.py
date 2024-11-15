A = input().strip()
B = input().strip()
len_A, len_B = len(A), len(B)

# DP 테이블 초기화
dp = [
    [0 for _ in range(len_B + 1)]
    for _ in range(len_A + 1)
]

# LCS 계산
for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        if A[i - 1] == B[j - 1]:  # 문자가 같다면 이전 값에 1을 더함
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:  # 문자가 다르면 이전 값 중 최댓값을 가져옴
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS 길이
lcs_length = dp[len_A][len_B]

# 최소 삭제 횟수 계산
result = (len_A - lcs_length) + (len_B - lcs_length)
print(result)
