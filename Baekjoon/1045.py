import itertools

def union_parent(parent, i, j):
    pi, pj = parent[i], parent[j]
    if pi < pj:
        parent[j] = parent[i]
        return
    else:
        parent[i] = parent[j]
        return

def prep_roads(parent, n):
    for i in range(1, n + 1):
        line = input()
        for j in range(i + 1, n + 1):
            char = line[j - 1]
            if char == 'N':
                continue
            union_parent(parent, i, j)
            roads.append((i, j))

n, m = map(int, input().split())
parent = list(range(n+1))
roads = []
prep_roads(parent, n)

for el in parent:
    if (el != 1 and el != 0) or (len(roads) < m):
        print(-1)
        exit()

# print(roads)

for comb in itertools.combinations(roads, m):
    result = [0] * (n + 1)
    num = 0
    for road in comb:
        if num == m:
            break
        i, j = road
        result[i] += 1
        result[j] += 1
        num += 1
    result.pop(0)
    if 0 in result:
        continue
    break

print(*result)