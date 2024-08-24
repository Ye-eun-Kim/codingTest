from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# BFS
def bfs(q):
    # x, y는 각각 row, col
    while q:
        x, y = q.popleft()
        global graph
        # graph[x][y] = 2 # visited 개념
        for dxx, dyy in zip(dx, dy):
            nx, ny = x+dxx, y+dyy
            if nx >=0 and nx < m and ny >= 0 and ny < n:
                v = graph[nx][ny]
                if v == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))

first_row = graph[0]
last_row = graph[m-1]
for j in range(n):
    v = first_row[j]
    if v == 1: # 전류 X
        continue
    # 전류 O
    q = deque()
    graph[0][j] = 2  # visited 개념
    q.append((0, j))
    bfs(q)
    for val in last_row:
        if val == 2:
            print('YES')
            exit()

print('NO')

