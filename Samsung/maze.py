from collections import deque

file = open("sample.txt", "r")
input = file.readline
N, M, K = map(int, input().split())  # 미로 크기, 참가자 수, 게임 시간
maze = [[0 for _ in range(N+1)] for _ in range(N+1)] # 1, 1을 시작점으로, n, n을 끝점으로
for i in range(1, N+1):
    maze[i][1:N+1] = list(map(int, input().split()))
people = []
for _ in range(M):
    people.append([tuple(map(int, input().split())), N])
    # people은 2차원 배열, m개의 [(좌표 튜플), exit까지 거리]를 가짐.
er, ec = map(int, input().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def print_maze():
    for i in range(1, N+1):
        for j in range(1, N+1):
            exist = False
            if maze[i][j] != 0:
                print(maze[i][j], end=" ")
                continue
            if er == i and ec == j:
                print("#", end = " ")
                continue
            for person in people:
                if (i, j) in person:
                    exist = True
                    break
            if exist:
                print("*", end=" ")
            else:
                print(0, end=" ")
        print()
    print()

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
# 벽 내구도 -1 -> maze 반영

def find_square():
    # 가장 가까운 참가자 찾기
    people.sort(key=lambda x: (x[1], x[0]))
    r, c = people[0][0]
    diff_r = abs(r-er)
    diff_c = abs(c-ec)
    if diff_r > diff_c:
        l = diff_r
        ur, lr = (er, r) if er > r else (r, er)
        uc, lc = (ec, c) if ec > c else (c, ec)
        cnt = diff_r-diff_c
        while (cnt):
            if 2 <= lc:
                lc -= 1
            else:
                uc += 1
            cnt -= 1
    elif diff_r < diff_c:
        l = diff_c
        uc, lc = (ec, c) if ec > c else (c, ec)
        ur, lr = (er, r) if er > r else (r, er)
        cnt = diff_c - diff_r
        while (cnt):
            if 2 <= lr:
                lr -= 1
            else:
                ur += 1
            cnt -= 1
    else:
        l = diff_r
        ur, uc = max(r, er), max(c, ec)
        lr, lc = min(r, er), min(c, ec)
    return lr, ur, lc, uc, l

def rotate():
    global er, ec
    lr, ur, lc, uc, l = find_square()
    temp = [[0 for _ in range(l+1)] for _ in range(l+1)]
    for i in range(l+1):
        for j in range(l+1):
            r, c = lr + i, lc + j
            maze_val = maze[r][c]
            tr, tc = j, l - i  # temp의 r, c
            if maze_val != 0: # 벽일 때
                maze_val -= 1
                temp[tr][tc] = maze_val
                continue # 출구, 벽, 사람은 동시에 같은 곳에 있지 않음. 출구와 사람은 같은 곳에 있을 수 있지만 현재는 아님
    # 출구와 참가자 위치 갱신을 위 코드와 함께하니 오류 발생. 앞에서 좌표 갱신해놓고 뒤에서 바뀐 좌표에 대해 검증하면 위치 바뀌어버림
    # temp 완성한 다음에 돌려야 할 듯
    er, ec = lr+(ec-lc), uc-(er-lr)
    for k in range(len(people)): # 벽도, exit도 아닌 0일 때, 사람이 위치했는지 파악하고 위치를 갱신
        pr, pc = people[k][0]
        if lr <= pr <= ur and lc <= pc <= uc: # 참가자가 박스에 포함될 경우
            nr = lr+(pc-lc)
            nc = uc-(pr-lr)
            people[k][0] = nr, nc
    # temp를 maze에 적용
    for tr in range(l+1):
        for tc in range(l+1):
            mr, mc = lr+tr, lc+tc
            maze[mr][mc] = temp[tr][tc]


# 참가자 거리 정보 입력
for m in range(M):
    pr, pc = people[m][0]
    people[m][1] = cal(pr, pc)

q = []
cnt = 0
result = 0 # 이동 거리 합
for i in range(K):
    print(i, "th")
    print_maze()
    # 참가자별로 이동하기 = 방향 찾기+이동 가능 여부 파악
    for p in range(len(people)):
        if people[p][0] == -1:
            continue
        (r, c), cur_d = people[p]
        nr, nc = 0, 0
        new_d = N
        # 참가자 이동: 상하좌우, maze 0으로만, 거리 줄어야, 사람 있어도 괜찮, 최대 K초(번) 반복
        for k in range(4):
            tr, tc = r+dr[k], c+dc[k]
            if not in_range(tr, tc) or maze[tr][tc] != 0:
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
            else: # new_d < cur_d
                nr, nc = tr, tc
                cur_d = new_d
        if nr != 0 and nc != 0: # 이동했을 때만 r, c 갱신, 이동 안 했을 때는 0, 0이라 절대 안 됨
            people[p][0] = (nr, nc)
            people[p][1] = new_d
            result += 1
        if (nr == er and nc == ec) or new_d == 0: # 탈출
            people[p][0] = -1
            cnt += 1
            q.append(p)

    q.sort()
    while q:
        idx = q.pop()
        people.pop(idx)

    if len(people) == 0:  # 모든 참가자 탈락하면 종료
        print("no people")
        print(people)
        break

    print(result)
    print(people)
    print_maze()

    # 벽 범위 찾기
    # 벽 회전
    rotate()
    # people의 distance 갱신
    for m in range(len(people)):
        (pr, pc) = people[m][0]
        people[m][1] = cal(pr, pc)
    print_maze()
    print("="*100)


print(result)
print(er, ec)