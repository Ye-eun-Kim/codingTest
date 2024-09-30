def solution(park, routes):
    dirs = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
    H, W = len(park), len(park[0])
    g = [[e for e in el] for el in park]
    for i in range(H):
        for j in range(W):
            if g[i][j] == 'S':
                r, c = i, j
    for route in routes:
        dir, dis = route.split(" ")
        dis = int(dis)
        dr, dc = dirs[dir][0], dirs[dir][1]
        flag = False
        tr, tc = r, c
        for _ in range(dis):
            nr, nc = tr+dr, tc+dc
            if not(0<=nr<=H-1 and 0<=nc<=W-1):
                flag = True
                break
            if g[nr][nc] == 'X':
                flag = True
                break
            tr, tc = nr, nc
        if not flag:
            r, c = tr, tc
        
    return [r, c]