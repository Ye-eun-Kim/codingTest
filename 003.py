# 이것이 코딩테스트다 99p
# 1이 될 때까지

n, k = map(int, input().split())
cnt = 0

while n != 1:
    if (n%k == 0):
        n = n//k
        cnt+=1
        if n == 1:
            break
    else:
        n -= 1
        cnt+=1
        if n == 1:
            break

print(cnt)