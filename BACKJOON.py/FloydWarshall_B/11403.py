n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 플로이드 워셜 알고리즘
for k in range(n): # k는 거쳐가는 노드
    for i in range(n): # i는 시작 노드
        for j in range(n): # j는 도착 노드
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

# 출력
for row in graph:
    for col in row:
        print(col, end = ' ')
    print()