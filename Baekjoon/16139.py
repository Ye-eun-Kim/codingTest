import sys

s = input()
q = int(input())
questions = [sys.stdin.readline().split() for _ in range(q)]

# dp dictionary key: 문자열, value: 해당 index까지 문자가 몇 개 나왔는지 누적 표시하는 리스트
dp = {}
chars = list(set(s)) # 반복 피하기 위해 set
len_s = len(s)

for j in range(len(chars)):
    dp[chars[j]] = [0]*len_s  # dictionary value가 될 list 초기화(문자열 길이만 한 list)

dp[s[0]][0] = 1  # index 에러 방지

for i in range(1, len_s):
    for char in chars:
        dp[char][i] = dp[char][i-1]
    dp[s[i]][i] += 1  # 해당 문자가 위치하는 index에 +1

for question in questions:
    target, left, right = question[0], int(question[1]), int(question[2])
    if target not in dp:  # 오답노트: 이 조건 안 해서 key error 발생했음(딕셔너리 주의!!)
        print(0)
        continue
    if left == 0:  # index error 방지 목적(left-1)
        if dp[target][left] == 1:
            # s의 첫 문자가 내가 찾던 문자일 때, 문자 등장하는 순간 dp 값 증가함을 고려하여 +1
            print(dp[target][right] - dp[target][left] + 1)
            continue
        print(dp[target][right] - dp[target][left])
        continue
    else:
        # 문자가 등장하는 순간 dp 값이 증가하기 때문에 left-1을 써야 함
        print(dp[target][right]-dp[target][left-1])

# for question in questions:
#     target, left, right = question[0], int(question[1]), int(question[2])
#     value = s[left:right+1].count(target)
#     print(value)7-+