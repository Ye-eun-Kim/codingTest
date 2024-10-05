n = int(input())
m = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

center = n//2

r, c = (center, center)

num = 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = 0
x, y = 0, 0

# 이전 숫자 +1을 입력
# 어디에?
stop = False
for i in range(n):
    if stop:
        break
    for _ in range(2):
        if stop:
            break
        for _ in range(i+1):
            graph[r][c] = num
            if m == num:
                x, y = r, c
            num += 1
            if num == n**2+1:
                stop = True
                break
            r = r+dr[d%4]
            c = c+dc[d%4]
        d+=1


for k in range(n):
    for j in range(n):
        print(graph[k][j], end=" ")
    print()
print(x+1, y+1)