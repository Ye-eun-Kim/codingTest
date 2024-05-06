r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

def dfs(x, y):
    graph[x][y] = '.'
    for k in range(len(dx)):
        nx, ny = x+dx[k], y+dy[k]
        if nx < 0 or nx >= r:
            continue # 처음에 이걸 break로 해서 틀림!
        if ny < 0 or ny >= c:
            continue
        if graph[nx][ny] == '#':
            dfs(nx, ny)

for i in range(r):
    for j in range(c):
        if graph[i][j] == '#':
            dfs(i, j)
            result+=1

print(result)
