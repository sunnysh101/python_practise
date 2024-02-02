# Super keyword


# Super keyword is used to call the parent class method from the child class

# Example of super keyword
class A:
    def __init__(self):
        print("Class A")

    def print_hi(self):
        print("Hello from A")


class B(A):
    def __init__(self):
        print("Class B")

    def print_hello(self):
        print("Hello from B")


class C(B):
    def __init__(self):
        print("Class C")

    def print_hello(self):
        self.print_hi()
        super().print_hello()
        print("Hello from C")


c = C()
c.print_hello()

# The above example would print "Hello from C" as the method is overridden in the child class.
# To call the parent class method we can use the super keyword as follows:

# Super can be used with the init method as well
# Example of super keyword with init method

class A:
    def __init__(self):
        print("Class A")


class B(A):
    def __init__(self):
        print("Class B")
        super().__init__()

    def print_hello(self):
        print("Hello from B")


class C(B):
    def __init__(self):
        print("Class C")
        super().__init__()

    def print_hello(self):
        super().print_hello()
        print("Hello from C")
