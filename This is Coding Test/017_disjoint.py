# 이것이 코딩테스트다 273p
# 서로소 집합 알고리즘
# Union Find

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]  # 경로 압축법: x와 parent[x] 값은 같지만 서로 다른 객체
    '''부모 테이블에 바로 루트 노드가 들어가기 때문에 자동으로 갱신된다.
    예를 들어 처음에 3의 루트 노드가 자신이었다가 2로 바뀐다고 하자.
    이때 2가 새로운 루트 노드 1을 가지게 된다면 3의 루트 노드도 1로 바뀐다.'''
    # return x  --> 개선 이전 코드

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union의 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

'''
사이클 판별 코드 시작
'''
cycle = False  # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b)
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent, a, b)
'''
사이클 판별 코드 끝
'''

'''
부모 테이블을 출력하여 현황을 확인하는 목적의 코드

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end="")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end = "")
for i in range(1, v+1):
    print(parent[i], end=" ")

'''

'''
input 예시
6 4
1 4
2 3
2 4
5 6

output 예시
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 2 1 5 5
'''