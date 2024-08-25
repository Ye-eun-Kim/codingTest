r,c,k = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(c+1) for _ in range(r+1)] # 지도 정보
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

golems = [] # 골렘 정보를 담음
golems.append((0,0)) # dummy...
for _ in range(k):
    ci, di = map(int, input().split())  # di: exit 위치, 0~3 북동남서
    golems.append((ci, di))

vals = [0] * (k+1) # 골렘의 행 정보 저장하는 리스트


def mark(c, r, i): # 센터의 r, c를 받으면 주변을 다 graph에 체크
    global dx, dy
    try:
        graph[r][c] = i
    except:
        print(c, r, i)
    for dxx, dyy in zip(dx, dy):
        x, y = c+dxx, r+dyy
        if in_range(x, y):
            graph[y][x] = i

def travel(x, y, i, nd):
    # 인접 골렘 파악하기
    # 인접 골렘의 val이 곧 해당 골렘의 val
    val = y+1
    global dx, dy, graph, vals
    ex, ey = x+dx[nd], y+dy[nd]
    for dxx, dyy in zip(dx, dy):
        nx, ny = ex+dxx, ey+dyy
        if in_range(nx, ny):
            j = graph[ny][nx]
            if j != i and j != INF:
                val = max(vals[j], val)
    vals[i] = val
    return vals[i]


def can_go(x, y):
    global dx, dy
    for dxx, dyy in zip(dx, dy):
        nx, ny = x+dxx, y+dyy
        if ny >= 1:
            if in_range(nx, ny):
                if graph[ny][nx] == INF:
                    continue
                else:
                    return False
            return False
        else:
            if ny <= r and nx >= 1 and nx <= c:
                continue
            else:
                return False
    return True



def in_range(x, y):
    if x >= 1 and x <= c and y <= r and y >= 1:
        return True
    return False

# 0: 못 감, 1: 남, 2: 서남, 3: 동남
def go(ri, ci, di):
    dx, dy, dd = [0, -1, 1], [1, 1, 1], [0, -1, 1]
    x, y = ci, ri
    for dxx, dyy, ddd in zip(dx, dy, dd):
        nx, ny, nd = x+dxx, y+dyy, (di+ddd)%3
        if can_go(nx, ny):
            return ny, nx, nd # can_go True라면 그 방향으로 움직여...
    # 아무 방향으로도 이동할 수 없다면 본래 값을 출력
    return ri, ci, di


def down(ci, di):
    ri = -1
    while True:
        nr, nc, nd = go(ri, ci, di)
        if nr == ri and nc == ci and nd == di:
            break # 다 내려간 것!
        ri, ci, di = nr, nc, nd
    return nc, nr, nd # 센터 x, y 좌표, exit 정보

tot = 0
vacant = True
for i in range(1, k+1):
    golem = golems[i]
    ci, di = golem[0], golem[1]
    if vacant: # 비어 있을 때 그냥 내리기
        mark(ci, r-1, i)
        vals[1] = r
        tot += r
        vacant = False
        print(tot, ci, r-1, i)
        continue
    x, y, nd = down(ci, di)
    if y < 2:
        # graph, vals 초기화
        graph = [[INF] * (c + 1) for _ in range(r + 1)]
        vals = [0] * (k + 1)
        vacant = True
        continue
    mark(x, y, i)
    tot += travel(x, y, i, nd)
    print(tot, x, y, i)

print(tot)

# TODO: 골렘을 내리기(정착)
'''
- range 넘어가지 않게 조정
--- 초기화 알고리즘
- 빈칸인지 여부 확인
- exit 체크
- 최대한 내리기: 우선순위) 아래 -> 아래 왼쪽 -> 아래 오른쪽
- 골렘 정보 속 exit 위치 잘 갱신하기! 골렘 번호가 index of list
'''
# TODO: 골렘을 이동시키기
'''
- 인접한 골렘 속 정령 행 정보가 최종 행 정보임(점화식 마냥...)
- 골렘별 정령 행 정보 저장 리스트 만들기
'''
# TODO: 행 합 연산
