count = {}
cards = [3, 7, 8, -1]

for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

count.get(2000)

print(count)