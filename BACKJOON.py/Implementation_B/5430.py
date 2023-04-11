T = int(input())

def R(a):
    a.reverse()
    return a

def D(b):
    b.reverse()
    b.pop()
    b.reverse()
    return b

array = []

for i in range(T):
    p = str(input())
    n = int(input())
    x = list(map(int, input().split()))
    if len(x) == 0:
        x = 'error'
        array.append(x)
        break
    
    for j in p:
        if j == R:
            R(x)
        elif j == D:
            D(x)
    
    array.append(x)

for k in array:
    print(k)