N = int(input())
seq = list(map(int, input().split()))
index_seq = [len(seq)]

new_seq = sorted(seq)

for val in seq:
    for idx, num in enumerate(new_seq):
        if num == val:
            if idx in index_seq:
                continue
            else:
                index_seq.append(idx)
                break

for idx in index_seq[1:]:
    print(idx + 1, end=" ")