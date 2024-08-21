# 이것이 코딩테스트다 228p
# 효율적인 화폐 구성
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
coins = [int(input().strip()) for i in range(N)]
dp = [0]*(M+1)

for coin in coins:
    if coin < M+1:
        dp[coin] = 1

for i in range(coins[0], M+1):
    for j in range(N):
        point = i+coins[j]
        if point < M+1:
            if dp[point] == 0:
                dp[point] = dp[i] + 1
            else:
                dp[point] = min(dp[i] + 1, dp[point])
                # min을 사용할 거니까 처음부터 1001을 사용했어도 좋았겠다~ 그러면 코드가 더 간단했을 듯.
                # 조건문 하나 필요 없으니께


if dp[M] != 0:
    print(dp[M])

else:
    print(-1)
