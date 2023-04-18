# 문자열 재정렬
data = input()
result = []
num = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        num += int(x)

result.sort()

if num != 0:
    result.append(str(num))

print(''.join(result))