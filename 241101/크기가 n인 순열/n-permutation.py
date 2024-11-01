# Permutation

n = int(input())
visited = [False] * (n + 1)
arr = []

def permutation(curr_num):
    # 종료 조건
    if curr_num == n + 1:
        print(*arr)
        return
    
    # 1부터 n까지 돌면서, arr에 추가할 값을 선택.
    for i in range(1, n + 1):
        if visited[i]:
            continue
        
        visited[i] = True
        arr.append(i)
        
        permutation(curr_num + 1)

        visited[i] = False
        arr.pop()

permutation(1)