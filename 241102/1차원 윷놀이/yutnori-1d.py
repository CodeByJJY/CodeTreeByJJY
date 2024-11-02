# m칸의 윷놀이 판에서
# k개의 말이 주어졌을 때
# n회의 기회 속에서 점수를 최대로 내는 법.
# -> n번의 기회 속에서 k개의 말 중 1개를 중복해서 점수를 부여할 때, 
#    숫자 m 이상인 말은 몇개인가?

n, m, k = map(int, input().split())
score_board = [0] * (k + 1)  # 각자의 말의 점수를 표기
score_list = []         # 각 경우의 수에서 획득한 점수를 모음.

# n개의 숫자가 공백을 두고 주어짐
chances = list(map(int, input().split()))

# 매 기회마다 어떤 말을 선택할 것인지 정하는 함수
def choose(curr_num):
    # 종료 조건
    if curr_num == n:
        cnt = 0
        for piece in score_board[1:]:
            if piece >= m:  cnt += 1
        score_list.append(cnt)
        return
    
    # 진입
    forward = chances[curr_num]

    for i in range(1, k + 1):
        score_board[i] += forward
        choose(curr_num + 1)
        score_board[i] -= forward

choose(0)

print(max(score_list))