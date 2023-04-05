# 백준 10809번 - 알파벳 찾기
word = input()
alphabet = list(range(97,123))

for x in alphabet :
    print(word.find(chr(x)))