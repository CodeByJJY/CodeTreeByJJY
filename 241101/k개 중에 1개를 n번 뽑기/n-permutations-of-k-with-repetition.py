arr = []

def choose(K, N):
    #   종료 조건
    #   길이가 N일 때 출력 후 되돌아가기.
    if N == 0:
        print(*arr)
        return

    #   진입
    for num in range(1, K+1):
        arr.append(num)
        choose(K, N-1)
        arr.pop()




#   1<=K<=8,    1<=N<=8
K, N = map(int, input().split())
choose(K, N)