from collections import deque

r, c, k = 0, 0, 0
MAX_L = 70
graph = [[0] * MAX_L for _ in range(MAX_L+3)] # 실질적으로 map을 3~n+2까지 쓰고 싶어서.
isExit = [[False] * MAX_L for _ in range(MAX_L+3)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0

def inRange(y, x):
    return 3 <= y < r+3 and 0 <= x < c
    # y의 하한값 때문에 헷갈렸음! canGo에서 안 쓰기 때문에 하한값 신경쓸 필요 없음.
    # 순수하게 in range인지 묻는 것. 애초에 inRange와 canGo는 독립적인 게 맞음.

def resetMap():
    for i in range(r+3):
        for j in range(c):
            graph[i][j] = 0
            isExit[i][j] = False

def canGo(y, x):
    flag = y+1 < r+3 and 0 <= x-1 and x+1 < c
    flag = flag and graph[y-1][x-1] == 0
    flag = flag and graph[y-1][x] == 0
    flag = flag and graph[y-1][x+1] == 0
    flag = flag and graph[y][x-1] == 0
    flag = flag and graph[y][x] == 0
    flag = flag and graph[y][x+1] == 0
    flag = flag and graph[y+1][x] == 0
    return flag

def bfs(y, x):
    result = y
    visited = [[False] * c for _ in range(r+3)]
    q = deque()
    q.append((y, x))   # 두 줄을 한 줄로 q = deque([(y, x)])
    visited[y][x] = True
    while q:
        cur_y, cur_x = q.popleft()
        for m in range(4):
            ny, nx = cur_y+dy[m], cur_x+dx[m]
            if inRange(ny, nx) and not visited[ny][nx] and (graph[ny][nx] == graph[cur_y][cur_x] or (isExit[cur_y][cur_x] and graph[ny][nx] != 0)):
                q.append((ny, nx))
                visited[ny][nx] = True
                result = max(result, ny)
    return result

def down(y, x, d, id):
    if canGo(y+1, x):
        down(y+1, x, d, id)
    elif canGo(y+1, x-1):
        down(y+1, x-1, (d+3)%4, id)  # d-1보다는 d+3이 낫다.
    elif canGo(y+1, x+1):
        down(y+1, x+1, (d+1)%4, id)
    else:
        if not inRange(y-1, x-1) or not inRange(y+1, x+1): # 사실 두 번째 거 이해 x
            resetMap()
        else:
            graph[y][x] = id
            for m in range(4):
                graph[y+dy[m]][x+dx[m]] = id
            isExit[y+dy[d]][x+dx[d]] = True
            global answer
            answer += bfs(y, x) - 3 + 1 # 시작 지점이 3이니까!! 시작을 1로 만들어야 해서..

def main():
    global r, c, k
    r, c, k = map(int, input().split())
    for id in range(1, k+1): #골렘 번호 id
        x, d = map(int, input().split())
        down(1, x-1, d, id) # x는 시작 지점이 0이니까 입력-1 함!!
    print(answer)

if __name__ == "__main__":
    main()