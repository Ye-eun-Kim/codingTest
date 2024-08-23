# 이것이 코딩테스트다 289p
'''
크루스칼 알고리즘: 최소 신장 트리 탐색
1. 간선 데이터를 비용에 따라 정렬
2. 간선의 사이클 발생 여부 확인(사이클 있으면 신장 트리 아님)
3. 모든 간선에 대해 2번 과정 반복
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(paent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)