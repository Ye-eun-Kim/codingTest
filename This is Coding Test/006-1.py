# 이것이 코딩테스트다 115p
# 왕실의 나이트
# 답지
# ord 함수의 쓰임!!!

import time


plan = input()

start_time = time.time()

column = int(ord(plan[0]))
row = int(plan[1])

steps = [(-1,-2),(1,-2),(2,-1), (2,1), (1,2),(-1,-2),(-2,1),(-2,-1)]

result = 0

for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

end_time = time.time()

print("Time: ", end_time - start_time)