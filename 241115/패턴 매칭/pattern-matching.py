def is_match(s, p):
    # 문자열과 패턴의 길이
    len_s, len_p = len(s), len(p)
    
    # DP 테이블 초기화
    dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
    dp[0][0] = True  # 빈 문자열과 빈 패턴은 일치

    # 패턴 초기화 (패턴에 '*'이 있는 경우를 위해)
    for j in range(2, len_p + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    # DP 테이블 채우기
    for i in range(1, len_s + 1):
        for j in range(1, len_p + 1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:  # 현재 문자가 일치하거나 '.'인 경우
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':  # '*'인 경우
                dp[i][j] = dp[i][j-2]  # '*'을 0개로 취급
                if p[j-2] == s[i-1] or p[j-2] == '.':  # '*'을 1개 이상으로 취급
                    dp[i][j] |= dp[i-1][j]
    
    return dp[len_s][len_p]

# 입력 처리
s = input().strip()
p = input().strip()

# 결과 출력
print("true" if is_match(s, p) else "false")
