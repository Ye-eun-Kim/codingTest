import copy

n = int(input())
input_matrix = [list(map(int, input().split())) for _ in range(n)]
result = copy.deepcopy(input_matrix)


def recur(origin, y, result):
    for idx, value in enumerate(result[y]):
        if value == 0:
            continue
        result[origin][idx] = 1
        if origin < idx:
            recur(origin, idx, result)


for x, row in enumerate(input_matrix):
    for y, value in enumerate(row):
        if value == 0:
            continue
        result[x][y] = 1
        recur(x, y, result)


print(result)


