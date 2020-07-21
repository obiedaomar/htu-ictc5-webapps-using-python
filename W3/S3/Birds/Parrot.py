from Bird import Bird

import random
# Parrot class (child)


class Parrot(Bird):

    # __init__ method for the Parrot object
    def __init__(self, name, age):

        # call super().__init__() function
        super().__init__(name, age)

        # instance attribute
        self.level = int(random.random()*10)
        self.has_birthday_today = False

    # string representation
    def __str__(self):
        # return the parrot
        return f'''
        \\\\
        (o>
        //\\
        V_/__
        ||
        ||\n\n This is {self.name}, {self.age} years old. \n\n'''

    # instance methods

    def dance(self):
        if self.level > 7:
            print(f"{self.name} is dancing a special dance.")
        else:
            super().dance()

    def celebrate_birthday(self):
        if self.age > 3:
            print(f"I am {self.name}. I am celebrating my birthday today.")

            rnd_bday = random.random()
            # print(rnd_bday)
            if rnd_bday > 0.2:
                self.has_birthday_today = True

            if self.has_birthday_today:
                self.age += 1
                self.eat("cake")
                self.dance()
            else:
                print(
                    f"There is {round(float(rnd_bday*100))}% chance that it is my birthday today.")
        else:
            print("Haha! Nice try, maybe next year.")

    # overridden method
    def eat(self, food):
        if food == "seeds" or self.has_birthday_today:
            super().eat(food)
        else:
            print(f"Yuck! Can't eat {food}.")
