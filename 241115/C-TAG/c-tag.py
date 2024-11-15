from itertools import combinations

# 입력 받기
N, M = map(int, input().split())
group_A = [input().strip() for _ in range(N)]
group_B = [input().strip() for _ in range(N)]

# 구분 가능한 조합 수를 저장할 변수
count = 0

# 모든 세 자리 조합에 대해 그룹을 구분할 수 있는지 확인
for comb in combinations(range(M), 3):
    # 각 조합에 대해 A 그룹과 B 그룹의 패턴을 집합으로 저장
    patterns_A = set()
    patterns_B = set()
    
    for string in group_A:
        # 그룹 A에서 선택된 자리의 문자열 패턴을 저장
        pattern = (string[comb[0]], string[comb[1]], string[comb[2]])
        patterns_A.add(pattern)
        
    for string in group_B:
        # 그룹 B에서 선택된 자리의 문자열 패턴을 저장
        pattern = (string[comb[0]], string[comb[1]], string[comb[2]])
        patterns_B.add(pattern)
    
    # 두 그룹의 패턴이 겹치지 않으면 구분 가능
    if patterns_A.isdisjoint(patterns_B):
        count += 1

# 결과 출력
print(count)
