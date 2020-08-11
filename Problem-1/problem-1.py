nums = [10, 15, 3, 7, 9, 16]


def nums_that_equal(nums, k):
    numbers = []
    for i in nums:
        for j in range(len(nums)):
            if nums[j] + i == k:
                numbers.append((nums[j], i))
    return numbers


print(nums_that_equal(nums, 17))
