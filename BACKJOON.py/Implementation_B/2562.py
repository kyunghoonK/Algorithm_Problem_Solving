# 백준 2562번 - 최댓값
numbers = []
for i in range(9):
    a = int(input())
    numbers.append(a)

print(max(numbers))
print(numbers.index(max(numbers))+1)