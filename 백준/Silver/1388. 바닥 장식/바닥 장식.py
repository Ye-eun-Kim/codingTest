n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

cnt = 0


def x_dfs(y, x):
    graph[y][x] = 0
    if x == m-1:
        return
    if graph[y][x+1] == '-':
        x_dfs(y, x+1)

def y_dfs(y, x):
    graph[y][x] = 0
    if y == n-1:
        return
    if graph[y+1][x] == '|':
        y_dfs(y+1, x)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            continue
        elif graph[i][j] == '-':
            if j == m-1:
                cnt += 1
                continue
            x_dfs(i, j)
            cnt += 1
        elif graph[i][j] == '|':
            if i == n-1:
                cnt += 1
                continue
            y_dfs(i, j)
            cnt += 1

print(cnt)
