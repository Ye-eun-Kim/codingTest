from collections import deque

n = int(input())
pairs = int(input())
graph = [list() for _ in range(n+1)]
for _ in range(pairs):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


check = list()
result = 0


def bfs(q):
    while(q):
        v = q.popleft()
        if v not in check:
            check.append(v)
        for adj in graph[v]:
            if adj not in check:
                q.append(adj)


q = deque()
q.append(1)
bfs(q)
# exclude 1
print(len(check)-1)