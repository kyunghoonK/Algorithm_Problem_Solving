# 국영수

n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    array.append( (input_data[0], input_data[1], input_data[2], input_data[3]) )

array = sorted(array, key = lambda student: student[1])

for student in array:
    print(array[0])