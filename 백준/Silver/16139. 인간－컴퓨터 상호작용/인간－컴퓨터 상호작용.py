s = input()
q = int(input())
questions = [input().split() for _ in range(q)]

for question in questions:
    target, left, right = question[0], int(question[1]), int(question[2])
    cnt = 0
    for i in range(left, right+1):
        if target == s[i]:
            cnt += 1
    print(cnt)