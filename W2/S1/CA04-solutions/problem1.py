# Create a function `check_ten(n1, n2)` which returns a Boolean True if the sum of the numbers is 10.

# check_ten(x,y)


def check_ten(x, y):
    if x + y == 10:
        return True
    return False

# A faster and more efficient way
# def check_ten(x, y):
#     return (x + y == 10)


# Call check_ten(x,y)
print("10, 5,", check_ten(10, 5))
print("15, 5,", check_ten(15, 5))
print("5, 5,", check_ten(5, 5))
print("20, 5,", check_ten(20, 5))
