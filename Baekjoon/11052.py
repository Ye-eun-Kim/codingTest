n = int(input())
prices = list(map(int, input().split()))
dp = [price for price in prices]

for i in range(1, n):
    for j in range(i // 2):
        if j % 2 == 1 and j == n // 2 - 1:
            dp[i] = max(2 * prices[j], dp[-1])
            print("same", 2 * prices[j], dp[-1])
        else:
            print(prices[j] + prices[n - j - 2], dp[-1])
            dp[i] = max(prices[j] + prices[n - j - 2], dp[-1])
            print("changed", dp[-1])

print(dp[-1])