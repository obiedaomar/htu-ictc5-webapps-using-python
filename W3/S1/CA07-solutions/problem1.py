# factorial_print(number)


def factorial_print(number):

    factorial = 1

    if number < 0:
        print(f"{number}! does not exist.")
    elif number == 0:
        print("0! = 1")
    else:
        for i in range(1, number + 1):
            factorial = factorial*i
        print(f"{number}! =", factorial)


# factorial_return(number)


def factorial_return(number):

    factorial = 1

    if number < 0:
        return None
    elif number == 0:
        return factorial
    else:
        for i in range(1, number + 1):
            factorial = factorial*i
        return factorial

# factorial_return(number)


def factorial_recursive(number):

    if number < 0:
        return None
    elif number == 0:
        return 1
    else:
        return number * factorial_recursive(number - 1)


# call factorial_print(number)
factorial_print(7)
factorial_print(-1)
factorial_print(1)

# call factorial_return(number)
print(factorial_return(7))
print(factorial_return(-1))
print(factorial_return(1))

# call factorial_recursive(number)
print(factorial_recursive(7))
print(factorial_recursive(-1))
print(factorial_recursive(1))
