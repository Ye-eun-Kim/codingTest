import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]


# 시작 r, c는 0~N-8, 0~M-8
# B로 시작하는 case, W로 시작하는 case
b_case = [[0 for _ in range(M-7)] for _ in range(N-7)]
w_case = [[0 for _ in range(M-7)] for _ in range(N-7)]

b_sample = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
w_sample = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

for r in range(N-7):
    for c in range(M-7):
        temp_g = graph[r:r+8]
        sub_graph = []
        for col in range(8):
            sub_graph.append(temp_g[col][c:c+8])
        b_cnt, w_cnt = 0, 0
        for i in range(8):
            for j in range(8):
                if b_sample[i][j] != sub_graph[i][j]: # b_case 점검
                    b_cnt += 1
                if w_sample[i][j] != sub_graph[i][j]: # w_case 점검
                    w_cnt += 1
        b_case[r][c] = b_cnt
        w_case[r][c] = w_cnt


result = N*M


for row in b_case:
    result = min(result, min(row))
for roww in w_case:
    result = min(result, min(roww))

print(result)