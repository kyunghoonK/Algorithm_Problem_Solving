# 숫자 카드 2
def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return count.get(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

import sys
input = sys.stdin.readline

array = []

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))
    
count = {}
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for j in b:
    print(binary_search(a, j, 0, n-1), end = ' ')