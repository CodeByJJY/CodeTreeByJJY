from sortedcontainers import SortedSet

# 명령 개수 n
n = int(input())
s = SortedSet()

# 명령 실행 함수
def treeset(text):
    if text == "largest":
        if s:   print(s[-1])
        else:   print(None)
    elif text == "smallest":
        if s:   print(s[0])
        else:   print(None)
    else:
        cmd, val = text.split()
        val = int(val)
        if cmd == "add":
            if val not in s:    s.add(val)
        elif cmd == "remove":
            s.remove(val)
        elif cmd == "find":
            if val in s:    print("true")
            else:           print("false")
        elif cmd == "lower_bound":
            idx = s.bisect_left(val)
            if idx < len(s):    print(s[idx])
            else:               print(None)
        elif cmd == "upper_bound":
            idx = s.bisect_right(val)
            if idx < len(s):    print(s[idx])
            else:               print(None)


# n개 명령 입력
for _ in range(n):
    command = input()
    treeset(command)