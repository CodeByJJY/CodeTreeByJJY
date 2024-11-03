# concept : 각 원소를 순회하면서 각 원소에 대한 dfs 탐색을 행한다.

# 격자의 크기
n = int(input())
visited = [[False for _ in range(n)] for _ in range(n)]

# 블럭 입력
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 블럭 범위 내인지 여부 탐색
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 해당 블럭으로 갈 수 있는지 여부 탐색
def can_go(cur_x, cur_y, nxt_x, nxt_y):
    # 블럭 범위 내에 있는가?
    if not in_range(nxt_x, nxt_y):
        return False
    
    # 방문한 적 있거나, 현재 블럭의 숫자와 다른가?
    if visited[nxt_x][nxt_y] or grid[cur_x][cur_y] != grid[nxt_x][nxt_y]:
        return False
    
    return True

# DFS 탐색
def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    block_size = 0

    while stack:
        cur_x, cur_y = stack.pop()
        block_size += 1

        dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
        for dx, dy in zip(dxs, dys):
            nxt_x, nxt_y = cur_x + dx, cur_y + dy

            if can_go(cur_x, cur_y, nxt_x, nxt_y):
                visited[nxt_x][nxt_y] = True
                stack.append((nxt_x, nxt_y))

    return block_size

# 결과 변수
burst_count = 0
max_block_size = 0

# 격자를 순회하며 DFS 실행
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block_size = dfs(i, j)
            if block_size >= 4:
                burst_count += 1
            max_block_size = max(max_block_size, block_size)

# 결과 출력
print(burst_count, max_block_size)