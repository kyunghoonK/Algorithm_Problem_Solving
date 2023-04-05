# 세 수

n = int(input())
waiting = list(map(int, input().split()))

sum = 0
result = 0

waiting.sort()

for i in waiting:
    sum += i
    result += sum

print(result)