nums = [1, 2, 1, 3, 2, 1, 1]


for num in nums:
    while nums.count(num) % 2 == 0 and num in nums:
        nums.remove(num)
        nums.remove(num)
print(nums)