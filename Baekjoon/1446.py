# 시작점이 정렬되어 있다는 가정 하에선 맞는 코드

n, d = map(int, input().split())

graph = [i for i in range(d+1)]

for i in range(n):
    [start, end, length] = map(int, input().split())
    if end > d:
        continue
    graph[end] = min(graph[end], graph[start]+length)
    for j in range(end+1, d+1):
        if end == 160 and j < 181:
            print(graph[j], graph[j-1]+1)
        graph[j] = min(graph[j], graph[j-1]+1)
        if end == 160 and j < 181:
            print(f"결국: {graph[j]}")


    print(f"140: {graph[140]}, 160: {graph[160]}, 180: {graph[180]}, 900: {graph[900]}")

print(graph[d])