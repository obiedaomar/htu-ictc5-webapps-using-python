# Create a function `sum_ten(n1, n2)` which returns a Boolean True if the sum of the numbers is 10. Otherwise, return the actual sum value.

# sum_ten(x,y)


def sum_ten(x, y):
    if x + y == 10:
        return True
    return (x + y)


# Call sum_ten(x, y)
print(sum_ten(10, 2))
print(sum_ten(2, 2))
print(sum_ten(8, 2))
