nums = [1, 3, 4, 5, 3 , 2, 1]
print(list(set(nums)))


for num in nums:
    while nums.count(num) > 1:
        nums.remove(num)
print(nums)


res = []
for num in nums:
    if num not in res:
        res.append(num)
print(res)