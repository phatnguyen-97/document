list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Full Slice
sub_list = list[2:5:1]
print(sub_list)  # Output: [2, 3, 4]

# Get n-first elements
sub_list_2 = list[:2]
print(sub_list_2)  # Output: [0, 1]

# Get n-last elements
sub_list_3 = list[-2:]
print(sub_list_3)  # Output: [8, 9]

# Get n-th elements with step
sub_list_4 = list[::2]
print(sub_list_4)  # Output: [0, 2, 4, 6, 8]

# Using Python List slice to reverse a list
sub_list_5 = list[::-1]
print(sub_list_5)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Using Python List slice to substitute part of a list
list[0:2] = ["Phat", "Nguyen"]
print(list)  # Output: ['Phat', 'Nguyen', 2, 3, 4, 5, 6, 7, 8, 9]

# Using Python List slice to partially replace and resize a list
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print(f"The list has {len(colors)} elements")  # 7

colors[0:2] = ["black", "white", "gray"]
print(
    colors
)  # Output: ['black', 'white', 'gray', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(f"The list now has {len(colors)} elements")  # 8
