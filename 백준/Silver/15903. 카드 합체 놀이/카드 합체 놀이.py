n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for i in range(m):
    temp = nums[0]+nums[1]
    nums[0], nums[1] = temp, temp
    nums.sort()

print(sum(nums))