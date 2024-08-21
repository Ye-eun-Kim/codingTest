def search(value, i, j, graph, n, m):
    temp = []
    len_max = 0
    for y in range(j+1, m):
        if graph[i][y] == value:
            # 길이를 저장
            temp.append(y-j)
    for length in temp:
        x = i+length
        if x >= n:
            continue
        if graph[x][j] == value:
            if graph[x][j+length] == value:
                len_max = length

    return len_max+1



def solve():
    n, m = map(int, input().split())
    # nums = [list() for _ in range(10)]
    graph = [list(map(int, input())) for _ in range(n)]

    max_len = 1

    for i in range(n):
        for j in range(m):
            value = graph[i][j]
            temp_len = search(value, i, j, graph, n, m)
            max_len = max(max_len, temp_len)

    return max_len * max_len


result = solve()
print(result)