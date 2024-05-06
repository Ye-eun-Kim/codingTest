# 이것이 코딩테스트다 113p
# 시각
# 실패해서 GenAI의 도움을 받아 코드를 수정함

n = int(input())
result = 0

for i in range(n+1):
    if i%10 == 3 or (i//10) == 3:
        # result+=1  --- 나의 잘못된 기존 코드
        result += 3600
    else:  # 심지어 이 else를 처음에 썼다가 지워버림... if문이 충족되면
        # 당연하게 다음 코드가 실행되지 않는다고 생각함. 바보!
        for j in range(60):
            if j%10 == 3 or (j//10) == 3:
                # result+=1
                result+=60
            else:
                for k in range(60):
                    if k%10 == 3 or (k//10) == 3:
                        result+=1

print(result)




'''
초간단 코드!!


h = int(input())
result = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1

print(count)

'''