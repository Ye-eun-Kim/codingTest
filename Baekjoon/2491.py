n = int(input())
series = list(map(int, input().split()))

dp_long = [1]*n
dp_short = [1]*n

for i in range(n-1):
    if series[i] <= series[i+1]:
        dp_long[i+1] = dp_long[i]+1
    if series[i] >= series[i+1]:
        dp_short[i+1] = dp_short[i]+1

result = max(max(dp_long), max(dp_short))

print(result)


