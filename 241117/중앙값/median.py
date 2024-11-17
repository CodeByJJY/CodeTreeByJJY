import sys
import heapq

# 입력
input = sys.stdin.read
data = input().split()

# 테스트 케이스 수
t = int(data[0])
index = 1

results = []

for _ in range(t):
    # 수열의 크기
    m = int(data[index])
    index += 1

    # 수열의 값들
    sequence = list(map(int, data[index:index + m]))
    index += m

    # 힙 초기화
    max_heap = []  # 중앙값 이하 (최대 힙)
    min_heap = []  # 중앙값 이상 (최소 힙)
    current_result = []

    for i in range(m):
        num = sequence[i]

        # 최대 힙에 삽입
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # 힙 균형 유지
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # 홀수 번째 원소마다 중앙값 출력
        if (i + 1) % 2 == 1:
            current_result.append(-max_heap[0])

    results.append(" ".join(map(str, current_result)))

# 출력
sys.stdout.write("\n".join(results) + "\n")
