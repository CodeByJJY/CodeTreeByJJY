def count_triplets_with_sum(n, k, numbers):
    count = 0
    for i in range(n):
        seen = {}
        target = k - numbers[i]
        for j in range(i + 1, n):
            complement = target - numbers[j]
            if complement in seen:
                count += seen[complement]
            if numbers[j] in seen:
                seen[numbers[j]] += 1
            else:
                seen[numbers[j]] = 1
    return count

# 입력 처리
# 첫 번째 줄에서 n과 k를 입력받습니다.
n, k = map(int, input().strip().split())

# 두 번째 줄에서 n개의 정수를 입력받습니다.
numbers = list(map(int, input().strip().split()))

# 결과 계산 및 출력
result = count_triplets_with_sum(n, k, numbers)
print(result)
