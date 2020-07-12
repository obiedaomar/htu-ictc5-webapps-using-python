# Create a function `last_two(astring)` which returns the last two characters as a tuple. If there are less than two characters, return the value "Error".

# last_two(astring)


def last_two(astring):
    if len(astring) < 2:
        return "Error"
    return tuple(astring[-2: len(astring)])

# Call last_two(astring)


print(last_two("hello"))
