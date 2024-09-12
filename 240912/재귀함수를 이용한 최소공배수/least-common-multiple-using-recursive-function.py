# 재귀함수를 이용한 최소공배수      # 70xp
# n개의 수가 주어졌을 때 이 수들의 최소공배수를 구하는 프로그램을 작성해보세요. 단, 재귀함수를 이용하여 문제를 해결해주세요.

def lcm(a, b):
    org_a, org_b = a, b
    c = a%b
    while b != 0:
        c = a%b
        a = b
        b = c
    return (org_a*org_b)//a

n = int(input())

num = list(map(int, input().split()))
num.sort()


if n == 1:
    print(*num)
else:
    lcm_1 = lcm(num[0], num[1])
    for i in num[2:]:
        lcm_1 = lcm(lcm_1, i)

    print(lcm_1)