# 만들 수 없는 금액
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for i in coins:
    if target < i:
        break
    target += i

print(target)