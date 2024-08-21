# 백준 1260번
# DFS, BFS
# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, v = map(int, input().split())
graph = [list() for _ in range(n+1)]
visited_bfs = [0]*(n+1)
visited_dfs = [0]*(n+1)

for i in range(m):
    inputs = list(map(int, input().split()))
    x = inputs[0]
    y = inputs[1]
    graph[x].append(y)
    graph[y].append(x)

for x in graph:
    x.sort()


def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in range(len(graph[v])):
        nv = graph[v][i]
        if visited_dfs[nv] == 1:
            continue
        dfs(nv)


def bfs(v):
    q = deque()
    visited_bfs[v] = 1
    q.append(v)
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in graph[x]:
            if visited_bfs[y] == 1:
                continue
            visited_bfs[y] = 1
            q.append(y)


dfs(v)
print()
bfs(v)



