# 이것이 코딩테스트다 113p
# 시각
# 실패한 코드

n = int(input())

cnt = 0
result = 0
i = 3599

while(i >= 0):
    if i//600 == 3:
        cnt+=600
        i-=600
    elif (i%600)//60 == 3:
        cnt+=60
        i-=60
    elif ((i%600)%60)//10 == 3:
        cnt+=10
        i-=10
    elif ((i%600)%60)%10 == 3:
        cnt+=1
        i-=1
    else:
        i-=1


for j in range(n+1):
    if j == 3 or j == 13 or j == 23:
        result+=1
    else:
        result+= cnt

print(result)
        
            
