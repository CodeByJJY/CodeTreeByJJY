street = [0 for _ in range(1, 2001)]

n = int(input())
start = 1000
cnt = 0

for _ in range(n):
    instr = input()
    scalar = int(instr[0])

    if instr[2] == 'L':
        for i in range(start - scalar, start):
            street[i] += 1
        start -= scalar
    else:
        for i in range(start, start + scalar):
            street[i] += 1
        start += scalar

for i in street:
    if i >= 2:  cnt += 1

print(cnt)