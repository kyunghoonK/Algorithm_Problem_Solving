# 백준 25304번 - 영수증

x = int(input())

n = int(input())
sum = 0

for i in range(n):
    a,b = map(int, input().split())
    t = a*b
    sum += t

if sum == x:
    print("Yes")
else:
    print("No")