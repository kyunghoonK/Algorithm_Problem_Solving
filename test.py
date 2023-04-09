import sys

n = int(input())
d = list(map(int, input().split()))
d.sort()

m = int(input())
c = list(map(int,input().split()))

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return None
    if array[mid] == target:
        return mid
    elif array[mid] > target :
        binary_search(array, target, start, mid - 1)
    else :
        binary_search(array, target, mid + 1, end)

for i in c:
    result = binary_search(d, i, 0, n-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no")