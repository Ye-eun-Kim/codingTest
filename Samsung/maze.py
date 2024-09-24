file = open("sample.txt", "r")
input = file.readline
N, M, K = map(int, input().split())  # 미로 크기, 참가자 수, 게임 시간
walls = []
maze = [[0 for _ in range(N+1)] for _ in range(N+1)] # 1, 1을 시작점으로, n, n을 끝점으로
for i in range(1, N+1):
    maze[i] = list(map(int, input().split()))
    for el in maze[i]:
        if el != 0:
            walls.append(el)
# maze = [[i for i in input().split()] for _ in range(N)]
people = []
for _ in range(M):
    people.append([tuple(map(int, input().split())), N])
er, ec = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# print(people, ex, ey)

# 출구까지 거리 계산 함수
def cal(r1, c1, r2=er, c2=ec):
    return abs(r1-r2)+abs(c1-c2)

# 종료 조건: 1. 시간 끝, 2. 모두 탈출


# 벽 회전
# 가장 가까운 참가자 찾기 -> 2개 이상이면 좌상단 r 작은 거 -> c 작은 거
# 벽 시계 방향 90도 회전 -> temp 만들어서 회전 후 복사본 만들고 참고
# 벽 내구도 -1 -> walls, maze 반영

def find_square():
    # 가장 가까운 참가자 찾기
    (r, c), d = people[0]
    for i in range(1, M):
        (cr, cc), cd = people[i]
        if cd < d:
            r, c = cr, cc
        elif cd == d:
            if cr < r or (cr == r and cc < c):
                r, c = cr, cc
    l = max(abs(r-er), abs(c-ec))
    if r < er:
        lr, ur = r, er
    elif r > er:
        lr, ur = er, r
    else:
        temp = 0
        for j in range(l, -1, -1):
            lr = er-j
            temp = j
            if in_range(lr):
                break
        ur = er+(l-j)
    if c < ec:
        lc, uc = c, ec
    elif c > ec:
        lc, uc = ec, c
    else:
        temp = 0
        for j in range(l, 0, -1):
            lc = ec-j
            temp = j
            if in_range(lc):
                break
        uc = ec+(l-j)
    return lr, ur, lc, uc, l

def rotate():
    lr, ur, lc, uc, l = find_square()
    temp = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            maze_val = maze[lr+i][lc+j]
            if maze_val != 0: # 벽일 때
                tr, tc = j, l-i
                if maze_val != 0:
                    maze_val -= 1
                temp[tr][tc] = maze_val
            # TODO: 참가자, exit 돌리기
            # TODO: 여기 하다 말았다. 일단 temp 좌표는 0~l-1까지라서 좀 헷갈림
            if i == er and j == ec: # exit
                er, ec = lr+tr, lc+tc
                rc-i-1
                
                

    return

def in_range(r, c):
    return 1<=r<=N and 1<=c<=N


result = 0 # 이동 거리 합
for _ in range(K):
    cnt = 0
    # 참가자 이동: 상하좌우, maze 0으로만, 거리 줄어야, 사람 있어도 괜찮, 최대 K초(번) 반복
    # 참가자별로 이동하기 = 방향 찾기+이동 가능 여부 파악
    for p in range(M):
        if people[p][0] == -1: # 죽은 참가자일 때 continue
            continue
        r, c = people[p][0]
        cur_d = cal(r, c)
        nr, nc = 0, 0
        for k in range(4):
            tr, tc = r+dr[k], c+dc[k]
            new_d = cal(tr, tc)
            if new_d == cur_d:
                if k%2 == 1:
                    continue
                else:
                    nr, nc = tr, tc
                    continue
            elif new_d < cur_d:
                if in_range(tr, tc) and maze[r][c] == 0:
                    nr, nc = tr, tc
                    cur_d = new_d
                    result += 1
        if nr != 0 and nc != 0: # 이동했을 때만 r, c 갱신, 이동 안 했을 때는 0, 0이라 절대 안 됨
            r, c = nr, nc
            people[p][1] = new_d
        if r == er and c == ec: # 탈출
            people[p][0] = -1
            cnt += 1
    # 벽 범위 찾기
    # 벽 회전
    rotate()

    if cnt == M: # 모든 참가자가 죽으면 게임 끝
        break

print(result)
print(er, ec)





