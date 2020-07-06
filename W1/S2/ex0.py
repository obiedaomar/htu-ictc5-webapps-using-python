# Declaring a list
linux_distros = ['Debian', 'Ubuntu', 'Fedora',
                 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']

# Print the list
print("The list contains %s." % linux_distros)
print("The type of 'linux_distros' is '%s'." % type(linux_distros))

# Finding the length
print("The list contains %d elements." % len(linux_distros))

# Append an element
linux_distros.append("Mint")
print("The new list contains %s." % linux_distros)

# Pop an element
my_element = linux_distros.pop()
print("The popped element is: '%s'." % my_element)
print("After popping the element the new list contains %s." % linux_distros)

linux_distros.pop(4)
print(linux_distros)

# # Insert an element
print(linux_distros[4])
linux_distros.insert(2, "Mint")
print(linux_distros)
print(linux_distros[4])

# Remove an element
linux_distros.remove("Arch")
print(linux_distros)

# Extending a list
debian_distros = ['Debian', 'Ubuntu', 'Mint']
linux_distros.extend(debian_distros)
print(linux_distros)

# Find the index of an element
# print(linux_distros.index("Arch"))
print(linux_distros.index("Mint"))

# # Reverse the list
# print(linux_distros)
# linux_distros.reverse()
# print(linux_distros)

# # Sort the list
# print(linux_distros)
# linux_distros.sort()
# print(linux_distros)

# What does this do?
linux_distros.sort()
linux_distros.reverse()
print(linux_distros)
