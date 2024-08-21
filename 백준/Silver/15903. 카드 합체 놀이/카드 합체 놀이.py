import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(m):
    temp = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, temp)
    heapq.heappush(heap, temp)

print(sum(heap))


# heapq를 모를 때 작성한 코드(이하)

# import sys
#
# n, m = map(int, input().split())
# nums = sorted(list(map(int, sys.stdin.readline().split())))
#
# for i in range(m):
#     temp = nums[0]+nums[1]
#     nums[0], nums[1] = temp, temp
#     nums.sort()
#
# print(sum(nums))