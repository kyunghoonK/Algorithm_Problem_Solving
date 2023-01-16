# 백준 5597번 - 과제 안 내신 분..?
m = []

for i in range(1,31):
    m.append(i)

for _ in range(28):
    a = int(input())
    m.remove(a)

print(min(m))
print(max(m))