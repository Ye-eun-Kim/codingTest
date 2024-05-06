# 이것이 코딩테스트다 149p
# 음료수 얼려 먹기

n, m = map(int, input().split())
v = []

for i in range(n):
    v.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def dfs(v, x, y):
    v[x][y] = 1
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= n or nx < 0 or ny >= m or ny < 0:
            continue
        if v[nx][ny] == 1:
            continue
        dfs(v, nx, ny)   # 중요!!!!! 이 부분에서 x, y 반환하면 안 된다!!!!!!!
    
for i in range(n):
    for j in range(m):
        if v[i][j] == 0:
            dfs(v, i, j)
            cnt += 1

print(cnt)


    


