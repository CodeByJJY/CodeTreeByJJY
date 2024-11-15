from sortedcontainers import SortedSet
    

T = int(input())

for _ in range(T):
    k = int(input())
    s = SortedSet()

    for _ in range(k):
        cmd, val = input().split()
        val = int(val)

        if cmd == 'I':  s.add(val)
        elif cmd == 'D' and s:
            if val == 1:    s.remove(s[-1])
            elif val == -1: s.remove(s[0])
        
    if not s:
        print("EMPTY")
    else:
        print(s[-1], s[0])