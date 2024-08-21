# 시간이 더 오래 걸리는데..? 다른 사람들 정답 코드랑 큰 차이가 없는데 대체 왜..?
# 오히려 나는 dp만 사용해서 시간 복잡도를 줄일 수 있을 거라고 생각했었는데..
# 공간복잡도만 줄어들고 시간 복잡도는 그대로인 것인가?

# n = int(input())
# dp = list(map(int, input().split()))
#
# for i in range(1, n):
#     for j in range(i):
#         dp[i] = max(dp[j] + dp[i - j - 1], dp[i])
#
# print(dp[-1])

n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    if i == 1:
        dp[1] = max(2 * dp[0], dp[1])
    if i % 2 == 1:
        for j in range(i // 2 + 1):
            if j == (i // 2):
                dp[i] = max(2 * dp[j], dp[i])
            else:
                dp[i] = max(dp[j] + dp[i - j - 1], dp[i])
    else:
        for j in range(i // 2):
            if j == (i // 2):
                dp[i] = max(2 * dp[j], dp[i])
            else:
                dp[i] = max(dp[j] + dp[i - j - 1], dp[i])

print(dp[-1])