# 이것이 코딩테스트다 217p
# 1로 만들기

n = int(input())

def fir(n):
    n /= 5
    return n

def sec(n):
    n /= 3
    return n

def thi(n):
    n /= 2
    return n

def fou(n):
    n -= 1
    return n

cnt = 0

while(n > 1):
    if n % 5 == 0:
        n = fir(n)
    elif n % 3 == 0:
        n = sec(n)
    elif (n-1) % 5 == 0:
        n = fou(n)
    elif (n-1) % 3 == 0:
        n = fou(n)
    elif n % 2 == 0:
        n = thi(n)
    else:
        n = fou(n)
    cnt += 1

print(cnt)