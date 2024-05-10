import numpy

n = int(input())
input_matrix = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*n for _ in range(n)]

for x, row in enumerate(input_matrix):
    for y, value in enumerate(row):
        print(x, y, value)