# 팰린드롬 만들기- 실버 3

import sys
from collections import Counter

word = list(map(str, sys.stdin.readline().strip()))
word.sort()
check = Counter(word)
for i in check:
    print(i)
    
cnt = 0 # 홀수의 개수
center = "" # 홀수의 문자

# 홀수의 개수가 1보다 클 경우 팰린드롬으로 바꾸지 못한다
if cnt > 1:
    print("I'm Sorry Hansoo")