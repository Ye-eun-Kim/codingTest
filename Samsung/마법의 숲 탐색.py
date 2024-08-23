r,c,k = map(int, input().split())
INF = int(1e9)
map = [[INF]*(c+1) for _ in range(r+1)] # 지도 정보
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

golems = [] # 골렘 정보를 담음
golems.append((0,0)) # dummy...
for _ in range(k):
    ci, di = map(int, input().split())  # di: exit 위치, 0~3 북동남서
    golems.append((ci, di))

vals = [0] * (k+1) # 골렘의 행 정보 저장하는 리스트


def mark(r, c, i): # 센터의 r, c를 받으면 주변을 다 map에 체크
    global dx, dy
    for dxx, dyy in zip(dx, dy):
        x, y = c+dxx, r+dyy
        map[x][y] = i

def travel(i):
    # TODO: 인접 골렘 파악하기
    # 인접 골렘의 r_val이 곧 해당 골렘의 r_val

    vals[i] = r_val
    return r_val


def in_range(x, y):
    if x >= 2 and x <= c-1 and y <= r-1:
        return True
    return False


# 0: 못 감, 1: 남, 2: 서남, 3: 동남
def go(ri, ci, di):
    dx, dy, dd = [0, -1, 1], [1, 1, 1], [0, -1, 1]
    x, y = ci, ri
    for dxx, dyy, ddd in zip(dx, dy, dd):
        nx, ny, nd = x+dxx, y+dyy, (di+ddd)%3
        if not in_range(nx, ny):
            continue
        return nx, ny, nd # in_range True라면 그 방향으로 움직여...
    # 아무 방향으로도 이동할 수 없다면 본래 값을 출력
    return ri, ci, di


def down(ci, di):
    ri = -1
    while True:
        nr, nc, nd = go(ri, ci, di)
        if nr == ri and nc == ci and nd == di:
            break # TODO: 다 내려간 것!
    return nc, nr, nd # 센터 x, y 좌표, exit 정보

tot = 0
vacant = True
for i in range(1, k+1):
    golem = golems[i]
    ci, di = golem[0], golem[1]
    if vacant: # 비어 있을 때 그냥 내리기
        mark(r-1, ci, i)
        vals[1] = r
        tot += r
        vacant = False
        continue
    x, y, nd = down(ci, di)
    if y < 2:
        # map, vals 초기화
        map = [[INF] * (c + 1) for _ in range(r + 1)]
        vals = [0] * (k + 1)
        vacant = True
        continue
    golems[i][1] = nd
    mark(x, y, i)
    tot += travel(i)


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
