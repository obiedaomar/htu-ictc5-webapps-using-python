# Comparison and Logical Operators

# Comparison Operators

# Evaluate this

x = 5
y = 8

# Output: x > y is False
print(f'{x} > {y} is', x > y)

# Output: x < y is True
print('%d < %d is %s' % (x, y, x < y))

# Output: x == y is False
print('x == y is', x == y)

# Output: x != y is True
print('x != y is', x != y)

# Output: x >= y is False
print('x >= y is', x >= y)

# Output: x <= y is True
print('x <= y is', x <= y)

# Evaluate this

print(1 == 2 or 2 < 3)  # True
print(0 == -1 or (4 < 8 and 2 != 3))  # True

# Logical Operators

x = True
y = False

print(f'x= {x} and y= {y} is: ', x and y)
print(f'x= {x} or y= {y} is:', x or y)
print(f'not x= {x} is:', not x)
