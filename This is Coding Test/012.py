# 이것이 코딩테스트다 223p
# 바닥 공사

N = int(input())
dp = [0]*(N+1)
dp[1] = 1
dp[2] = 3
for i in range(3, N+1):
    dp[i] = (dp[i-1]-dp[i-2])*dp[1] + dp[i-2]*dp[2]
    # 정답 코드
    # dp[i] = dp[i-2]*2+dp[i-1]... 훨씬 간단했음

print(dp[-1]%796796)