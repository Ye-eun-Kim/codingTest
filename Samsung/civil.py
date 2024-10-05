import copy
from collections import deque

input = open("civil.txt", "r").readline
K, M = map(int, input().split())
graph = [[i for i in list(map(int, input().split()))] for _ in range(5)]
walls = [j for j in list(map(int, input().split()))]

centers = [(1,1),(1,2),(1,3), (2,1),(2,2),(2,3), (3,1),(3,2),(3,3)]
a = [(1, -1), (0, -1), (-1, -1), (1, 0), (-1, 0), (1, 1), (0, 1), (-1, 1)] # 돌린 뒤 순서
b = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # 돌리기 전 순서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def is_inrange(r, c):
    return 0<=r<=4 and 0<=c<=4

def spin(r, c, curr_graph):
    g = copy.deepcopy(curr_graph)
    store = []
    for i in range(8):
        tr, tc = r+a[i][0], c+a[i][1]
        store.append(curr_graph[tr][tc])
    for j in range(8):
        nr, nc = r+b[j][0], c+b[j][1]
        g[nr][nc] = store.pop(0)
    return g

def cal(curr_graph, flag):
    val = 0
    for num in range(1, 8):
        visited = []
        for r in range(5):
            for c in range(5):
                if (r, c) in visited:
                    continue
                q = deque()
                node = curr_graph[r][c]
                v = []
                if node != num:
                    continue
                temp_val = 1
                visited.append((r, c))
                q.append((r, c))
                if flag == 1:
                    v.append((r, c))
                    curr_graph[r][c] = 0
                while q:
                    r, c = q.popleft()
                    for i in range(4):
                        nr, nc = r+dr[i], c+dc[i]
                        if not is_inrange(nr, nc):
                            continue
                        if curr_graph[nr][nc] == num and (nr, nc) not in visited:
                            temp_val += 1
                            visited.append((nr, nc))
                            q.append((nr, nc))
                            if flag == 1:
                                v.append((nr, nc))
                                curr_graph[nr][nc] = 0
                if temp_val >= 3:
                    val += temp_val
                else:
                    while v:
                        vr, vc = v.pop(0)
                        curr_graph[vr][vc] = num
    return curr_graph, val

def explore():
    temp_val, temp_angle, temp_center = 0, 1, (0, 0)  # temp_val이 0으로 남는다면 종료
    for center in centers:
        curr_center = center
        r, c = curr_center
        t_val, t_angle = 0, 1
        curr_graph = copy.deepcopy(graph)
        for curr_angle in range(1, 4):  # angle은 1-2-3이 각각 90, 180, 270도
            curr_graph = spin(r, c, curr_graph) # 90도씩 돌리기 때문
            curr_graph, curr_val = cal(curr_graph, 0)
            if curr_val != 0 and curr_val > t_val:
                t_val, t_angle = curr_val, curr_angle
        if t_val > temp_val:
            temp_val, temp_angle, temp_center = t_val, t_angle, curr_center
        elif t_val == temp_val and t_angle < temp_angle:
            temp_val, temp_angle, temp_center = t_val, t_angle, curr_center
        elif t_val == temp_val and t_angle == temp_angle:
            tr, tc = temp_center
            if c < tc:
                temp_val, temp_angle, temp_center = t_val, t_angle, curr_center
            elif c == tc and r < tr:
                temp_val, temp_angle, temp_center = t_val, t_angle, curr_center
    return temp_center, temp_angle, temp_val

def fill(g):
    for c in range(5):
        if len(walls) == 0:
            break
        for r in range(4, -1, -1):
            if len(walls) == 0:
                break
            if g[r][c] == 0:
                g[r][c] = walls.pop(0)
    return g

def print_graph():
    for i in range(5):
        print(graph[i])
    print()

for k in range(K):
    result = 0
    center, angle, val = explore()
    if val == 0:
        break
    for _ in range(angle):
        graph = spin(center[0], center[1], graph)
    while val:
        graph, val = cal(graph, 1)
        graph = fill(graph)
        result += val
    if result == 0:
        continue
    print(result, end = ' ')