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

total_count = sum(sd.values())

for key, value in sd.items():
    percentage = (value / total_count) * 100
    print(f"{key} {percentage:.4f}")