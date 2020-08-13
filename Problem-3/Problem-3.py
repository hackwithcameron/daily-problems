test_arry = [3, 4, -1, 1]
test_arry2 = [1, 2, 0]
test_arry3 = [-1, -5, -3]
test_arry4 = [123, 12, 13, 14, 160, 16, -100, -14, -23]


def find_first_missing_pos(arry):
    arry.sort()  # Sort Array from least to greatest
    if arry[-1] > 0:  # Check if there are any positive numbers in array.
        for i in range(len(arry)):
            if arry[i] >= 0:  # Check if number at index "i" in array is positive
                try:
                    # Check to see if next number in array is the next number numerically
                    if arry[i + 1] != arry[i] + 1:
                        return print(arry[i] + 1)  # If next number was not in numerical order return missing number
                except IndexError:  # Catch index error and return the last indexed number in array + 1
                    return print(arry[i] + 1)
    else:
        return print("There are no positive numbers in the array.")


find_first_missing_pos(test_arry)
find_first_missing_pos(test_arry2)
find_first_missing_pos(test_arry3)
find_first_missing_pos(test_arry4)
