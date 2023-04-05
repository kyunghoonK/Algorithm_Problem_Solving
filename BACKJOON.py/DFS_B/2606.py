# DFS(깊이 우선 탐색) 풀이

n = int(input()) # 컴퓨터의 개수
v = int(input()) # 간선의 개수

graph = [ [] for _ in range(n+1) ]

cnt = 0
visited = [0] * (n+1)

for i in range(v):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)