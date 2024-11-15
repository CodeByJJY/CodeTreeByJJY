from itertools import combinations

def count_triplets_with_sum(n, k, numbers):
    count = 0
    # 세 개의 서로 다른 위치를 선택하여 조합을 생성
    for comb in combinations(range(n), 3):
        if numbers[comb[0]] + numbers[comb[1]] + numbers[comb[2]] == k:
            count += 1
    return count

# 입력 처리
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# 결과 계산 및 출력
result = count_triplets_with_sum(n, k, numbers)
print(result)
