numbers = list(range(1,10001))

remove_list = []

for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        remove_list.append(num)

for z in set(remove_list):
    numbers.remove(z)

for y in numbers:
    print(y)