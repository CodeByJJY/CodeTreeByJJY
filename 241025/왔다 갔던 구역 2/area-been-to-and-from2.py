street = [0 for _ in range(2000)]

n = int(input())
start = 1000
cnt = 0

for _ in range(n):
    instr = input().split()
    scalar = int(instr[0])
    direction = instr[1]

    if direction == 'L':
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