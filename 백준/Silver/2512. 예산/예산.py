# chatGPT 코드
n = int(input())
requests = list(map(int, input().split()))
requests.sort()
m = int(input())

sum_requests = sum(requests)

if sum_requests <= m:
    print(requests[-1])
else:
    low, high = 0, requests[-1]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        total = sum(min(mid, req) for req in requests)

        if total <= m:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    print(result)


# 나의 기존 코드

'''
n = int(input())
requests = list(map(int, input().split()))
requests.sort()
m = int(input())

sum_requests = sum(requests)
tot_diff = sum_requests - m
result = 0

if tot_diff <= 0:
    print(requests[-1])

else:
    for i in range(n-1, -1, -1):
        big_num_sum = 0
        for j in range(n-1, i-1, -1):
            big_num_sum += requests[j]
        temp = (big_num_sum - tot_diff) // (n-j)
        if i == n-1:
            result = temp
        elif temp > result:
            result = temp
        else:
            break
    print(result)
'''