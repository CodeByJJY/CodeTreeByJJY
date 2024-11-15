from sortedcontainers import SortedDict
import sys

n = int(sys.stdin.readline().strip())  # 명령어 수
d = SortedDict()  # SortedDict 초기화

# 명령어 처리
for _ in range(n):
    command = sys.stdin.readline().strip()
    if command.startswith("add"):
        _, k, v = command.split()
        k, v = int(k), int(v)
        d[k] = v  # (k, v) 추가 또는 업데이트

    elif command.startswith("remove"):
        _, k = command.split()
        k = int(k)
        del d[k]  # k 제거

    elif command.startswith("find"):
        _, k = command.split()
        k = int(k)
        print(d.get(k, "None"))  # 값이 없으면 None 출력

    elif command.startswith("print_list"):
        if d:
            print(" ".join(map(str, d.values())))  # value 값들 출력
        else:
            print("None")
