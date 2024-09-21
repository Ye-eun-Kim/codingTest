# 격자 길이, 턴, 산타 인원, 루돌프 힘, 산타 힘
n,m,p,c,d = 0,0,0,0,0
rr, rc = 1, 1
MAX_N = 50
MAX_P = 30
graph = [[0] * (MAX_N+1) for _ in range(MAX_N+1)]
s_state = [0] * (MAX_P+1) # 기본 0, 패배 -1, 기절 당시의 m
s_val = [0] * (MAX_P+1) # 산타 점수 배열
s_loc = [0] * (MAX_P+1) # 산타 위치 배열
dr = [-1, 0, 1, 0, -1, 1, 1, -1] # 상우하좌-대각선 네 개
dc = [0, 1, 0, -1, 1, 1, -1, -1]

def inRange(r, c):
    return 1 <= r <= n and 1 <= c <= n

# calculate distance between santa and ru
def cal(sr, sc):
    return (sr-rr)**2+(sc-rc)**2

# 가장 가까운 산타를 찾는 함수
def findS():
    dist = int(1e9)
    sr, sc = 0, 0
    santa_num = 0
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            if graph[i][j] != 0 and graph[i][j] != -1:
                n_dist = cal(i, j)
                if n_dist < dist:
                    dist = n_dist
                    santa_num = graph[i][j]
                    sr, sc = i, j
    return sr, sc, santa_num, dist

def align(r,c,i):
    cur_s = graph[r][c]
    nr, nc = r+dr[i], c+dc[i]
    if not inRange(nr,nc):
        s_state[cur_s] = -1 # 밀린 것 탈락
        return
    if graph[nr][nc] != 0:
        align(nr, nc, i)
    graph[r][c] = 0
    graph[nr][nc] = cur_s
    s_loc[cur_s] = (nr, nc)

# 루돌프의 움직임
def rMove(turn):
    sr, sc, santa_num, dist = findS()
    direction = 0
    nnr, nnc = 0, 0
    for i in range(8):
        global rr, rc
        nr, nc = rr+dr[i], rc+dc[i]
        if not inRange(nr, nc):
            continue
        d = (nr-sr)**2+(nc-sc)**2
        if d < dist:
            dist = d
            nnr, nnc = nr, nc
            direction = i
    graph[rr][rc] = 0
    rr, rc = nnr, nnc
    graph[rr][rc] = -1
    if rr == sr and rc == sc: # 충돌하는 경우
        s_val[santa_num] += c # 점수 더하기
        s_state[santa_num] = turn # 턴 번호를 state로 설정
        # 산타 밀린 좌표가 range 안에 있는지 확인
        nsr, nsc = sr+c*dr[direction], sc+c*dc[direction]
        if not inRange(nsr, nsc): # 없으면 탈락
            s_state[santa_num] = -1
        else: # 있으면 다른 산타랑 충돌하는지(상호작용) 확인
            if graph[nsr][nsc] != 0: # 충돌
                align(nsr, nsc, direction) # 뒤로 한 칸씩
            graph[nsr][nsc] = santa_num
            s_loc[santa_num] = (nsr, nsc)

# 산타 한 명의 움직임
def sMove(sr, sc, santa_num, turn):
    # 가까워지는 방향의 좌표 찾기
    nsr, nsc = sr, sc
    dist = cal(sr, sc)
    direction = 0
    for i in range(4): # 산타는 상하좌우만
        drr, dcc = sr + dr[i], sc + dc[i]
        if (not inRange(drr, dcc)) or (graph[drr][dcc] in range(1, p+1)):
            continue
        n_dist = cal(drr, dcc)
        if dist > n_dist:
            nsr, nsc = drr, dcc
            direction = i
            dist = n_dist
    if nsr == sr and nsc == sc: # 이동할 곳이 없을 때
        return
    if nsr == rr and nsc == rc: # 충돌
        s_val[santa_num] += d # 산타 점수 + d
        s_state[santa_num] = turn # 턴 번호를 state로 설정
        direction = (direction+2)%4
        nsr, nsc = nsr+d*dr[direction], nsc+d*dc[direction] # 반대 방향으로 튕김
        # 산타가 범위 안에 있는지 확인
        if not inRange(nsr, nsc): # 없으면 탈락
            s_state[santa_num] = -1
            graph[sr][sc] = 0
            return
        else: # 있으면 다른 산타랑 충돌하는지(상호작용) 확인
            if graph[nsr][nsc] != 0 and graph[nsr][nsc] != santa_num: # 충돌
                align(nsr, nsc, direction) # 뒤로 한 칸씩
    graph[sr][sc] = 0
    graph[nsr][nsc] = santa_num
    s_loc[santa_num] = (nsr, nsc)

def printGraph(turn):
    print(turn, "th turn")
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(graph[i][j], end=' | ')
        print()
    print("s_state: ", s_state)
    print("s_value: ", s_val)

def main():
    global n, m, p, c, d
    global rr, rc
    n, m, p, c, d = map(int, input().split())
    rr, rc = map(int, input().split())
    # graph initialization
    graph[rr][rc] = -1
    for _ in range(p):
        i, sr, sc = map(int, input().split())
        graph[sr][sc] = i
        s_loc[i] = (sr, sc)
    # printGraph(0)
    # print()
    for j in range(1, m+1):
        rMove(j)
        for k in range(1, p + 1):  # 산타 기절 여부 확인
            if s_state[k] != 0 and (s_state[k] == -1 or s_state[k] >= j-1): # 아직 기절
                continue
            s_state[k] = 0
            sMove(s_loc[k][0], s_loc[k][1], k, j)
        for k in range(1, p+1):
            if s_state[k] != -1:
                s_val[k] += 1
        if s_state.count(-1) == p:  # 조기 종료 조건
            break
        # printGraph(j)
        # print()
    for m in range(1, p+1):
        print(s_val[m], end=" ")


if __name__ == "__main__":
    main()
