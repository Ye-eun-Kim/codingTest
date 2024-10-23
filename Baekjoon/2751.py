import sys
input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

print(*nums, sep='\n')