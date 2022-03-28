"""The benefit of using set datatype is that set operation can be performed for the element.
"""

# Union

"""Union can be used by using either the pipe | operator or using the union() function.
Either way, the function will return a union of both sets.
"""
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)    
print(set_A.union(set_B))
print(set_B.union(set_A))

"""Similarly, intersection can be performed using the & operator or the intersection() keyword.
"""

set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

print(set_A & set_B)
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))

"""Difference can be used to perfrom a difference between one list and another. Difference can be
used by using either the - operator or the difference() function.
"""
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}


print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))