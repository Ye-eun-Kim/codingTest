# import itertools
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
    # pi, pj = parent[i], parent[j]
    '''
    40%에서 오류나는 원인!! 바로 여기!! 아래와 같이 코드를 짰었기 때문에 에러가 났나봄
    
    if pi < pj:
        parent[j] = parent[i]
    else:
        parent[i] = parent[j]
    '''
    if pi < pj:
        parent[pj] = parent[pi]
    else:
        parent[pi] = parent[pj]

n, m = map(int, input().split())
parent = list(range(n+1))
roads = deque()
extras = deque()
result = [0] * (n+1)


'''
정답 코드의 방향성
간선 먼저 저장
mst 생성(union find) + 잉여 간선 저장
mst 없으면 -1, 간선 개수 m보다 작으면 -1
'''

'''
현재 코드의 방향성 --- 자꾸 40쯤에서 멈춤
mst 생성(union find), 잉여 간선(=cycle 만드는 것) 저장
필요한 간선만큼 잉여 간선에서 포함시킴 => extras -> roads
road의 양끝에 대해 개수 세기
'''

for i in range(1, n + 1):
    line = input()
    for j in range(i + 1, n + 1):
        char = line[j - 1]
        if char == 'Y':
            if find_parent(parent, i) != find_parent(parent, j):
                union_parent(parent, i, j)
                roads.append((i, j))
            else: # cycle 생성하면 잉여 간선
                extras.append((i, j))

'''
이대로 하면 50% 에서 에러남
1이 다른 것과 연결되지 않는 경우가 있을지도?

for el in parent:
    if (el != 1 and el != 0) or ((len(roads)+len(extras)) < m):
        print(-1)
        exit()
'''

if (len(roads) != n-1) or ((len(roads)+len(extras)) < m):
    print(-1)
    exit()

done = False
if len(roads) >= m:
    done = True

while not done:
    road = extras.popleft()
    roads.append(road)
    if len(roads) == m:
        done = True

for _ in range(m):
    a, b = roads.popleft()
    result[a] += 1
    result[b] += 1

result.pop(0)
print(*result)



'''
시간 초과가 뜨는 코드 : 조합 사용
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