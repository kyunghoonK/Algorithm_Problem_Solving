# 함수를 생성하는 경우

def hansu(num):
    hansu_cnt = 0
    for i in range(1,num+1):
        num_list = list

# 함수를 생성하지 않는 경우
num = int(input())

hansu = 0

for i in range(1,num+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        hansu += 1
    elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        hansu += 1
print(hansu)