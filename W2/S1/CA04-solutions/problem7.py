# Create a function `sum_or_max(my_list)`, given a list, if the length of the list is even return the sum of the list. If the length is odd, return the maximum value in that list.

# sum_or_max(my_list)


def sum_or_max(my_list):
    if len(my_list) % 2 == 0:
        return sum(my_list)
    return max(my_list)


# Call sum_or_max(my_list)
print(sum_or_max([1, 2, 3, 4, 5]))
print(sum_or_max([1, 2, 3, 4, 5, 6]))
print(sum_or_max([1, 2, 3]))
