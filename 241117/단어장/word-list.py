from sortedcontainers import SortedDict
import sys

sd = SortedDict()

# n 입력
n = int(sys.stdin.readline())

# 각각의 문자열 입력
for _ in range(n):
    color = sys.stdin.readline().strip()
    
    if color not in sd:
        sd[color] = 1
    else:
        sd[color] += 1

for key, value in sd.items():
    print(f"{key} {value}")