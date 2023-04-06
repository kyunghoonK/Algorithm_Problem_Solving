import sys
n, k = map(int, sys.stdin.readline().split())

array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()
array.reverse()

result = 0
m = 0


for i in array:
    m = k // i
    result += m
    k = k % i
    if k == 0:
        break

print(result)