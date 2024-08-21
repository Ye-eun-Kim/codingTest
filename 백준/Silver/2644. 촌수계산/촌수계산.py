n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [0]*(n+1)

for _ in range(m):
    # x가 부모
    x, y = map(int, input().split())
    graph[y] = x
    # 아래에서 위로 탐색하다가 같은 (조)부모를 만났을 때
    # 각자 올라간 거리를 더하면 될 듯

def dfs(v, w, cnt):
    if graph[v] == 0:
        return
    p = graph[v]
    cnt += 1
    if p == w:
        global result
        if result == -1:
            result = cnt
        else:
            result = min(result, cnt)
    else:
        dfs(p, w, cnt)
        dfs(w, p, cnt)

# result 기본값을 -1로 설정, 촌수 찾으면 그 값으로 변경
result = -1

if a == graph[b] or b == graph[a]:
    result = 1

dfs(a, b, 0)
dfs(b, a, 0)

print(result)

