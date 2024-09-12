N = int(input())

sum_list = []
numbers = list(map(int, input().split()))
numbers.sort()

for i in range(N):
    sum_list.append(numbers[i] + numbers[2*N-i-1])

print(max(sum_list))