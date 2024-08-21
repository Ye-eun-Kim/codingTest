n, m = map(int, input().split())
graph = [[]*n for _ in range(n)] # 인접 리스트
num_v = 0
roads = [] # 도로 집합

def is_connected():
    global graph

    return False

for i in range(n):
    string = input()
    for j in range(i+1, n):
        if string[j] == 'Y':
            graph[i].append(j)
            roads.append((i, j))
            continue

print(roads)

if not is_connected():
    print(-1)
    exit()

selected = []
for road in roads:
    if road[0] in selected





