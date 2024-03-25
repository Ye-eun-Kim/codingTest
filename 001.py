# 이것이 코딩테스트다 92p
# 큰 수의 법칙

N, M, K = input().split()
N = int(N)
M = int(M)
K = int(K)

li = input().split()
li = list(map(int, li))
li.sort(reverse=True)
li = li[0:2]

cnt = 0
tot = 0
while cnt < M :
    v = li.pop(0)
    li.append(v)
    for i in range(0, K):
        tot+=v
        cnt+=1
        if v < li[0]:
            break
        if cnt == M:
            break

print(tot)



'''


<정답 코드 1>
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m == 0:
        break
    result += second
    m-=1

print(result)


'''

'''


<정답 코드 2>
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k + m%(k+1)

result = 0
result += count*first
result += (m-count)*second

print(result)


'''