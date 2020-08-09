# Flow Control - Decisions

# if statements

x = -20

if x < 0:
    print(f"{x} is a negative number.")
    print("I belong to the if.")
else:
    print(f"{x} is a positive number.")
    print("I belong to the else.")

# Evaluate this

x, y, z = 45, 10, 0

if ((x == 5 or y == 20)) or ((not z) or (not False)):
    print(f"x: {x} y: {y}. Either x == 5 or y == 20.")
else:
    print(f"x: {x} y: {y}. Niether x == 5 nor y == 20.")

# Evaluate this

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}  # Set
number_to_check = 11

if number_to_check in prime_numbers:
    print("The number %d is a prime number." % number_to_check)
else:
    print("The number %d is not a prime number." % number_to_check)

# Short hand if - One statement blocks

a, b = 2, 3
if a > b:
    print("a is greater than b")

# Short hand if..else - One statement blocks

print("A is greater.") if a > b else print("B is greater.")

# Same as the short hand form above
# if a > b:
#     print("A is greater.")
# else:
#     print("B is greater.")

# # if..elif..else statements

# Evaluate this
x = 1

if x < 0:
    print(f"{x} is a negative number.")
elif x == 0:
    print(f"{x} is a zero.")
else:
    print(f"{x} is a positive number.")

# Nested if..elif..else statements

# Evaluate this

# Read input from stdin and cast to float
number = float(input("Enter a number: "))

# Check if number is positive
if number >= 0:
    # Check if number is zero
    if number == 0:
        print(f"{number} is zero.")
    else:
        print(f"{number} is a positive number.")
# Check if number is negative
else:
    print(f"{number} a negative is number.")
