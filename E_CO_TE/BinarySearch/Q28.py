# 고정점 찾기
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        binary_search(array, mid+1, end)
    else:
        binary_search(array, start, mid-1)

n = int(input())
data = list(map(int, input().split()))

index = binary_search(data, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)