import math

arry = [1, 2, 3, 4, 5]
arry2 = [3, 2, 1]


def product_of_nums(nums):
    lst = []
    for i in range(len(nums)):
        num = nums[i]
        nums.pop(i)
        result = math.prod(nums)
        lst.append(result)
        nums.insert(i, num)
    return lst


print(product_of_nums(arry))
