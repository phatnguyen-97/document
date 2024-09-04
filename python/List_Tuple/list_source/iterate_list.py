cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

for city in cities:
    print(city)
"""
Output:
New York
Beijing
Cairo
Mumbai
Mexico
"""

for item in enumerate(cities):
    print(item)
"""
Output: 
(0, 'New York')
(1, 'Beijing')
(2, 'Cairo')
(3, 'Mumbai')
(4, 'Mexico')
"""

for index, city in enumerate(cities):
    print(f"{index}: {city}")

"""
Output:
0: New York
1: Beijing
2: Cairo
3: Mumbai
4: Mexico
"""
