# Combination

N, M = map(int, input().split())

answer = []

def choose(curr_num, cnt):
    # 종료 조건
    if curr_num == M + 1:
        print(*answer)
        return
    
    # 진입
    for i in range(cnt, N + 1):
        answer.append(i)
        choose(curr_num + 1, answer[-1] + 1)
        answer.pop()

choose(1, 1)