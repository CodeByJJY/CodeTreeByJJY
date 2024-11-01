# DFS 문제의 체크 포인트
# 방문 체크
# 방문한 정점의 개수

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)

def dfs(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)

cnt = 0
for b in visited[2:]:
    if b:
        cnt += 1

print(cnt)