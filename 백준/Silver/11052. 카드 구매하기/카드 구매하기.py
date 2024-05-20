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