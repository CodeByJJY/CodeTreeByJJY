# n*n 행렬에 적힌 숫자들 중
# 정확히 n개의 칸에 색칠하여 합을 구함.
# 단, 한번 방문한 행, 열에는 두번다시 방문 불가.
# 최댓값 구하기

n = int(input())

# 전처리
# cnt = 0                 # 각 케이스마다 얻은 점수
score_board = []        # 각 케이스마다 얻은 점수 저장
col_visited = [False] * n     # 열 방문 여부

# n * n 크기의 격자에 정수 입력받기
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 행을 따라 내려가면서, 선택 후 점수 계산
def choose(curr_num, cnt):
    # 종료 조건
    if curr_num == n:
        score_board.append(cnt)
        return

    # 진입
    row = grid[curr_num]

    for idx, piece in enumerate(row):
        # 이미 방문한 열이라면, 다음 열로 pass
        if col_visited[idx]:
            continue

        # 방문하지 않은 열이라면
        col_visited[idx] = True
        cnt += piece
        choose(curr_num + 1, cnt)
        cnt -= piece
        col_visited[idx] = False

choose(0, 0)

print(max(score_board))