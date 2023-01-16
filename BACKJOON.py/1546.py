n = int(input())
score = list(map(int, input().split()))

m = max(score)
x = []
for i in score:
    x.append(i/m*100)

result = sum(x)/len(x)
print(result)