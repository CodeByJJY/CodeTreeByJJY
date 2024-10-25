street = [0 for _ in range(2000)]

n = int(input())
start = 999
cnt = 0

for _ in range(n):
    instr = input()
    scalar = int(instr[0])

    if instr[2] == 'L':
        for i in range(start, start - scalar - 1, -1):
            street[i] += 1
        start -= scalar
    else:
        for i in range(start, start + scalar + 1):
            street[i] += 1
        start += scalar

for i in street:
    if i >= 2:  cnt += 1

print(cnt)