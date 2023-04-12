def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

import sys
input = sys.stdin.readline

n = int(input())
array1 = list(map(int, input().split()))
array1.sort()

m = int(input())
array2 = list(map(int, input().split()))
answer = []

for i in array2:
    result = binary_search(array1, i, 0, n-1)
    if result == None:
        answer.append("0")
    else:
        answer.append("1")

for j in answer:
    print(j, end=' ')