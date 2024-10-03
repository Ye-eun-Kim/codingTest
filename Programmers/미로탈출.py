from collections import deque

INF = int(1e9)


def solution(maps):
    g = []
    s, e, l = (0, 0), (0, 0), (0, 0)
    r = -1
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    for line in maps:
        r += 1
        if 'S' in line:
            idx = line.find('S')
            line = line.replace('S', 'O')
            s = (r, idx)
        if 'L' in line:
            idx = line.find('L')
            line = line.replace('L', 'O')
            l = (r, idx)
        if 'E' in line:
            idx = line.find('E')
            line = line.replace('E', 'O')
            e = (r, idx)
        g.append(list(line))

    n = len(g)
    m = len(g[0])

    r, c = s

    visited = []
    q = deque()
    q.append((r, c, 0))
    visited.append((r, c))

    lever = False
    answer = 0

    while q:
        r, c, value = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr >= n or nr < 0 or nc >= m or nc < 0 or g[nr][nc] != 'O':
                continue
            if (nr, nc) not in visited:
                q.append((nr, nc, value + 1))
                visited.append((nr, nc))
                if (nr, nc) == l:
                    lever = True
                    answer = value + 1
                    break
        if lever:
            break

    if not lever:
        return -1

    r, c = l

    visited = []
    q = deque()
    q.append((r, c, 0))
    visited.append((r, c))

    ex = False
    exit_route = 0

    while q:
        r, c, value = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr >= n or nr < 0 or nc >= m or nc < 0 or g[nr][nc] != 'O':
                continue
            if (nr, nc) not in visited:
                q.append((nr, nc, value + 1))
                visited.append((nr, nc))
                if (nr, nc) == e:
                    ex = True
                    exit_route = value + 1
                    break
        if ex:
            break

    if not ex:
        return -1

    return answer + exit_route