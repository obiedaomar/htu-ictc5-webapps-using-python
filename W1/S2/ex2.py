# Declare a set
s = {1, 2, 3}

# Adding elements
s.add(4)
print(s)  # {1, 2, 3, 4}

s.add(5)
print(s)  # {1,2,3,4,5}

# Length of a set
print(len(s))

# Copy a set
another_s = s.copy()
print(another_s)  # {1, 2, 3, 4, 5}

# Difference between sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

x = set1.difference(set2)

print(x)  # {1}
y = set2.difference(set1)
print(y)  # {4}

# # Intersection of sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

x = set1.intersection(set2)
print(x)  # {2,3}
y = set2.intersection(set1)
print(y)  # {2,3}

# Union of sets
set1 = {1, 2, 3, 4, 4}
set2 = {2, 3, 4}
x = set1.union(set2)
print(x)  # {1,2,3,4}

# Remove an element
set1.discard(4)

# Pop an element
print(set1)
value = set1.pop()
print(set1)

# Membership check
print("Is 3 a member of set1? %s" % (3 not in set1))
