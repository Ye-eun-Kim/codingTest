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
