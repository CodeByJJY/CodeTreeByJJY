# 조건 : 연속하여 같은 숫자가 3번 나오면 안된다.

answer = []

# 1 <= K <= 4,  1 <= N <= 8
K, N = map(int, input().split())


def choose(curr_num):
    if curr_num == N + 1:
        print(*answer)
        return

    # 조건문
    # 1. 해당 시점까지 완성된 answer 배열 길이가 3보다 작거나
    # 2. 현재 숫자가 전, 전전 숫자와는 다를 경우
    # 결론 : 배열에 숫자 추가
    for i in range(1, K + 1):
        if curr_num <= 2:
            answer.append(i)
        elif i != answer[curr_num-2]:
            answer.append(i)
        elif answer[curr_num-2] == answer[curr_num-3]:
            continue
        else:
            answer.append(i)

choose(1)