# 단어 정렬
import sys
n = int(sys.stdin.readline())

array = []

for i in range(n):
    array.append(sys.stdin.readline().strip())

set_array = set(array)
array = list(set_array)

array.sort()
array.sort(key = len)

for i in array:
    print(i)