def count_expressions(N, M, numbers):
    # DP 테이블 초기화: -20에서 20까지의 값의 경우만 저장 가능
    dp = [[0] * 41 for _ in range(N)]
    dp[0][numbers[0] + 20] = 1  # 첫 번째 숫자를 더한 결과를 초기화

    # DP 테이블 업데이트
    for i in range(1, N):
        for j in range(-20, 21):
            if dp[i - 1][j + 20] > 0:
                # 현재 숫자를 더하거나 빼는 경우
                if -20 <= j + numbers[i] <= 20:
                    dp[i][j + numbers[i] + 20] += dp[i - 1][j + 20]
                if -20 <= j - numbers[i] <= 20:
                    dp[i][j - numbers[i] + 20] += dp[i - 1][j + 20]

    # 결과 출력
    return dp[N - 1][M + 20]

# 입력 예제
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 결과 출력
print(count_expressions(N, M, numbers))