def count_triplets_with_sum(n, k, numbers):
    count = 0
    # 딕셔너리를 사용하여 두 수의 합을 저장
    for i in range(n):
        seen = {}
        target = k - numbers[i]
        for j in range(i + 1, n):
            complement = target - numbers[j]
            # 이전에 complement가 나온 적이 있는지 확인
            if complement in seen:
                count += seen[complement]
            # 현재 숫자를 seen에 추가
            if numbers[j] in seen:
                seen[numbers[j]] += 1
            else:
                seen[numbers[j]] = 1
    return count

# 입력 처리
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# 결과 계산 및 출력
result = count_triplets_with_sum(n, k, numbers)
print(result)
