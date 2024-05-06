# 이것이 코딩테스트다 96p
# 숫자 카드 게임

n, m = map(int, input().split())
li = [[0 for i in range(n)] for j in range(m)]
# 굳이 2차원 배열 사용할 필요 없음 한 줄씩만 받아서 min value 구하면 됨

for i in range(0, n):
    li[i] = list(map(int, input().split()))
    if i == 0:
        target = min(li[i])
    temp = min(li[i])
    if temp > target:
        target = temp

print(target)

