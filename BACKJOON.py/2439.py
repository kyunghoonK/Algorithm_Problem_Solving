# 백준 2439번 - 별 찍기 - 2
n = int(input())

for i in range(n):
    print(" "*(n-(i+1))+"*"*(i+1))

# 다른 풀이
a=int(input())
for i in range(1,a+1):
    print(" "*(a-i) + "*"*i)
