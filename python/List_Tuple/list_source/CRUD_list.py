list_elements = ["Phat", "Nguyen", "Tan"]

# Access last element
print(list_elements[-1])  # Output: Tan

# Add new List element
list_elements.append("DC")
print(list_elements)  # Output: ['Phat', 'Nguyen', 'Tan', 'DC']

# Modify List element
list_elements[-1] = "DC22"
print(list_elements)  # Output: ['Phat', 'Nguyen', 'Tan', 'DC22']

# Add new List element in any order
list_elements.insert(2, "Test")  # Output: ['Phat', 'Nguyen', 'Test', 'Tan', 'DC22']
print(list_elements)

# Remove elements from list
del list_elements[2]
print(list_elements)  # Output: ['Phat', 'Nguyen', 'Tan', 'DC22']

# Remove last element from list and return that element
last = list_elements.pop()
print(last)  # Output: DC22
print(list_elements)  # Output: ['Phat', 'Nguyen', 'Tan']

second = list_elements.pop(2)
print(second)  # Tan
print(list_elements)  # Output: ['Phat', 'Nguyen']

# Remove by value
list_elements.remove("Nguyen")
print(list_elements)  # Output: ['Phat']
