n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

result = []
cnt = 0

def dfs(x, y):
    global cnt
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(cnt)
            cnt = 0

print(len(result))
result.sort()
for i in result:
    print(i)