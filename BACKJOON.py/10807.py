# 백준 10807번 - 개수 세기
n = int(input())

a = list(map(int, input().split()))
v = int(input())
num = 0

for i in range(len(a)):
    if a[i] == v:
        num += 1

print(num)