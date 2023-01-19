# 백준 11720번 - 숫자의 합
a = int(input())
b = int(input())

total = 0

for i in str(b):
    total += int(i)

print(total)