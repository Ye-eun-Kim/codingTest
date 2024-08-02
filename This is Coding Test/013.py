# 이것이 코딩테스트다 228p
# 효율적인 화폐 구성
import sys
input = sys.stdin.readline

N, M = map(int, input())
coins = [input().strip() for i in range(N)]
dp = [0]*(M+1)


for i in range(coins[0], M+1):
    for j in range(N):
        if i-coins[j] >= coins[0] and dp[i] != 0:
            dp[i] = min(dp[i-coins[j]]+1,dp[i])
        if i in coins:
            dp[i] += 1


