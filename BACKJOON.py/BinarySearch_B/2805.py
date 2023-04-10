n, m = map(int, input().split())
trees = list(map(int, input().split()))

array = []

for i in range(int(max(trees))):
    for j in trees:
        if j - i < 0:
            array.append(0)
        else:
            array.append(j-i)
if sum(array) == m:
    print(i)
