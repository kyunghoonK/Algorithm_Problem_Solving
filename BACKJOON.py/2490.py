a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

result1 = 0
result2 = 0
result3 = 0

for i in a:
    result1 += i
    
if result1 == 0:
    print("D")
elif result1 == 1:
    print("C")
elif result1 == 2:
    print("B")
elif result1 == 3:
    print("A")
else:
    print("E")

for i in b:
    result2 += i
    
if result2 == 0:
    print("D")
elif result2 == 1:
    print("C")
elif result2 == 2:
    print("B")
elif result2 == 3:
    print("A")
else:
    print("E")

for i in c:
    result1 += i
    
if result3 == 0:
    print("D")
elif result3 == 1:
    print("C")
elif result3 == 2:
    print("B")
elif result3 == 3:
    print("A")
else:
    print("E")
