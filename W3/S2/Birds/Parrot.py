class Parrot:

    # class attribute
    species = "bird"

    # __init__ method
    def __init__(self, name, age):
        # instance attribute
        self.name = name
        self.age = age
        self.color = ""
        self.has_flat_beak = False
        self.allowed_foods = ["seeds", "nuts", "grapes"]

        print(f'''
 \\\\
 (o>
 //\\
_V_/__
 ||
 ||\n\n This is {self.name}, {self.age} years old. \n\n''')

 # instance method

    def sing(self, song):
        print(f"{self.name} sings {song}.")

    def dance(self):
        return f"{self.name} is now dancing."

    def change_color(self, color):
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        if self.color == "":
            return f"{self.name} has not color."
        else:
            return self.color

    def eat(self, food):
        if food in self.allowed_foods:
            print(f"{self.name} is eating {food}.")
        else:
            print(f"Yuck! {self.name} does not eat {food}.")

    def celebrate_birthday(self):
        print(f"I am {self.name}. I am {self.age} years old.")
        if self.age > 3:
            self.allowed_foods.append("cake")
            self.eat("cake")
            self.age += 1
            print("Yummy cake!")
        else:
            print("Haha! Nice try, maybe next year.")


# instantiate the Parrot class
blu = Parrot("Blu", 2)
woo = Parrot("Woo", 4)

blu.species = "Exotic birds"
print(Parrot.species)

print(f"{blu.name} is a {blu.species}.")
print(f"{woo.name} is a {woo.species}.")

# print the type of both instances
# print(type(blu), type(woo))

# if blu == woo:
#     print("'blu' is 'boo'")
#     print(woo, blu)
# else:
#     print("'blu' is not 'woo'")
#     print(woo, blu)

# change the attributes
woo.age = 5
woo.has_flat_beak = True
blu.age = 3

# access the instance attributes
print(f"{blu.name} is {blu.age} years old.")
print(f"{woo.name} is {woo.age} years old.")

# calling the instance methods

# blu.sing("I love you")
# woo.sing("Happy")
# print(blu.dance())

# print current color then change it
# blu.color = "Red"           # Direct changing on attribute
# blu.change_color("White")   # Calling a method like dance()
# print(blu.color)

# print(blu.name)             # Direct reading from the attribute 'name'
# print(blu.get_name())       # Getting the name using a method call 'get_name()'

# blu.change_color("Pink")    # Set an attibute 'color' using a setter method
# print(blu.get_color())      # Get the attribute 'color' using a getter method

# woo.allowed_foods = ["seeds"]   # Set what woo can eat
# woo.eat("grapes")               # eat "grapes"
# woo.eat("seeds")                # eat "seeds"

# blu.eat("grapes")               # eat "grapes"
# blu.eat("seeds")                # eat "seeds"

# blu.celebrate_birthday()
# woo.celebrate_birthday()

# print(f"{blu.name} is {blu.age}. {woo.name} is {woo.age}.")

# print(f"{woo.name} can eat {woo.allowed_foods}.")
# print(f"{blu.name} can eat {blu.allowed_foods}.")

# # access the class attributes
# print(f"Blu is a {blu.species}.")
# print(f"Woo is also a {woo.species}.")

# # call our instance methods
# print(blu.sing("'Happy'"))
# print(blu.dance())
