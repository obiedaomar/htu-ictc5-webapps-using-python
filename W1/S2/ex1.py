# Packing a tuple

colors = ("Red", "Blue", "Green")
print("The type of 'colors' is: %s" % type(colors))
print("The tuple contains: %s" % str(colors))

# Print an element
print(colors[0])
print(colors[1])
print(colors[-1])

# Unpacking a tuple
color1, color2, color3 = colors
# print(color1)
# print(color1, color2, color3)

# Print the length
print(len(colors))

# Count the number of occurences
print(colors.count('Red'))

# Find the index of an element
print(colors.index('Red'))

# Max and min for tuples

t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)

t3 = t1*4 + t2

print(t3)
print("Is 3 in t1? %s" % (3 in t1))

print(t1[0])

print("The maximum in t1 is: %d" % max(t1))
print("The minimum in t1 is: %d" % min(t1))
