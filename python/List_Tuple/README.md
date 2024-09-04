## What is a List
- A `list` is an ordered collection of items. </br>
- Python uses the square brackets ([]) to indicate a `list`. The following shows an `empty list`: </br>

```python
empty_list = []
```
- When we create a List object, it takes 56 bytes of memory. </br>
- [List Overall](./list_source/list.py) </br>
- [List CRUD](./list_source/CRUD_list.py) </br>
- [List Sort](./list_source/sort_list.py) </br>
    - The `sort()` method sorts a list in place. In other words, it changes the order of elements in the original list. </br>
    - To return the new sorted list from the original list, you use the `sorted()` function </br>
- [List Slice](./list_source/slice_list.py) </br>
    - Syntax `sub_list = list[begin: end: step]` </br>
    - To get the n-first elements from a list, you omit the first argument: `list[:n]` </br>
    - To get the n-last elements from a list, you use the negative indexes: `list[-n:]` </br>
    - Using Python List slice to get every nth element from a list: `sub_list = list[::step]` </br>
    - Using Python List slice to reverse a list: `reversed_list = list[::-1]` </br>
    - Using Python List slice to substitute part of a list </br>
    - Using Python List slice to partially replace and resize a list </br> 
    - Using Python list slice to delete elements: `del list[start:end]`</br> 
- [List Unpack](./list_source/unpack_list.py) </br>

## What is Tuple?
- Sometimes, you want to create a list of items that cannot be changed throughout the program. `Tuple` allows you to do that. </br>
- A `Tuple` is a list that cannot change (immutable list). Python refers to a value that cannot change as immutable. So by definition, a `Tuple` is an `immutable list`. </br>
- [Tuple Overall](./tuple_source/tuple.py) </br>