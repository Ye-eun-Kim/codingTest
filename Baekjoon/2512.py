n = int(input())
requests = list(map(int, input().split()))
m = int(input())

sum_requests = sum(requests)

if sum_requests <= m:
    print(max(requests))

else:
    temp = []
    avg = m//n
    diff = sum_requests - m
    for request in requests:
        if request > avg:
            temp.append(request)
    num_overs = len(temp)
    if diff % num_overs == 0:
        sub = diff // num_overs
    else:
        sub = diff // num_overs + 1
    avg_temp = sum(temp)/len(temp)
    print(int(avg_temp - sub))