"""Comprehension is a technique of shorthanding loops to generate list, dict or tuples.
"""

"""
List comprehension

List comprehension is used generate a list by computing values that requires iteration.
A simple loop is written as:
for val in vals:
    //do an operation here

In list comprehension the syntax is used as follows.
[val for val in vals if condition)]
Similarly loops can be nested too
"""

from py import code


nums = [1, 2,3,4,5]
double_nums = [x*2 for x in nums]
print(double_nums)

# Example of generating a list of number from 1 to 10
for num in range(0,10):
    print(num+1)

# The above example can also be written as:
nums = [num + 1 for num in range(0, 10)]
print(nums)

# Although irrelevant but the simplest way would be the following
print(list(range(1,11))) # This would produce the same result as above.

# Example of nested comprehension

nums = [1, 2,3,4,5]
double_nums = [val*2 for val in [x*2 for x in nums]]
print(double_nums)

# Similarly multiple for can be ran inside a single list comprehension
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)