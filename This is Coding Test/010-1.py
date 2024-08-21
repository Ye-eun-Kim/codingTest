# 이것이 코딩테스트다 217p
# 1로 만들기
# 정답 코드
# 내 코드는 정답인지 모르겠음...


n = int(input())

d = [0]*(n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[n])


