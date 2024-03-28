# 이것이 코딩테스트다 115p
# 왕실의 나이트
import time


plan = input()

start_time = time.time()

char = plan[0]
num = int(plan[1])

cnt = 0
result = 0

if char == 'a' or char == 'h':
    cnt = 2
elif char == 'b' or char == 'h':
    cnt = 3
else:
    cnt = 4

if num == 1 or num == 8:
    cnt += 2
elif num == 2 or num ==  7:
    cnt += 3
else:
    cnt += 4

if cnt == 4:
    result = 2
elif cnt == 5:
    result = 3
elif cnt == 6:
    result = 4
elif cnt == 7:
    result = 6
else:
    result = 8

print(result)

end_time = time.time()

print("Time: ", end_time - start_time)