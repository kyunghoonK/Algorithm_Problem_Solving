a,b,c = map(int, input().split())

if c - b <= 0:
    n = -1
    print(n)
else:
    n = a//(c-b)+1
    print(n)
