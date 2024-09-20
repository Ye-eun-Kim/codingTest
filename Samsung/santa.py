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

def isSantaCrash():

def align(r,c,i):
    cur_s = graph[r][c]
    nr, nc = r+dr[i], c+dc[i]
    if not inRange(nr,nc):
        s_state[cur_s] = -1 # 밀린 것 탈락
    else:
        align(nr, nc, i)
        graph[nr][nc]= cur_s
        s_loc[cur_s]= (nr, nc)

def findS():
    dist = int(1e9)
    santa_num = 0
    sr, sc = 0, 0
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] != 0:
                n_dist = cal(i, j)
                if n_dist < dist:
                    dist = n_dist
                    santa_num = graph[i][j]
                    sr, sc = i, j
    return sr, sc, santa_num, dist

def rMove(turn):
    sr, sc, santa_num, dist = findS()
    direction = 0
    for i in range(8):
        nr, nc = rr+dr[i], rc+dc[i]
        if not inRange(nr, nc):
            continue
        d = (nr-sr)**2+(nc-sc)**2
        if d < dist:
            dist = d
            nnr, nnc = nr, nc
            direction = i
    rr, rc = nnr, nnc
    if rr == sr and rc == sc: # 충돌하는 경우
        s_val[santa_num] += c # 점수 더하기
        s_state[santa_num] = turn # 턴 번호를 state로 설정
        # 산타 밀린 좌표가 range 안에 있는지 확인
        nsr, nsc = sr+dr[i], sc+dc[i]
        if not inRange(nsr, nsc): # 없으면 탈락
            s_state[santa_num] = -1
        else: # 있으면 다른 산타랑 충돌하는지(상호작용) 확인
            if graph[nsr][nsc] != 0: # 충돌
                align(nsr, nsc, direction) # 뒤로 한 칸씩
            graph[nsr][nsc] = santa_num
            s_loc[santa_num] = (nsr, nsc)

def sMove(turn):
    for i in range(1, p+1):
        if s_state[i] >= turn - 1 # 아직 기절
            continue
        s_state[i] = 0
        
        sr, sc = s_loc[i]

def main():
    global n, m, p, c, d
    global rr, rc
    n, m, p, c, d = map(int, input().split())
    rr, rc = map(int, input().split())
    # graph initialization
    graph[rr][rc] = -1
    for i in range(1, p + 1):
        sr, sc = map(int, input().split())
        graph[sr][sc] = i
        s_loc[i] = (sr, sc)
    for j in range(m):
        rMove(j)
        sMove(j)
        for k in range(1, p+1):
            if s_state[k] != -1:
                s_val[k] += 1


if __name__ == "__main__":
    main()
