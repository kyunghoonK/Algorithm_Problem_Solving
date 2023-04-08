import sys
n = int(sys.stdin.readline())

road = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

result = 0
money = cost[0]

for i in range(n-1):
    if cost[i] < money:
        money = cost[i]
    result += money * road[i]

print(result)