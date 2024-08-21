# 이것이 코딩테스트다 259p
# 미래 도시
# 플로이드-워셜 버전

# import sys
# input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dest, meeting = map(int, input().split())

for k in range(n+1):
    for b in range(n+1):
        for a in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

to_middle = graph[1][meeting]
to_end = graph[meeting][dest]


if to_middle == INF or to_end == INF:
    print(-1)
else:
    print(to_middle+to_end)