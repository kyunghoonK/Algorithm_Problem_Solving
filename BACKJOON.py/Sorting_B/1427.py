import sys
input = sys.stdin.readline

n = int(input())

a = str(n)
array = []

for i in a:
    array.append(i)

array.sort()
array.reverse()

for i in array:
    print(i, end='')