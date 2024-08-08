# 이것이 코딩테스트다 259p
# 미래 도시
# 다이젝스트라 버전

import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

# 정점과 간선 개수 입력받음
n, m = map(int, input().split())
# 간선 정보 리스트 초기화
graph = [[] for _ in range(n+1)]
# 간선 정보를 인접 리스트로 받음
for _ in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 이 부분을 처리하지 않아서 계속 오류 났었음
    # 거리는 전부 1이므로 tuple을 저장할 필요 없음
# x, k 입력
x, k = map(int, input().split())
# 거리 정보 저장하는 리스트

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for dest in graph[now]:
            cost = dist + 1
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(q, (cost, dest))

    return distance[end] if distance[end] != INF else -1


result = 0
first = dijkstra(1, k)
if first != -1:
    result += first
else:
    print(-1)
    exit()
second = dijkstra(k, x)
if second != -1:
    result += second
    print(result)
else:
    print(-1)
    exit()

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""
"""
4 2
1 3
2 4
3 4
"""
