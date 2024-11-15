def max_similarity(N, M, sequence):
    # DP 테이블 정의
    dp = [[[0] * (M + 1) for _ in range(5)] for _ in range(N)]
    
    # 첫 번째 위치 초기화
    for num in range(1, 5):
        dp[0][num][0] = 1 if num == sequence[0] else 0
    
    # DP 테이블 채우기
    for i in range(1, N):
        for prev_num in range(1, 5):
            for changes in range(M + 1):
                for curr_num in range(1, 5):
                    new_changes = changes + (1 if curr_num != prev_num else 0)
                    if new_changes <= M:
                        similarity = dp[i-1][prev_num][changes] + (1 if curr_num == sequence[i] else 0)
                        dp[i][curr_num][new_changes] = max(dp[i][curr_num][new_changes], similarity)
    
    # 최대 유사도 계산
    max_similarity = 0
    for num in range(1, 5):
        for changes in range(M + 1):
            max_similarity = max(max_similarity, dp[N-1][num][changes])
    
    return max_similarity

# 입력 처리
N, M = map(int, input().split())
sequence = list(map(int, input().split()))

# 결과 출력
print(max_similarity(N, M, sequence))
