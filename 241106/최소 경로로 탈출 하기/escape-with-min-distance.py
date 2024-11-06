from collections import deque

n, m = map(int, input().split())
X_LEN, Y_LEN = n, m

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

q = deque()
step = [
    [0 for _ in range(Y_LEN)]
    for _ in range(X_LEN)
]
visited = [
    [False for _ in range(Y_LEN)]
    for _ in range(X_LEN)
]

def in_range(x, y):
    return 0 <= x < X_LEN and 0 <= y < Y_LEN

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return True

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x, y))

push(0, 0, 0)


dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

# BFS 탐색
while q:
    x, y = q.popleft()

    # 도착지에 도달했을 경우 최단 거리 출력 후 종료
    if x == X_LEN - 1 and y == Y_LEN - 1:
        print(step[x][y])
        exit()

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            push(new_x, new_y, step[x][y] + 1)

# 도착지에 도달하지 못한 경우 -1 출력
print(-1)