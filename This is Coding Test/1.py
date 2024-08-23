def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, rank, a, b):
    rootA = find_parent(parent, a)
    rootB = find_parent(parent, b)
    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
            if rank[rootA] == rank[rootB]:
                rank[rootB] += 1

n, m = map(int, input().split())
roads = []

for i in range(1, n + 1):
    line = input().strip()
    for j in range(i + 1, n + 1):
        if line[j - 1] == 'Y':
            roads.append((i, j))

# 모든 도로의 가능한 조합을 확인하는 대신, 도로들을 점진적으로 추가하면서 확인
parent = list(range(n + 1))
rank = [0] * (n + 1)
result = [0] * (n + 1)
connected_count = 0

for road in roads:
    i, j = road
    if find_parent(parent, i) != find_parent(parent, j):
        union_parent(parent, rank, i, j)
        connected_count += 1

    result[i] += 1
    result[j] += 1

    # 모든 도시가 연결되었는지 확인
    if connected_count == n - 1:  # 도시가 n개일 때, 최소 n-1개의 연결이 필요
        break

# 모든 도시가 연결되었는지 확인
root = find_parent(parent, 1)
if all(find_parent(parent, i) == root for i in range(1, n + 1)):
    print(*result[1:])
else:
    print(-1)