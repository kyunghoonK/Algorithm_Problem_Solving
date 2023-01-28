n,k = map(int, input().split())
total = 0

while n != 1:
    if n % k == 0:
        n = n//k
        total += 1
        if n == 1:
            print(total)
            break
        
    else:
        n -= 1
        total += 1
        if n == 1:
            print(total)
            break