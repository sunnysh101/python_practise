# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

# Suppose we have various shapes and we need to calculate their area we can use polymorphism to calculate the area of each shape.

# Example of polymorphism
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


shapes = [Circle(10), Rectangle(10, 20)]

for shape in shapes:
    print(shape.area())


# In the above example, we have two classes Circle and Rectangle both have the same method area. We can use the same method to calculate the area of each shape. This is called polymorphism.

# Another way of using polymorphism is by using the same method name in different classes. This is called method overriding.


# Example of method overriding
class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


b = B()
b.show()

# In the above example, the method show is overridden in the child class B. When we call the show method from the object of class B, it would call the method from the child class B.
