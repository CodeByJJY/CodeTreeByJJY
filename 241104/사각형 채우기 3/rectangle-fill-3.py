MOD = 1000000007  # 결과를 나눌 모듈러 값

# 입력
n = int(input("n을 입력하세요: "))

# 예외 처리: n이 1 또는 2인 경우의 결과를 바로 출력
if n == 1:
    print(2)
    exit()
elif n == 2:
    print(7)
    exit()

# DP 배열 초기화
dp = [0] * (n + 1)
dp[1], dp[2] = 2, 7

# 점화식을 이용하여 DP 배열 채우기
for i in range(3, n + 1):
    dp[i] = (2 * dp[i - 1] + dp[i - 2]) % MOD

# 결과 출력
print(dp[n])