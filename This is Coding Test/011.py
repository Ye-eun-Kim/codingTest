# 이것이 코딩테스트다 220p
# 개미 전사

import copy

n = int(input())
ks = list(map(int, input().split()))
gain = copy.deepcopy(ks)

for i in range(n):
    for j in range(i+2, n):
        v = ks[i] + ks[j]
        gain[j] = v if v > gain[j] else gain[j]

print(max(gain))