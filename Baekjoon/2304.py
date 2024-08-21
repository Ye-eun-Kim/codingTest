import sys
input = sys.stdin.readline

n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]
infos = sorted(infos, key=lambda x: -x[1])
right, left = infos[0][0], infos[0][0]
node = infos.pop(0)
r, l = node[0], node[0]

# 시작 기둥의 면적 (아래 과정에서 계산되지 않음)
area = node[1]

while infos:
    node = infos.pop(0)
    x, h = node[0], node[1]
    if x < l:
        area += (l - x) * h
        l = x
    elif x > r:
        area += (x - r) * h
        r = x
    else:
        continue

print(area)
