'''Considering reuse (modularisation)
when creating python programs'''


def greet():
    print("Hello, World!")


# Additional activity - create a calculator class and re-use this by instantiating it in the main.py
class Calculator:
    def __init__(self, a, b):
        self.a = 3
        self.b = 5

    def calculate(self):
        return self.a + self.b


# So as not to contaminate your global
# namespace, it is good practice to use a
# main function.


# so that we can reuse our code as both a
# module and a script
# we can use an if statement to ensure
# that some code is only executed when name is __main__
if __name__ == '__main__':
    print(__name__)  # module name when imported
    # above is __main__ when running directly
    pass
    # main() # only called when a script
