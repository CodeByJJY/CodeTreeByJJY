n, m = map(int, input().split())
sequence = list(map(int, input().split()))
queries = list(map(int, input().split()))

# 각 숫자의 빈도를 저장할 딕셔너리 생성
frequency = {}

# 수열의 각 숫자에 대해 빈도 계산
for num in sequence:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# 각 질의에 대해 빈도를 출력
result = []
for q in queries:
    result.append(frequency.get(q, 0))  # 해당 숫자가 없으면 0으로 출력

print(" ".join(map(str, result)))