
from Bird import Bird

import random

# Penguin class (child)


class Penguin(Bird):

    # __init__ method for the Penguin object
    def __init__(self, name, age):

        # call super().__init__() function
        super().__init__(name, age)

        # instance attributes
        self.name = name
        self.age = age

        # print the penguin
        print("A new penguin waddless in.")

    # instance methods

    def run(self):
        print("Waddle. Waddle.")

    def find_krill(self):
        rnd_int = random.random()  # 0.0 - 1.0

        if rnd_int > 0.5:
            print("<>< <>< <><")
            super().eat("krill")
        else:
            print("No fish today!")

    # overridden method
    def fly(self):
        print("I am a penguin! I cannot fly.")
