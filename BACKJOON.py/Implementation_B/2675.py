# 백준 2675번 - 문자열 반복
a = int(input())

for _ in range(a):
    t,s = input().split()
    for x in str(s):
        print(x*int(t), end="")
    print()
