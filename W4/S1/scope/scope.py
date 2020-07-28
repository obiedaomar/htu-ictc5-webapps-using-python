# Scope

a, b, c = 1, 2, 3

# Define a function to print the values


def print_values(a, b, c):
    print(f"A: {a}. B: {b}. C: {c}.")


def some_other_function(x, y, z):
    # local scope
    a, b, c = x, y, z
    print_values(a, b, c)


def another_function():
    # local scope
    a, b, c = 0, 0, 0
    print_values(a, b, c)


def global_function():
    # global a, b, c
    a, b, c = 9, 9, 9
    print_values(a, b, c)


# What would this do?
# some_other_function(4, 5, 6)
# another_function()
# global_function()
print_values(a, b, c)
