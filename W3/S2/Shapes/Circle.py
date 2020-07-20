class Circle:

    # class attributes
    pi = 3.1415

    def __init__(self, radius=1.0):

        # instance attributes
        self.radius = float(radius)

    # overriding the string representation method
    def __str__(self):
        return f"r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}"

    def get_area(self):
        return self.radius * self.radius * Circle.pi

    def get_circumference(self):
        return 2 * Circle.pi * self.radius

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

# Playground


c1 = Circle(3)
c2 = Circle()   # radius = 1

# change the colors
c1.set_color("black")
c2.set_color("white")

# print the colors
print(c1.get_color())
print(c2.get_color())

# pring the circles or "objects"
print(c1)
print(c2)

# c1.my_new_field = True
# print(c1.my_new_field)

# print the radius
print(f"C1: r = {c1.radius} a = {c1.get_area()}.")
print(f"C2: r = {c2.radius} a = {c2.get_area()}.")

# print the circumference using the getter method
print(f"c1 = {c1.get_circumference()}")
print(f"c2 = {c2.get_circumference()}")
