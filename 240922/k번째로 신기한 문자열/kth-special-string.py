n, k, T = input().split()
n, k = int(n), int(k)
dictionary = []

for _ in range(n):
    word = input()
    if word[:len(T)] == T:
        dictionary.append(word)

dictionary.sort()

print(dictionary[k-1])