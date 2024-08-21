n, m = map(int, input().split())
inputs = list(map(int, input().split()))

dp = []

value = 0
cnt = 0

for i in range(0, n):
    value += inputs[i]
    dp.append(inputs[i])
    if value >= m:
        while (value > m):
            value -= dp[0]
            dp.pop(0)
        if value == m:
            cnt += 1

print(cnt)