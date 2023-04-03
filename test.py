n = int(input())

list = []

for i in range(n):
    list.append(int(input()))

list.sort()
list.reverse()
print(list)