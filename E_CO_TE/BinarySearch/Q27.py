# 정렬된 배열에서 특정 수의 개수 구하기
n, x = map(int, input().split())
array1 = list(map(int, input().split()))
cnt = 0

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

for i in range(n):
    result = binary_search(array1, x, 0, len(array1)-1)
    if result != None:
        cnt += 1
else:
    print("-1")
        

print(cnt)
        