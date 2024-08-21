import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 기존에 sorted를 이용했던 것을 sort로 변경
a.sort()
b.sort(reverse=True)

tot = 0
for i in range(n):
    tot = tot + a[i] * b[i]

print(tot)

