# 이것이 코딩테스트다 99p
# 1이 될 때까지
# 예시 답안 개선

n, k = map(int, input().split())
cnt = 0

target = (n//k)*k
cnt += (n-target)
while n >= k:
    n //= k
    cnt+=1

print(cnt)