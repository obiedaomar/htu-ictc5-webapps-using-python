# The range() function

for i in range(5):
    # What would this print?
    print(i)

for i in range(5, 10):
    # What would this print?
    print(i)

for i in range(0, 10, 3):
    # What would this print?
    print(i)

# Using range() with lists

words = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(words)):
    print("Word at index %d is '%s'." % (i, words[i]))


# Evaluate this
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
            # loop fell through without finding a factor
        print(n, 'is a prime number')

# Evalute this
x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
        print(x)

# Evaluate this
x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
