def binary_search(array, target, start, end):
    mid = (start+end) // 2
    if start > end :
        return None
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

for i in b:
    result = binary_search(a, i, 0, n-1)
    if result == None:
        print("0")
    else:
        print("1")