# 이것이 코딩테스트다 110p
# 상하좌우

n = int(input())
plan = input().split()
point = [1,1]
for p in plan:
    if p == 'R':
        point[1] = point[1]+1
        if (point[1]) > n:
            point[1] -= 1
    elif p == 'L':
        point[1] = point[1]-1
        if (point[1]) < 1:
            point[1] += 1
    elif p == 'D':
        point[0] = point[0]+1
        if (point[0]) > n:
            point[0] -= 1
    elif p == 'U':
        point[0] = point[0]-1
        if (point[0]) < 1:
            point[0] += 1

print(point[0], point[1])
