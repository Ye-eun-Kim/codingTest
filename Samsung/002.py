t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    m = [[0 for i in range(n)] for j in range(n)]
    v = [[0 for i in range(5)] for j in range(14)]


    def move(m, x, y, core):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            cnt = 0
            overlap = [0, 0]
            while 1:
                x += dx[i]
                y += dy[i]
                if m[x][y] == 1:
                    overlap = [0,0]
                    cnt = 0
                    break
                if m[x][y] != 0:
                    overlap[0] += 1
                    overlap[1] = m[x][y]
                cnt += 1
                if x == 0 or x == n-1 or y == 0 or y == n-1:
                    break
            overlap = tuple(overlap)
            v[core][i+2] = (cnt, overlap)

        len_line = min(v[core][1:5])
        index_line = v[core].index(len_line)

        if v[core][index_line][1][0] == 0:
            while (1):
                x += dx[index_line]
                y += dy[index_line]
                m[x][y] = core
                if x == 0 or x == n - 1 or y == 0 or y == n - 1:
                    break
            v[core][0] = (x, y)
            v[core][1] = (len_line, index_line)
        else:
            other_core = v[core][index_line][1][1]
            core_second_index = 0
            other_second_index = 0
            for i in range(4):

            other_priority = v[core][1][0] + v[other_core][1][0]
            core_priority =



        return m


    for i in range(n):
        m[i] = list(map(int, input().split()))


    core = 2

    for x in range(1, n-1):
        for y in range(1, n-1):
            # exclude the edge
            if m[x][y] == 0:
                continue
            if m[x][y] == 1:
                v[core][0] = (x, y)
                m = move(m, x, y, core)







    result = 0

    print(f"#{test_case} {result}")
