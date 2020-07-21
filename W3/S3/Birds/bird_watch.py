from Bird import Bird
from Penguin import Penguin
from Parrot import Parrot


def print_bird(bird):
    Bird.who_is_this(bird)


# instantiate the Parrot class
blu = Parrot("Blu", 2)
woo = Parrot("Woo", 4)

# instantiate the Parrot class
some_bird = Bird("Some", 12)

# instantiate the Penguin class
peggy = Penguin("Sue", 3)


# print(blu.name, woo.name, some_bird.name, peggy.name)
# print(blu.age, woo.age, some_bird.age, peggy.age)

# run some methods on peggy

peggy.run()
peggy.who_is_this()
peggy.fly()

peggy.find_krill()
peggy.find_krill()
peggy.find_krill()

# run some methods on blu

blu.who_is_this()
blu.fly()
blu.eat("fish")
blu.eat("seeds")

# run some methods on blu
woo.eat("seeds")
woo.celebrate_birthday()

# run some methods on some_bird

# some_bird.who_is_this()
# some_bird.fly()

# print the bird

print_bird(peggy)
print_bird(blu)
print_bird(some_bird)

# print some objects

print(blu)
print(peggy)
print(some_bird)

# checks with isinstance()

# print(isinstance(blu, Parrot))
# print(isinstance(woo, Bird))
# print(isinstance(some_bird, Bird))
# print(isinstance(some_bird, Parrot))    # False
# print(isinstance(peggy, Bird))
# print(isinstance(peggy, Penguin))
# print(isinstance(woo, Penguin))         # False
