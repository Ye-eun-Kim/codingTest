# 이것이 코딩테스트다 152p
# 미로 탈출

from collections import deque

n, m = map(int, input().split())
plans = []
for i in range(n):
    plans.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(plans, q, dx, dy):
    while(q):
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if plans[nx][ny] == 0:
                continue

            '''
            사실 아래에 내가 작성한 것은 정확하지 않음
            어차피 일찍 노드를 방문하는 것만 적으면 되기에
            if plans[nx][ny] == 1 
            의 경우에만 +1 해주면 됨
            '''
            
            if plans[nx][ny] != 1 and plans[nx][ny] < plans[x][y]+1:
                continue
            plans[nx][ny] = plans[x][y]+1
            q.append((nx, ny))

            if nx == n-1 and ny == m-1:
                return plans[nx][ny]
                
q = deque()
x, y = 0, 0
q.append((x,y))
print(q)


print(bfs(plans, q, dx, dy))