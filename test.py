import sys
input = sys.stdin.readline

# 이진 탐색
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

t = int(input())

for _ in range(t):
    n = int(input())
    array1 = list(map(int,input().split()))
    array1.sort()
    m = int(input())
    array2 = list(map(int, input().split()))
    for i in array2:
        if binary_search(array1, i, 0, n-1) == None:
            print("0")
        else:
            print("1")
            