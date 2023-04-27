# 고정점 찾기
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        binary_search(array, target, mid+1, end)
    else:
        binary_search(array, target, start, mid-1)

n = int(input())
data = list(map(int, input().split()))

for i in data:
    if binary_search(data, i, 0, len(data))!=None and binary_search(data, i, 0, len(data)) == data[binary_search(data, i, 0, len(data))]:
        print(binary_search(data, i, 0, len(data)))
    else:
        print("-1")
        