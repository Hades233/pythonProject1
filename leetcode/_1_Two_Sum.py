def twoSum(nums, target):
    for m in range(len(nums) - 1):
        for n in range(m + 1, len(nums)):
            temp = nums[m] + nums[n]
            if temp == target:
                return [m,n]


nums1 = [2, 3, 4, 5, 6, 7]
target1 = 12
twoSum(nums1, target1)
