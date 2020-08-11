import math

# Test Arrays
arry = [1, 2, 3, 4, 5]
arry2 = [3, 2, 1]


def product_of_nums(nums):
    lst = []  # Create empty list

    for i in range(len(nums)):  # Loop through input list using index value
        num = nums[i]  # Sets num equal to the value of the number at index "i" in nums
        nums.pop(i)  # Removes value at index "i"
        result = math.prod(nums)  # Finds product of entire list with value at index "i" removed
        lst.append(result)  # appends the result to the new list
        nums.insert(i, num)  # re-insert the original number at index "i" back into place

    return lst  # Return list once complete


print(product_of_nums(arry))
print(product_of_nums(arry2))

