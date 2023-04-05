import sys
sys.setrecursionlimit(10000)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    
    graph = [ [0]*m for i in range(n) ]
    
    for i in range(k):
        a,b = map(int, input().split())
        graph[b][a] = 1
    
    cnt = 0
    
    def dfs(x, y):
        global cnt
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        return False
    
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                cnt += 1
    
    print(cnt)