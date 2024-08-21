def dfs(graph, start, end, visited):
    visited.add(start)

    # 시작 정점에서 도착 정점으로 가는 경로가 있는 경우
    if graph[start][end] == 1:
        return True

    # 인접한 정점들을 순회하며 경로 탐색
    for neighbor in range(len(graph)):
        if graph[start][neighbor] == 1 and neighbor not in visited:
            if dfs(graph, neighbor, end, visited):
                return True

    return False


def solve(graph, n):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            visited = set()
            if dfs(graph, i, j, visited):
                result[i][j] = 1

    return result


# 입력 받기
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 문제 해결
answer = solve(graph, n)

# 출력
for row in answer:
    print(*row)