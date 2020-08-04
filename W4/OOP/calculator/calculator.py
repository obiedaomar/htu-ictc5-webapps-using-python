from operations import Operations


class Calculator:

    def __init__(self):
        print("Calcuatlor")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "You cannot divide by zero."
        else:
            return a/b

    def power(self, a, b):
        pass

    def abs(self, a):
        return abs(a)

    def pretty_print(self, operation, result):
        pass

    def get_user_input(self):

        # Ask user for operation
        print("\n Please choose an operation: \n")
        print("\t * add 2 3")
        print("\t * subtract 6 4")
        print("\t * multiply 3.14 2")
        print("\t * divide 6 1.5")

        print(
            "\n Type the operation name, first operand, then second operand. Example: add 2 3\n")
        operation = input("> ").split(' ')

        if operation[0] in ():
            print(self.add(float(operation[1]), float(operation[2])))
        elif operation[0] == Operations.SUBTRACT.name:
            print(self.subtract(float(operation[1]), float(operation[2])))
        elif operation[0] == Operations.MULTIPLY.name:
            print(self.multiply(float(operation[1]), float(operation[2])))
        elif operation[0] == Operations.DIVIDE.name:
            print(self.divide(float(operation[1]), float(operation[2])))
        else:
            print("Operation unknown or operands are missing. Try again.")
            self.get_user_input()


my_calc = Calculator()

while True:
    my_calc.get_user_input()
