n = int(input())
total = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    total += n // coin
    n %= coin
    
print(total)