# 백준 2480번 - 주사위 세개
a,b,c = map(int, input().split())
r = 0

if a==b==c :
    r += 10000+1000*a
elif a==b!=c :
    r += 1000+100*a
elif a==c!=b :
    r += 1000+100*a
elif b==c!=a :
    r += 1000+100*b
else:
    r += max(a,b,c)*100

print(r)