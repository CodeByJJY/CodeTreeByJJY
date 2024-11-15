# 수열 1
n = int(input())
arr1 = list(map(int, input().split()))
set1 = set(arr1)

# 수열 2
m = int(input())
arr2 = list(map(int, input().split()))
set2 = set(arr2)

exist = True

for elem2 in arr2:
    if elem2 not in set1:
        exist = False
    else:
        exist = True

    if exist:   print(1, end=" ")
    else:       print(0, end=" ")