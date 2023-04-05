# 백준 10871번 - X보다 작은 수
n,x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] < x:
        print(a[i], end=" ")