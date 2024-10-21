# LG CNS 코딩테스트 3번
# 에러 케이스 처리를 잘못 했다...ㅠㅠ

import heapq as q

INF = int(1e9)
N, M, T, S, E = map(int, input().split()) # 정점의 수, 간선의 수, 프리패스 정점의 수, 출발 정점, 도착 정점
free = list(map(int, input().split())) # 프리패스를 파는 정점 리스트(입력 받을 것)

g = [[] for _ in range(N+1)] # 단방향 간선 저장
gg = [[] for _ in range(N+1)] # 양방향 간선 저장 - 프리패스 구매 시점부터 적용하기 위해서
distance = [INF for _ in range(N+1)] # S부터 프리패스 모든 정점까지의 거리 저장
distance[S] = 0 # 시작-시작 거리는 0

for _ in range(M):
    s, e = map(int, input().split())
    g[s].append(e)
    gg[s].append(e)
    gg[e].append(s)


def dijkstra(h):
    while h:
        dist, node = q.heappop(h)
        for i in g[node]: # node와 연결된 다른 노드들에 대해 거리 갱신
            if distance[i] > dist + 1: # 처음 방문하는 노드이더라도 distance[i]가 INF일 것이기에 무조건 해당됨
                distance[i] = dist + 1
                q.heappush(h, (distance[i], i))
    return

# S부터 모든 정점까지 거리 구하기 - 프리패스 최소 거리 그룹 정할 때 사용함
h = []
q.heappush(h, (0, S))
dijkstra(h) # S로부터의 거리 담은 distance 배열 완성

mins = [] # 프리패스 구매할 수 있는 정점들 중에서 S로부터 최소 거리인 정점들을 수집할 리스트
dist = INF # S로부터 최소 거리 저장 변수

for node in free:
    if distance[node] < dist:
        dist = distance[node]
        mins = [node] # 이전에 저장되어 있던 노드는 밀어버려야 한다! dist가 갱신됐기 때문
    elif distance[node] == dist:
        mins.append(node) # dist 갱신 안 됐으니 기존 노드에 추가

# 프리패스 정점 구하기 위해 프리패스-출구 거리 계산
mindist = {} # 프리패스 정점별 H까지의 거리 담는 딕셔너리

for node in mins:
    flag = False # Exit 포인트에 도달했는지 체크. 반복문이 여러 개라 break만으로 탈출이 불가능하여 flag 설정.
    visited = [] # 방문 노드 체크
    mindist[node] = 0 # 시작할 때는 거리 0
    h = []
    visited.append(node)
    q.heappush(h, (0, node))

    while h:
        if flag: # 이미 출구를 만났다면 종료. 더 해봤자 거리가 늘어날 뿐임
            break
        dist, n = q.heappop(h)
        for nearnode in gg[n]:
            if nearnode in visited: # 양방향이기 때문에 무한 루프 방지하기 위해 필요
                continue
            mindist[node] = dist + 1
            if nearnode == E:
                flag = True
                break
            visited.append(nearnode)
            q.heappush(h, (mindist[node], nearnode))
    # 제출 후 추가한 코드ㅠㅠㅠㅠㅠㅠㅠㅠ 이것만 제때 했어도!!
    if not flag:
        mindist[node] = INF

# 프리패스 구매할 정점을 최종적으로 결정
fd = INF # 프리패스-출구 거리
fn = 0 # 프리패스 정점 번호
for freenode, freedist in mindist.items():
    if freedist < fd:
        fn = freenode

answer = freenode, freedist+distance[freenode]

print(-1) if freedist+distance[freenode] == INF else print(answer[0], answer[1])
