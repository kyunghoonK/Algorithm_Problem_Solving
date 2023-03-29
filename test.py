n = int(input())
r = int(input())

graph = [ [] for i in range(n+1) ]

cnt = 0
visited = [0] * (n+1)

print("graph : ", graph)
print("visited : ", visited)

for i in range(r):
    a,b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global cnt
    visited[start] = 1