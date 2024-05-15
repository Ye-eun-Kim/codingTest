# 정답 코드이지만 다소 비효율적일지도?

n, d = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
roads.sort(key=lambda x:x[0])

graph = [i for i in range(d+1)]

for i in range(n):
    [start, end, length] = roads[i]
    if end > d:
        continue
    graph[end] = min(graph[end], graph[start]+length)
    for j in range(end+1, d+1):
        graph[j] = min(graph[j], graph[j-1]+1)

print(graph[d])