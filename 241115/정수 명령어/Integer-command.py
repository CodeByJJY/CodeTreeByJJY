from sortedcontainers import SortedSet

s = SortedSet()

def treeset(text):
    cmd, val = text.split()
    val = int(val)

    if cmd == 'I':
        s.add(val)
    
    if cmd == 'D':
        if s:
            if val == 1:    s.remove(s[-1])
            elif val == -1: s.remove(s[0])

T = int(input())

for _ in range(T):
    k = int(input())

    for _ in range(k):
        command = input()
        treeset(command)
    if not s:
        print("EMPTY")
    else:
        print(s[-1], s[0])