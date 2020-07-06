# get vs [] for retrieving elements
course = {'name': 'PythonWeb', 'code': 'ICTC5',
          'number_of_hours': 180, 'active': True}

# Output: Python
print(course['name'])

# Output: ICTC5
print(course.get('name'))

# Trying to access keys which doesn't exist throws error
# Output None
print(course.get('location'))

# KeyError
# print(course['location'])

# add item
course['location'] = 'Online'

# Output: {'location': 'Online', 'code': 'ICTC5', 'name': 'PythonWeb'}
print(course)

# Length
print(len(course))
print("The dictionary contains %s " % str(course))
print(type(course['active']))

# Clearing a dictionary
# course.clear()
# print(course)  # Output: {}

# Copying a dictionary
other_course = course.copy()
print(course)
print(other_course)

# Getting all items
items = course.items()  # Return  a list of tuples
print(items, type(items))

print(items[0], type(items[0]))

active_key, active_value = items[0]

print(active_key, type(active_key))
print(active_value, type(active_value))

# Getting all values and keys
values = course.values()
keys = course.keys()

print(values, type(values))
print(keys, type(keys))
