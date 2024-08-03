# 이것이 코딩테스트다 237p
# 다익스트라 간단한 알고리즘과 어려운 알고리즘 비교

# 간단한 알고리즘

import sys
input  = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 약 10억을 설정
# 1e9은 오버플로우를 발생시키지 않을 만큼 충분히 큰 수다.
# 실제 무한대는 핸들링 하기 더 어렵기 때문에 사용하지 않는다.

# 노드 개수와 간선의 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())

# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 만들기
# 인접 리스트: 연결된 노드를 직접 나열하는 방식
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 비용이 c라는 뜻
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    # 두 가지 변수 min_value, index 초기화
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
    # start와 연결된 j번째 노드(X)에 대하여. j의 구성: (X, 가중치)
        distance[j[0]] = j[1]
        # start부터 X까지의 거리: 가중치
        # start와 연결된 모든 노드에 대해 수행.
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 굳이 i를 작성할 필요는 없어 보임. 그냥 _로 처리해도 될 듯.
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        # get_smallest_node()에서 not visited 여부 확인하므로 n-1번만 반복해도 모든 노드 체크
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)


# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])