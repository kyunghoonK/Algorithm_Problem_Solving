import sys

n = int(sys.stdin.readline())

time = [ [0]*2 for _ in range(n)]

for i in range(n):
    s, e = map(int, sys.stdin.readline())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[]))

print(time)