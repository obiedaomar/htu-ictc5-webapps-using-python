some_string = "Hello, world!"
another_string = "Hello again!"

string_length = len(some_string)
another_length = len(another_string)

print("The length of the string '%s' is %d." % (some_string, string_length))
print("The length of the string '%s' is %d." %
      (another_string, another_length))

print("The length of the string is: %d" % len(some_string))


print("The index of the first 'o' in 'some_string' is: %d" %
      some_string.index('o'))

print("The index of the first 'l' in 'some_string' is: %d" %
      some_string.index('l'))

print("The count of 'l' in 'some_string' is: %d" % some_string.count('l'))
print("The count of 'o' in 'another_string' is: %d" %
      another_string.count('o'))

print("A substring between 3 and 7 from 'some_string' is: %s" %
      some_string[3:7])

print("A substring between 2 and 8 with steps of 2 from 'some_string' is: %s" %
      some_string[2:8:2])


print("This is the uppercase version of 'some_string': %s" % some_string.upper())
print("This is the lowercase version of 'some_string': %s" % some_string.lower())
print("This is the capitalized version of 'some_string': %s" % some_string.capitalize())


print("Splitting 'some_string' by the ',' gives us: %s" %
      some_string.split(','))
