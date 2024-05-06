# 이것이 코딩테스트다 220p
# 개미 전사
# 정답 코드
# 내 코드는 정답인지 모르겠음...


n = int(input())
ks = list(map(int, input().split()))

d = [0]*100

d[0] = ks[0]
d[1] = max(ks[0], ks[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+ks[i])

print(d[n-1])