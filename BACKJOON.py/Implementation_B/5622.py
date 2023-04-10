alphabet_list = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

word = input()
time = 0
for unit in alphabet_list:
    for i in unit:
        for x in word:
            if i == x:
                time = time + alphabet_list.index(unit) +3

print(time)

# alphabet_list[0] = 3
# alphabet_list[1] = 4
# alphabet_list[2] = 5
# alphabet_list[3] = 6
# alphabet_list[4] = 7
# alphabet_list[5] = 8
# alphabet_list[6] = 9
# alphabet_list[7] = 10