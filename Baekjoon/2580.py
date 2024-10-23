from collections import deque

graph = [list(map(int, input().split())) for _ in range(9)]

def check_row(r, c):
    nums = [1,2,3,4,5,6,7,8,9]
    for j in range(9):
        if j == c:
            continue
        nums.remove(graph[r][j])
    graph[r][c] = nums.pop(0)

def check_col(r, c):
    nums = [1,2,3,4,5,6,7,8,9]
    for k in range(9):
        if k == r:
            continue
        nums.remove(graph[k][c])
    graph[r][c] = nums.pop(0)

def check_box(r, c):
    sr, sc = r//3*3, c//3*3
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            if i == r and j == c:
                continue
            nums.remove(graph[i][j])
    graph[r][c] = nums.pop(0)

zeros = deque()
rows = [0 for _ in range(9)]
cols = [0 for _ in range(9)]
boxes = [0 for _ in range(9)]

for r in range(9):
    for c in range(9):
        if graph[r][c] == 0:
            zeros.append((r, c))
            rows[r] += 1
            cols[c] += 1
            boxes[r//3+c//3*3] += 1
while zeros:
    r, c = zeros.popleft()
    box_num = r//3+c//3*3
    if (rows[r]) == 1:
        check_row(r, c)
    elif (cols[c]) == 1:
        check_col(r, c)
    elif (boxes[box_num]) == 1:
        check_box(r, c)
    else:
        zeros.append((r, c))
        continue
    rows[r] -= 1
    cols[c] -= 1
    boxes[box_num] -= 1


for row in graph:
    print(*row, sep=' ')
