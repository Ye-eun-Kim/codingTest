# 이것이 코딩테스트다 262p
# 전보
# 다익스트라 알고리즘

import heapq

INF = int(1e9)
n, m, start = map(int, input().split())
distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, time = map(int, input().split())
    graph[a].append((b, time))

distance[start] = 0
q = []
heapq.heappush(q, (0, start))
while q:
    dist, now = heapq.heappop(q)
    # dist, now = el[0], el[1]
    if distance[now] < dist:
        continue
    for i in graph[now]:
        dest, time = i[0], i[1]
        distance[dest] = min(distance[now]+time, distance[dest])
        heapq.heappush(q, (distance[dest], dest))


num = -1  # 자신의 노드까지 거리가 0이기 때문에
tot = 0
for i in range(1, n+1):
    time = distance[i]
    if time != INF:
        num+=1
        if time > tot:
            tot = time

print(num, tot)

"""
3 2 1
1 2 4
1 3 2
"""