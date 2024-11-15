import heapq
import sys

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def empty(self):
        return len(self.items) == 0  # 수정: 비어 있으면 True 반환
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty():
            return "PriorityQueue is empty"  # 안전한 예외 처리
        return -heapq.heappop(self.items)
    
    def top(self):
        if self.empty():
            return "PriorityQueue is empty"  # 안전한 예외 처리
        return -self.items[0]

pq = PriorityQueue()

N = int(sys.stdin.readline().strip())

for _ in range(N):
    cmd = sys.stdin.readline().strip()

    if cmd.startswith("push"):
        val = int(cmd.split()[1])
        pq.push(val)
    
    elif cmd.startswith("pop"):
        print(pq.pop())
    
    elif cmd.startswith("size"):
        print(pq.size())
    
    elif cmd.startswith("empty"):
        print(1 if pq.empty() else 0)  # 비어 있으면 1, 아니면 0 출력
    
    elif cmd.startswith("top"):
        print(pq.top())
