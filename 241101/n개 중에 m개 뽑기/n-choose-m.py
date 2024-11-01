# Combination

N, M = map(int, input().split())

answer = []

def choose(cnt):
    # 종료 조건
    if len(answer) == M:
        print(*answer)
        return
    
    # 진입
    for i in range(cnt, N + 1):
        answer.append(i)
        choose(answer[-1] + 1)
        answer.pop()

choose(1)