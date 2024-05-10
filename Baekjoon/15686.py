n, m = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(n)]
# dist = [[0]*(n+1) for _ in range(n)]

h = list()
c = list()
graph = list()

for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(len(line)):
        char = line[j]
        if char == 1:
            h.append((i, j))
        elif char == 2:
            c.append((i, j))

dist = [[0]*(c+1) for _ in range(h)]




#
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             dist[idx][0] = (i,j)
#         elif graph[i][j] == 2:
#             if dist[idx][0] == 0:
#                 dist[idx][1]
#
#
# # if c <= m:
# #     #그냥..



