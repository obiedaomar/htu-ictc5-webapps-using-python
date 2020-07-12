# Create a function `first_upper(astring)` which returns the first letter in the string in upper case.

# first_upper(astring)


def first_upper(astring):
    return str(astring[0]).capitalize()


# Call first_upper(astring)
print(first_upper("hello"))
print(first_upper("Hello"))
