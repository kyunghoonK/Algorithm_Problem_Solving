n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

total = 0
for i in range(n):
    ab = a[i] * max(b)
    b.remove(max(b))
    total += ab

print(total)