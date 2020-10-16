"""
Generates a banner using the decorator function like

+-------------------+
|                   |
 This is a test post
|                   |
+-------------------+
"""


def make_frame(func):
    def inner(name):
        print("+"+"-"*len(name)+"+")
        print("|"+" "*len(name)+"|")
        print(" " + name)
        print("|"+" "*len(name)+"|")
        print("+"+"-"*len(name)+"+")

    return inner


@make_frame
def get_name(name):
    pass


get_name('This is a test post')
