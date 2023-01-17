n = int(input())

for _ in range(n):
    ox_list = input()
    score = 0
    sum_score = 0
    for i in ox_list:
        if i == 'o':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)