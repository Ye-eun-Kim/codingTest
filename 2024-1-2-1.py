r, c, k = map(int, input().split())
graph = [[(0, 0)]*(c+1) for _ in range(r+1)]
info = [] * (k+1)

for i in range(1, k+1):
    c, d = map(int, input().split())  # c>=2, 0<=d<=3
    info.append((c, d))

# 이동: 북동남서-0123
# 이동 우선순위
# 남쪽, 서회전, 동회전 (순서대로, 우선순위)
dx = [0, -1, 1]
dy = [-1, -1, -1]
dd = [0, -1, 1]

# 위치의 모든 기준은 중심
def in_range(x, y):
    if y<=r-1 and y>=2 and x<=c-1 and x>=2:
        return True
    else:
        return False

def first_in_range(x, y):
    if x<=c-1 and x>=2:
        return True
    else:
        return False

# 골렘의 모든 부분(날개)이 graph의 1과 겹치지 않는지 확인
# 겹치면 True, 안 겹쳐서 갈 수 있으면 False
def check(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for dxx, dyy in zip(dx, dy):
        nx, ny = x+dxx, y+dyy
        if graph[nx][ny] == (0, 0):
            continue
        else:
            return True
        return False

def can_go(x, y, d):
    for dxx, dyy, ddd in zip(dx, dy, dd):
        nx, ny, nd = x+dxx, y+dyy, (d+ddd)%4
        if y in range(-1, 1):
            if not first_in_range(nx, ny) or check(nx, ny):
                continue
            else:
                return nx, ny, nd
            global graph
            graph = [[(0, 0)]*(c+1) for _ in range(r+1)]
            return 0, y, d
        else:
            if not in_range(nx, ny) or check(nx, ny):
                continue
            else:
                return nx, ny, nd
    return 0, y, d

def down(x, y, d):
    nx, ny, nd = can_go(x, y, d)
    if nx != 0: # ny는 따지지 않아도 됨
        return down(nx, ny, nd)
    else:
        return x, y, d

def mark(x, y, d):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ex = x+dx[d]  # exit의 x
    ey = y+dy[d]  # exit의 y
    graph[x][y] = (ex, ey)
    cnt = 0
    for dxx, dyy in zip(dx, dy):
        nx, ny = x + dxx, y + dyy
        if cnt == d:
            graph[nx][ny] = (x, y)
            cnt += 1
            continue
        graph[nx][ny] = (ex, ey)
        cnt += 1

def adj_mv(x, y): # x, y는 exit 좌표
    # 위쪽으로 가진 않음
    dx = [1, 0, -1]
    dy = [0, -1, 0]
    for dxx, dyy in zip(dx, dy): # exit 주변 탐색
        nx, ny = x+dxx, y+dyy
        px, py = graph[nx][ny] # TODO: 이 좌표가 exit인지 중심인지 모름
        if graph[px][py] == (nx, ny):  # nx, ny가 exit 좌표일 때
            cx, cy = px, py
            px, py = nx, ny
        else: # 사이드 -> exit -> 중심
            # px, py 가 exit 좌표 = nx, ny가 아무 좌표
            cx, cy = graph[px][py]
        if px != x and py != y and px != 0 and py != 0:   # 다른 골렘이고 빈칸이 아닐 때
            return cx, cy
    return 0, 0



def explore(x, y):
    global r
    if y+1 == r:
        return r
    ex, ey = graph[x][y] # mark에서 exit 좌표를 중앙에 새겨두었기 때문
    nx, ny = adj_mv(ex, ey) # 반환값은 이동한 골렘의 중심 좌표

    if nx == 0 and ny == 0:
        return y+1


tot = 0
for i in range(k):
    c, d = info.pop(0)
    x, y = c, -1
    nx, ny, nd = down(x, y, d)
    mark(nx, ny, nd)
    tot += explore(nx, ny)

