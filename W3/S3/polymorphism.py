# A simple Python function to explain polymorphism


def poly_add(a, b=0, c=0):
    return a + b + c


# call the method
print(poly_add(2, 3))
print(poly_add(2, 3, 4))
print(poly_add(3))


# polymorphism with built-in functions
print(len("some string"))
print(len([1, 2, 3]))
