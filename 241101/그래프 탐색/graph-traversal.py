# DFS 문제의 체크 포인트
# 방문 체크
# 방문한 정점의 개수

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]          # 하나의 vertex에 연결된 다른 vertex 파악.
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)                 # vertex 목록은 1차원 배열로 표현 가능.

def dfs(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)

cnt = 0
for b in visited[2:]:                       # 다시 원점으로 돌아온 것은 제외.
    if b:
        cnt += 1

print(cnt)