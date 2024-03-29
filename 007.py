n, m = map(int, input().split())
a, b, d = map(int, input().split())

info = [[0 for i in range(n)] for i in range(n)]
moves = [(0,-1), (1,0), (0,1),(-1,0)]
info[a][b] = 1

for i in range(n):
    info[i] = list(map(int, input().split()))

move = (0,0)
cnt = 1
flag = True

while (flag):
    for j in range(4):
        d -= 1
        if d < 0:
            d += 4
        
        if d == 0:
            move = moves[3]
        elif d == 1:
            move = moves[2]
        elif d == 2:
            move = moves[1]
        else:
            move = moves[0]
        
        if a+move[0] < 0 or a+move[0] > n or b+move[1] < 0 or b+move[1] > m:
            continue

        info_loc = info[a+move[0]][b+move[1]]

        if info_loc == 0:
            a += move[0]
            b += move[1]
            info[a][b] = 1
            cnt += 1
            break

        elif j == 3:
            info_loc = info[a-move[0]][b-move[1]]
            if info_loc == 1:
                flag = 0
            else:
                a -= move[0]
                b -= move[1]


print(cnt)



        
    