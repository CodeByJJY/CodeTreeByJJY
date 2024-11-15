from sortedcontainers import SortedSet

s = SortedSet()

n, m = tuple(map(int, input().split()))

for _ in range(n):
    point = tuple(map(int, input().split()))
    s.add(point)

for _ in range(m):
    qst = tuple(map(int, input().split()))
    idx = s.bisect_left(qst)

    if idx == len(s):
        print(-1, -1)
    else:
        print(*s[idx])