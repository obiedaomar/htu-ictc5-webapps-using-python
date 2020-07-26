from shape import Shape

# Circle class


class Circle(Shape):
    pass
    # TODO: Implement __init__() for this class

    def __init__(self, radius=1.0):
        # Remember this is a subclass of Shape!
        self.radius = radius

    # TODO: Implement find_area() for this class
    def find_area(self):
        return 3.14 * self.radius**2

    # TODO: Implement find_circumference() for this class
    def find_circumference(self):
        return 2 * 3.14 * self.radius
