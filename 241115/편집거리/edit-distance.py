def edit_distance(A, B):
    N, M = len(A), len(B)
    # DP 테이블 초기화
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # 초기 값 설정
    for i in range(N + 1):
        dp[i][0] = i  # A의 i번째까지 B를 빈 문자열로 변환하는 데 필요한 삭제 연산 횟수
    for j in range(M + 1):
        dp[0][j] = j  # B의 j번째까지 A를 빈 문자열로 변환하는 데 필요한 삽입 연산 횟수

    # DP 테이블 채우기
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:  # 문자가 같을 경우 편집이 필요 없음
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 삽입, 삭제, 교체 중 최소 연산 횟수 선택
                dp[i][j] = min(dp[i][j - 1] + 1,  # 삽입
                               dp[i - 1][j] + 1,  # 삭제
                               dp[i - 1][j - 1] + 1)  # 교체

    return dp[N][M]

# 입력 처리
A = input().strip()
B = input().strip()

# 결과 출력
print(edit_distance(A, B))
