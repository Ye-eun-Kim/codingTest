# 이것이 코딩테스트다 248p
# 다익스트라 간단한 알고리즘과 개선된 알고리즘 비교
# 한 점에서 최단 거리

# 개선된 알고리즘
'''
Key point!
- Heap 자료 구조 사용 (Priority Queue 구현)
- distance 리스트는 그대로 사용, P.Q 추가 이용하여 최소 거리 노드 탐색 최적화
--> 최악에도 O(ElogV) 시간복잡도
'''

'''
<Priority Queue>
권장 : PriorityQueue <<< heapq : heapq가 더 빠름
우선 순위 : 첫 번째 원소
Min vs Max : 값 낮은(default) vs 큰 데이터 먼저 삭제
Max Heap 사용 위해선 우선순위 값에 (-) 붙여 저장
list로 priority queue 구현 가능하지만 시간복잡도 불리(O(N^2)) (vs. O(NlogN))
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수와 간선의 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())

# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 만들기
# 인접 리스트: 연결된 노드를 직접 나열하는 방식
graph = [[] for i in range(n+1)]
# 변화 1. 방문한 적이 있는지 체크하는 리스트 필요 없음
# visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a -> b 비용이 c라는 뜻
    graph[a].append((b, c))


# 변화 2. get_smallest_node() 필요 없음

def dijkstra(start):
    # 변화 3. heapq 등장
    q = []
    heapq.heappush(q, (0, start))
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있고 (distance가 dist보다 작다는 것은 INF 아니라는 뜻)
        # distance 값 갱신에 도움이 안 되면 패스
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        # 결론적으로 간선 수 E만큼 반복하게 되므로 O(ElogE)
        # 이때 E<V^2 (모든 노드끼리 연결될 경우 간선 개수인 E는 V^2 이하)
        # 따라서 logE < logV^2 = 2logV = logV
        # 따라서 O(ElogV)
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 것이 더 짧은 경우(갱신 이득)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

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
