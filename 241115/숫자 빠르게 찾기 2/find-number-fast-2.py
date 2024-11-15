from sortedcontainers import SortedSet
set1 = SortedSet()

n, m = map(int, input().split())

arr1 = list(map(int, input().split()))

for i in arr1:
    set1.add(i)

for _ in range(m):
    num = int(input())

    idx = set1.bisect_left(num)

    if idx == len(arr1):
        print(-1)
    else:
        print(set1[idx])