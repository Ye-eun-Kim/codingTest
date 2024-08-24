import sys
from collections import deque
input = sys.stdin.readline


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, i, j):
    pi = find_parent(parent, i)
    pj = find_parent(parent, j)
    if pi < pj:
        parent[pj] = parent[pi]
    else:
        parent[pi] = parent[pj]

n, m = map(int, input().split())
parent = list(range(n+1))
edges = deque()
extras = deque()
result = [0] * (n+1)


for i in range(1, n + 1):
    line = input()
    for j in range(i + 1, n + 1):
        char = line[j - 1]
        if char == 'Y':
            edges.append((i, j))

if len(edges) < m:
    print(-1)
    exit()

cnt = 0
for edge in edges:
    i, j = edge
    if find_parent(parent, i) != find_parent(parent, j):
        union_parent(parent, i, j)
        result[i] += 1
        result[j] += 1
        cnt += 1
    else:  # cycle 생성하면 잉여 간선
        extras.append((i, j))

if cnt != n-1:
    print(-1)
    exit()

for _ in range(m-cnt):
    i, j = extras.popleft()
    result[i] += 1
    result[j] += 1

result.pop(0)
print(*result)


