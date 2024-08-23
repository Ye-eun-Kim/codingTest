# 택배

import sys
input = sys.stdin.readline
INF = int(1e9)

# n <= 200, m <= 10000
n, m = map(int, input().split())

# 인접 행렬로. 플로이드-워셜 알고리즘 사용
graph = [[(0, INF) for i in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = '-'

# 무방향
for j in range(m):
    a, b, t = map(int, input().split())
    graph[a][b] = (b, t)
    graph[b][a] = (a, t)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # if a == 4 and b == 2 and k == 5:
            #     print()
            if a == b or a == k or b == k:
                continue
            ab = graph[a][b][1]
            cost = graph[a][k][1] + graph[k][b][1]
            if cost < ab:
                if graph[a][k][0] != 0:
                    graph[a][b] = (graph[a][k][0], cost)
                else:
                    graph[a][b] = (k, cost)

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j][0], end=" ")
    print("")