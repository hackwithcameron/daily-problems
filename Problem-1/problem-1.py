nums = [10, 15, 3, 7, 9, 16]


def nums_that_equal(num, k):
    if [True for i in num for j in num if i + j == k]:
        return True
    else:
        return False


test_k = [5, 8, 9, 12, 50, 20, 25]

for test_num in test_k:
    value = nums_that_equal(nums, test_num)
    print(f"k = {test_num} and test is {value}")
