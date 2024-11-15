def max_treasure(n, treasure_info):
    # dp 테이블 초기화
    dp = [[0] * 3 for _ in range(n)]
    
    # 1층 초기화
    dp[0][0] = treasure_info[0][0]
    dp[0][1] = treasure_info[0][1]
    dp[0][2] = treasure_info[0][2]
    
    # 2층부터 n층까지 dp 테이블 채우기
    for i in range(1, n):
        dp[i][0] = treasure_info[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = treasure_info[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = treasure_info[i][2] + max(dp[i-1][0], dp[i-1][1])
    
    # n층에서의 결과 계산 (1층의 방과 같은 경우를 제외)
    result = 0
    for first_choice in range(3):  # 1층에서의 선택
        for last_choice in range(3):  # n층에서의 선택
            if first_choice != last_choice:  # 1층과 n층의 선택이 다를 때만 고려
                result = max(result, dp[-1][last_choice])

    return result

# 입력 처리
n = int(input().strip())
treasure_info = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(max_treasure(n, treasure_info))
