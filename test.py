# 플로이드 워셜 함수

INF = int(1e9)

n = int(input())
m = int(input())

graph = [ [INF] * (n + 1) for _ in range(n + 1) ]

# 자신에서 자신으로 가는 값 0으로 설정
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] == 0

# 초기값 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(n + 1):
    for b in range(n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()