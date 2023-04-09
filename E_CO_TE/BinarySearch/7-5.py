# 이진 탐색 소스코드 구현(반복문) - 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n(가게의 부품 개수)
n = int(input())
array = list(map(int,input().split()))
array.sort()

# m(손님이 요청한 부품 개수)
m = int(input())
x = list(map(int, input().split()))

# 손님이 요청한 부품번호를 하나씩 확인
for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else :
        print('no', end=' ')