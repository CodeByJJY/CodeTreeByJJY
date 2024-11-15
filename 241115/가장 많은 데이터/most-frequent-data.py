from collections import Counter

# 입력 처리
n = int(input())  # 문자열 개수
strings = [input().strip() for _ in range(n)]  # 문자열 리스트 입력

# 문자열의 등장 횟수를 세기
count = Counter(strings)

# 가장 많이 등장한 횟수 찾기
max_count = max(count.values())

# 결과 출력
print(max_count)
