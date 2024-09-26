from collections import deque

file = open("sample.txt", "r")
input = file.readline
N, M, K = map(int, input().split())  # 미로 크기, 참가자 수, 게임 시간
walls = []
maze = [[0 for _ in range(N+1)] for _ in range(N+1)] # 1, 1을 시작점으로, n, n을 끝점으로
for i in range(1, N+1):
    maze[i][1:N+1] = list(map(int, input().split()))
    for el in maze[i]:
        if el != 0:
            walls.append(el)
            # TODO: walls 필요할까?
# maze = [[i for i in input().split()] for _ in range(N)]
people = []
for _ in range(M):
    people.append([tuple(map(int, input().split())), N])
    # people은 2차원 배열, m개의 [(좌표 튜플), exit까지 거리]를 가짐.
er, ec = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def print_maze():
    for i in range(1, N+1):
        print(maze[i][1:N+1])

def in_range(r, c):
    return 1<=r<=N and 1<=c<=N

# 출구까지 거리 계산 함수
def cal(r1, c1):
    global er, ec
    return abs(r1-er)+abs(c1-ec)

# 종료 조건: 1. 시간 끝, 2. 모두 탈출

# 벽 회전
# 가장 가까운 참가자 찾기 -> 2개 이상이면 좌상단 r 작은 거 -> c 작은 거
# 벽 시계 방향 90도 회전 -> temp 만들어서 회전 후 복사본 만들고 참고
# 벽 내구도 -1 -> walls, maze 반영

def find_square():
    # 가장 가까운 참가자 찾기
    people.sort(key=lambda x: (x[1], x[0]))
    r, c = people[0][0]

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
            if 1<=lr<=N:
                break
        ur = er+(l-j)
    if c < ec:
        lc, uc = c, ec
    elif c > ec:
        lc, uc = ec, c
    else:
        for i in range(l, -1, -1):
            lc = ec-i
            if 1<=lc<=N:
                break
        uc = lc+l
    return lr, ur, lc, uc, l

def rotate():
    global er, ec
    lr, ur, lc, uc, l = find_square()
    print("lr, ur, lc, uc, l:", lr, ur, lc, uc, l)
    temp = [[0 for _ in range(l+1)] for _ in range(l+1)]
    for i in range(l+1):
        for j in range(l+1):
            r, c = lr+i, lc+j
            maze_val = maze[r][c]
            tr, tc = j, l - i  # temp의 r, c
            if maze_val != 0: # 벽일 때
                if maze_val != 0:
                    maze_val -= 1
                temp[tr][tc] = maze_val
                continue # 출구, 벽, 사람은 동시에 같은 곳에 있지 않음. 출구와 사람은 같은 곳에 있을 수 있지만 현재는 아님
            if r == er and c == ec: # exit 좌표 변경
                er, ec = lr+tr, lc+tc
                continue
            for k in range(len(people)): # 벽도, exit도 아닌 0일 때, 사람이 위치했는지 파악하고 위치를 갱신
                if (r, c) == people[k][0]:
                    people[k][0] = lr+tr, lc+tc
    # temp를 maze에 적용
    for tr in range(l+1):
        for tc in range(l+1):
            mr, mc = lr+tr, lc+tc
            maze[mr][mc] = temp[tr][tc]


# 참가자 거리 정보 입력
for m in range(M):
    pr, pc = people[m][0]
    people[m][1] = cal(pr, pc)

q = deque()

cnt = 0
result = 0 # 이동 거리 합
for i in range(K):
    print((i+1),'th round')
    # 참가자별로 이동하기 = 방향 찾기+이동 가능 여부 파악
    for p in range(len(people)):
        if people[p][0] == -1:
            continue
        r, c = people[p][0]
        cur_d = cal(r, c)
        nr, nc = 0, 0
        # 참가자 이동: 상하좌우, maze 0으로만, 거리 줄어야, 사람 있어도 괜찮, 최대 K초(번) 반복
        for k in range(4):
            tr, tc = r+dr[k], c+dc[k]
            if not in_range(tr, tc):
                continue
            new_d = cal(tr, tc)
            if new_d > cur_d:
                continue
            elif new_d == cur_d:
                if k%2 == 1:
                    continue
                else:
                    nr, nc = tr, tc
                    continue
            elif new_d < cur_d:
                if in_range(tr, tc) and maze[tr][tc] == 0:
                    nr, nc = tr, tc
                    cur_d = new_d
        if nr != 0 and nc != 0: # 이동했을 때만 r, c 갱신, 이동 안 했을 때는 0, 0이라 절대 안 됨
            people[p][0] = (nr, nc)
            people[p][1] = new_d
            result += 1
            if i == 2:
                print(f"person moved!", "({r}, {c}), ({nr}, {nc})")
        if (nr == er and nc == ec) or new_d == 0: # 탈출
            people[p][0] = -1
            cnt += 1
            q.append(p)
        if cnt == M: # 모든 참가자 탈락하면 종료
            break
    if i == 2:
        print(breakpoint)

    # 탈락자 제거
    while q:
        idx = q.popleft()
        people.pop(idx)

    # 벽 범위 찾기
    # 벽 회전
    rotate()
    # people의 distance 갱신
    for m in range(len(people)):
        (pr, pc) = people[m][0]
        people[m][1] = cal(pr, pc)

    print_maze()
    print("People: ", people)
    print("Exit: ", er, ec)
    print()
    print()


print(result)
print(er, ec)





