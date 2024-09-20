n = int(input())
dp = [1] * (n+1)
dp[n-1] = 1 #SK
dp[n-2] = -1 #CY

for i in range(n, 0, -1):
    if i >= 1:
        dp[i-1] = -dp[i]
    if i >= 3:
        dp[i-3] = -dp[i]

if dp[0] == -1:
    print("SK")
else:
    print("CY")
