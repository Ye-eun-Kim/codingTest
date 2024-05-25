import sys

s = input()
q = int(input())
questions = [sys.stdin.readline().split() for _ in range(q)]

dp = {}
chars = list(set(s))
len_s = len(s)

for j in range(len(chars)):
    dp[chars[j]] = [0]*len_s

dp[s[0]][0] = 1

for i in range(1, len_s):
    for char in chars:
        dp[char][i] = dp[char][i-1]
    dp[s[i]][i] += 1

for question in questions:
    target, left, right = question[0], int(question[1]), int(question[2])
    if target not in dp:
        print(0)
        continue
    if left == 0:
        if dp[target][left] == 1:
            print(dp[target][right] - dp[target][left] + 1)
            continue
        print(dp[target][right] - dp[target][left])
        continue
    else:
        print(dp[target][right]-dp[target][left-1])


# for question in questions:
#     target, left, right = question[0], int(question[1]), int(question[2])
#     value = s[left:right+1].count(target)
#     print(value)7-+