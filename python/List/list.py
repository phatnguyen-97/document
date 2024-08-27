import sys

list_items = [1, 2, 3, 4, 5, 6]
list_items_2 = []

print(list_items)
print(id(list_items))

print(sys.getsizeof(list_items[0]))  # Output: 28 bytes for each element's value
print(
    sys.getsizeof(list_items)
)  # Output: 104 = 56 + 8*6 (reference to variables in list)= bytes
print(sys.getsizeof(list_items_2))  # Output: 56 bytes

# It will takes 104 + 28*6 = 272 bytes for all
print(list_items[-1])
