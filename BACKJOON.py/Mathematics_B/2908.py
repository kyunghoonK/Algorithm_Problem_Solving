a,b = input().split()

array1 = []
array2 = []

def big(a,b):
    for i in str(a):
        array1.append(i)
    array1.reverse()
    ans1 = int(array1[0])*100 + int(array1[1])*10 + int(array1[2])
    
    for x in str(b):
        array2.append(x)
    array2.reverse()
    ans2 = int(array2[0])*100 + int(array2[1])*10 + int(array2[2])
    
    print(max(ans1, ans2))

big(a,b)

# 1) if-else 코드
num1, num2 = input().split()
num1 = int(num1[::-1]) # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else:
    print(num2)

# 2) 삼항 연산자 코드
num1, num2 = input().split()
num1 = int()
num2 = int()

print(num1) if num1 > num2 else print(num2)