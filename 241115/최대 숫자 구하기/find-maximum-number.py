from sortedcontainers import SortedSet
import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
num_list = [i for i in range(1, m + 1)]
set1 = SortedSet(num_list)

num = list(map(int, sys.stdin.readline().split()))

for i in num:
    set1.remove(i)
    print(set1[-1])