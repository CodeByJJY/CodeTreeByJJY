N = int(input())
memo = [-1] * (N + 1)
memo[1], memo[2] = 1, 1

def fibbo(n):
    # 이미 n번째 값을 구한 적이 있다면, memo에 적힌 값 반환
    if memo[n] != -1:
        return memo[n]
    
    # n <= 2 : 종료 조건
    if n <= 2:
        memo[n] = 1
    # 종료조건 아닌 경우 : 점화식을 이용하여 답을 구한 뒤, memo에 저장.
    else:
        memo[n] = fibbo(n - 1) + fibbo(n - 2)
    
    # memo 값을 반환.
    return memo[n]


print(fibbo(N))