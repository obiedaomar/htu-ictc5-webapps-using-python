# Create a function `compare_length(s1, s2)` which returns the difference in length between the strings.

# compare_length(s1, s2)


def compare_length(s1, s2):
    return abs(len(s1) - len(s2))


# Call compare_length(s1, s2)
print(compare_length("ABC", "ABCD"))
print(compare_length("ABCDEFG", "ABCDEF"))
print(compare_length("AB", "ABCDEFG"))
print(compare_length("A", "A"))
print(compare_length("ABCDEFGHI", "AB"))
