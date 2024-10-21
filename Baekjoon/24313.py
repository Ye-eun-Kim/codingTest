a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 != c:
    std = -a0//(a1-c)
    if std > n0 or a1 > c:
        print(0)
    else:
        print(1)
else:
    if a0 <= 0:
        print(1)
    else:
        print(0)
