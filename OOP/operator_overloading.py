# Operator overloading in Python

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    # Overloading the '==' operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overloading the '>' operator
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    # Overloading the '<' operator
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    # Overloading the print() function
    def __str__(self):
        return f'<{self.x}, {self.y}>'
    
    def __len__(self):
        return 100

p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 + p2)  # Output: (3, 5)
print(p1 == p2)  # Output: False
print(p1 > p2)  # Output: False
print(p1 < p2)  # Output: True
print(p1)  # Output: (1, 2)

print(len(p1))

