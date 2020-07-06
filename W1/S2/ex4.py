# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
print(squares.pop(4))  # 16
print(squares.pop(5))  # 25

# # Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares, type(squares))

# # remove an arbitrary item, return (key,value)
item = squares.popitem()
item_key, item_value = item

print(item, type(item))  # (3, 9)
print(item_key, type(item_key))  # 3, int
print(item_value, type(item_value))  # 9, int

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# # remove all items
squares.clear()

# # Output: {}
print(squares)

# # delete the dictionary itself
# del squares  # free()

# # Throws Error
# print(squares)
