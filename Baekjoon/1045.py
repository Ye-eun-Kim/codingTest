# import itertools
import sys
from collections import deque
input = sys.stdin.readline


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, a)
    return parent[a]

def union_parent(parent, i, j):
    pi, pj = parent[i], parent[j]
    if pi < pj:
        parent[j] = parent[i]
        return
    else:
        parent[i] = parent[j]
        return


n, m = map(int, input().split())
parent = list(range(n+1))
roads = deque()
extras = deque()
result = []

for i in range(1, n + 1):
    line = input()
    for j in range(i + 1, n + 1):
        char = line[j - 1]
        if char == 'Y':
            union_parent(parent, i, j)
            roads.append((i, j))

for el in parent:
    if (el != 1 and el != 0) or (len(roads) < m):
        print(-1)
        exit()

cycle = False
for road in roads:
    a, b = road
    if find_parent(parent, a) == find_parent(parent, b):
        continue




'''
메모리 초과가 뜨는 코드...
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
'''

print(*result)