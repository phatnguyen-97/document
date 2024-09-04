"""
Unpacking and packing
If you want to unpack the first few elements of a list and don’t care about the other elements, you can:

First, unpack the needed elements to variables.
Second, pack the leftover elements into a new list and assign it to another variable.

By putting the asterisk (*) in front of a variable name, you’ll pack the leftover elements into a list and assign them to a variable.
"""

colors = ["red", "blue", "green", "orange"]
red, blue, *other = colors

print(red)  # Output: red
print(blue)  # Output: blue
print(other)  # Output: ['green', 'orange']
