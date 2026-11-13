#  Python Lists, Tuples & Sets — Complete Beginner-to-Advanced Guide

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Lists%20%7C%20Tuples%20%7C%20Sets-orange)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-success)
![Practice](https://img.shields.io/badge/Practice-24%20Problems-purple)

> 🎯 **Goal:** Learn how Python stores collections of values, when to use lists, tuples, and sets, and how to solve common collection-based programming problems.

---

## ✨ What's inside?

| Section | What you'll learn |
|---|---|
| 📋 Lists | Ordered, changeable collections; indexing, slicing, methods and algorithms |
| 🔒 Tuples | Ordered, immutable collections; packing, unpacking and tuple operations |
| 🧩 Sets | Unique values; union, intersection, difference and membership |
| ⚖️ Comparison | How to choose the right collection for a problem |
| 🧠 Problem-solving | Logic, algorithms, examples and common patterns |
| 💻 Practice tracker | 24 problems numbered **76–99** |

## 🧭 Learning dashboard

Use the checkboxes to track your progress. On GitHub, you can tick these boxes as you learn.

- [ ] Understand what a collection is
- [ ] Learn list creation, indexing and slicing
- [ ] Practise list insertion, deletion and updating
- [ ] Learn important list methods
- [ ] Understand tuples and immutability
- [ ] Practise tuple packing and unpacking
- [ ] Understand sets and unique elements
- [ ] Practise set operations
- [ ] Compare lists, tuples and sets
- [ ] Solve all 24 practice problems

## 🗺️ Learning roadmap

```text
Python Collections
       |
       +---- Lists  ------> Ordered + Mutable + Duplicates allowed
       |
       +---- Tuples ------> Ordered + Immutable + Duplicates allowed
       |
       +---- Sets --------> Unordered + Mutable + Unique elements
       |
       +---- Practice ----> Searching, sorting, matrices and set logic
```

## 📚 Table of contents

1. [What are collections?](#-1-what-are-collections)
2. [Lists](#-2-python-lists)
3. [List indexing and slicing](#-3-list-indexing-and-slicing)
4. [Important list methods](#-4-important-list-methods)
5. [List operations and useful built-ins](#-5-list-operations-and-useful-built-ins)
6. [Tuples](#-6-python-tuples)
7. [Tuple packing and unpacking](#-7-tuple-packing-and-unpacking)
8. [Sets](#-8-python-sets)
9. [Set operations](#-9-set-operations)
10. [List vs Tuple vs Set](#-10-list-vs-tuple-vs-set)
11. [Problem-solving patterns](#-11-problem-solving-patterns)
12. [Common mistakes](#-12-common-mistakes)
13. [Practice questions 76–99](#-13-practice-questions-7699)
14. [Final revision checklist](#-14-final-revision-checklist)

---

# 🔍 1. What are collections?

A **collection** stores multiple values in one variable.

Without a collection:

```python
student1 = "Ravi"
student2 = "Priya"
student3 = "Arun"
```

With a collection:

```python
students = ["Ravi", "Priya", "Arun"]
```

Python provides several collection types. Three important ones are:

- **List:** use when the data should remain in order and may change.
- **Tuple:** use when the data should remain in order but should not be changed.
- **Set:** use when you need unique values or fast membership checking.

---

# 📋 2. Python Lists

## 2.1 What is a list?

A **list** is an ordered and mutable collection that can store multiple values. It allows duplicate values and can contain different data types.

- **Ordered:** items keep their positions.
- **Mutable:** items can be added, removed or changed.
- **Duplicates allowed:** the same value can appear more than once.
- **Mixed data types:** a list can contain integers, strings, floats and other objects.

```python
numbers = [10, 20, 30, 40]
names = ["Ravi", "Priya", "Arun"]
mixed = [10, "Python", 3.5, True]
duplicates = [10, 20, 10, 30]

print(numbers)
print(names)
print(mixed)
print(duplicates)
```

## 2.2 Creating lists

```python
# Empty list
empty = []

# List of integers
numbers = [10, 20, 30, 40]

# List of strings
languages = ["Python", "Java", "C"]

# Mixed list
data = [101, "Raghuram", 8.5, True]

# Using list()
characters = list("PYTHON")
print(characters)  # ['P', 'Y', 'T', 'H', 'O', 'N']

# Using range()
values = list(range(1, 6))
print(values)  # [1, 2, 3, 4, 5]
```

## 2.3 Taking list input

### Read integers separated by spaces

```python
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)
```

Example input:

```text
10 20 30 40
```

Output:

```text
[10, 20, 30, 40]
```

### Read values one by one using a loop

```python
n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    value = int(input("Enter a number: "))
    numbers.append(value)

print(numbers)
```

## 2.4 Updating list elements

Lists are mutable, so you can change an element using its index.

```python
numbers = [10, 20, 30]
numbers[1] = 99

print(numbers)  # [10, 99, 30]
```

## 2.5 Adding elements

```python
numbers = [10, 20, 30]

numbers.append(40)       # Add one item at the end
numbers.insert(1, 15)    # Insert 15 at index 1
numbers.extend([50, 60]) # Add all items from another iterable

print(numbers)
```

| Method | Purpose |
|---|---|
| `append(x)` | Adds one item at the end |
| `insert(i, x)` | Adds an item at a particular index |
| `extend(iterable)` | Adds every item from another iterable |

## 2.6 Removing elements

```python
numbers = [10, 20, 30, 20, 40]

numbers.remove(20)  # Removes the first matching value
print(numbers)

last = numbers.pop()  # Removes and returns the last item
print("Removed:", last)

item = numbers.pop(0)  # Removes and returns item at index 0
print("Removed:", item)

del numbers[0]  # Deletes item at index 0
print(numbers)

numbers.clear()  # Removes every item
print(numbers)
```

| Method / statement | Purpose |
|---|---|
| `remove(x)` | Removes the first occurrence of value `x` |
| `pop()` | Removes and returns the last item |
| `pop(i)` | Removes and returns item at index `i` |
| `del` | Deletes an item or a slice |
| `clear()` | Removes all items |

⚠️ `remove(x)` raises `ValueError` if `x` is not present. Check with `if x in numbers:` when necessary.

---

# 🔢 3. List indexing and slicing

## 3.1 Positive indexing

Indexing starts at `0`.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])  # 10
print(numbers[1])  # 20
print(numbers[4])  # 50
```

## 3.2 Negative indexing

Negative indexing starts from the end. `-1` means the last item.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[-1])  # 50
print(numbers[-2])  # 40
print(numbers[-5])  # 10
```

## 3.3 Slicing

Syntax:

```python
list_name[start : stop : step]
```

The `stop` index is excluded.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50, 60]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # [60, 50, 40, 30, 20, 10]
```

## 3.4 Iterating through a list

```python
numbers = [10, 20, 30]

# Direct iteration
for value in numbers:
    print(value)

# Index-based iteration
for i in range(len(numbers)):
    print(i, numbers[i])

# enumerate() gives index and value
for index, value in enumerate(numbers):
    print(index, value)
```

---

# 🛠️ 4. Important list methods

| Method | What it does | Example |
|---|---|---|
| `append(x)` | Adds one item | `a.append(5)` |
| `extend(x)` | Adds multiple items | `a.extend([5, 6])` |
| `insert(i, x)` | Inserts at an index | `a.insert(1, 5)` |
| `remove(x)` | Removes first matching value | `a.remove(5)` |
| `pop(i)` | Removes and returns an item | `a.pop(0)` |
| `clear()` | Empties the list | `a.clear()` |
| `index(x)` | Returns first matching index | `a.index(5)` |
| `count(x)` | Counts occurrences | `a.count(5)` |
| `sort()` | Sorts the list in place | `a.sort()` |
| `reverse()` | Reverses in place | `a.reverse()` |
| `copy()` | Makes a shallow copy | `b = a.copy()` |

### `sort()` vs `sorted()`

```python
numbers = [40, 10, 30, 20]

numbers.sort()
print(numbers)  # [10, 20, 30, 40]

numbers = [40, 10, 30, 20]
new_list = sorted(numbers)

print(new_list)  # [10, 20, 30, 40]
print(numbers)   # Original list is unchanged
```

- `list.sort()` changes the original list and returns `None`.
- `sorted(iterable)` returns a new sorted list.

### Descending order

```python
numbers = [10, 50, 20, 40]
numbers.sort(reverse=True)
print(numbers)  # [50, 40, 20, 10]
```

---

# 🧰 5. List operations and useful built-ins

```python
a = [10, 20, 30]
b = [40, 50]

print(a + b)       # Concatenation: [10, 20, 30, 40, 50]
print(a * 2)       # Repetition
print(20 in a)     # Membership: True
print(99 not in a) # Membership: True
```

Useful built-in functions:

| Function | Purpose | Example |
|---|---|---|
| `len(a)` | Number of elements | `len([1, 2, 3])` → `3` |
| `max(a)` | Largest element | `max([2, 8, 4])` → `8` |
| `min(a)` | Smallest element | `min([2, 8, 4])` → `2` |
| `sum(a)` | Sum of numeric elements | `sum([2, 3])` → `5` |
| `sorted(a)` | Returns sorted list | `sorted([3, 1])` → `[1, 3]` |
| `any(a)` | True if any item is truthy | `any([0, 1])` → `True` |
| `all(a)` | True if every item is truthy | `all([1, 2])` → `True` |
| `list(x)` | Converts iterable to list | `list("abc")` → `['a','b','c']` |

## 5.1 List comprehension

A list comprehension creates a new list in a compact way.

```python
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

print(squares)  # [1, 4, 9, 16, 25]
print(evens)    # [2, 4]
```

Equivalent loop:

```python
squares = []

for x in numbers:
    squares.append(x * x)
```

## 5.2 Copying a list

```python
a = [10, 20, 30]

b = a          # Both names refer to the same list
c = a.copy()   # A separate shallow copy
d = a[:]       # Another shallow-copy technique

b[0] = 99
print(a)  # [99, 20, 30]

c[1] = 88
print(a)  # [99, 20, 30]
```

For nested lists, `.copy()` is shallow: inner lists are still shared. Use `copy.deepcopy()` when a fully independent nested copy is required.

---

# 🔒 6. Python Tuples

## 6.1 What is a tuple?

A **tuple** is an ordered and immutable collection.

- **Ordered:** items have positions.
- **Immutable:** after creation, items cannot be added, removed or replaced.
- **Duplicates allowed.**
- **Mixed data types allowed.**

```python
numbers = (10, 20, 30, 40)
names = ("Ravi", "Priya", "Arun")
mixed = (10, "Python", 3.5, True)

print(numbers)
print(names)
print(mixed)
```

## 6.2 Creating tuples

```python
empty = ()

numbers = (10, 20, 30)

# Parentheses are optional, but commonly used
another = 10, 20, 30

# One-item tuple needs a comma
single = (10,)

# Without the comma, this is an integer
not_a_tuple = (10)

from_list = tuple([1, 2, 3])
from_string = tuple("CAT")

print(type(single))      # <class 'tuple'>
print(type(not_a_tuple)) # <class 'int'>
```

## 6.3 Accessing tuple elements

Tuples support indexing, negative indexing, slicing and iteration just like lists.

```python
data = ("Python", "Java", "C", "JavaScript")

print(data[0])    # Python
print(data[-1])   # JavaScript
print(data[1:3])  # ('Java', 'C')

for language in data:
    print(language)
```

## 6.4 Tuple methods

Tuples have two main methods:

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))  # 3
print(numbers.index(20))  # 1
```

## 6.5 Why use tuples?

Use a tuple when a group of values should stay fixed, such as:

```python
# Coordinates
point = (10, 20)

# RGB color
color = (255, 100, 50)

# Fixed date
date = (13, 11, 2026)
```

⚠️ A tuple cannot be modified, but it can contain a mutable object such as a list. That inner list may still be changed.

```python
data = (10, [20, 30])
data[1].append(40)

print(data)  # (10, [20, 30, 40])
```

---

# 📦 7. Tuple packing and unpacking

## 7.1 Packing

Putting multiple values into one tuple is called **packing**.

```python
student = "Raghuram", 18, "CSIT"
print(student)
```

## 7.2 Unpacking

Assigning tuple values to separate variables is called **unpacking**.

```python
student = ("Raghuram", 18, "CSIT")

name, age, branch = student

print(name)
print(age)
print(branch)
```

The number of variables must match the number of tuple items unless extended unpacking is used.

## 7.3 Extended unpacking

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

## 7.4 Swapping variables

Python can swap two variables using tuple unpacking.

```python
a = 10
b = 20

a, b = b, a

print(a)  # 20
print(b)  # 10
```

---

# 🧩 8. Python Sets

## 8.1 What is a set?

A **set** is a collection of unique elements. Sets do not support indexing or slicing.

- **Unique:** duplicate values are removed.
- **Unordered:** do not depend on a fixed position.
- **Mutable:** elements can be added or removed.
- Set elements must be hashable (for example, integers, strings and tuples containing hashable values).

```python
numbers = {10, 20, 30, 20, 10}
print(numbers)  # {10, 20, 30} (display order may vary)
```

## 8.2 Creating sets

```python
numbers = {10, 20, 30}

# Empty set: use set(), not {}
empty = set()

# Convert a list to a set
unique_numbers = set([10, 20, 10, 30])

# Convert a string to a set of unique characters
letters = set("banana")

print(empty)
print(unique_numbers)
print(letters)
```

Important:

```python
empty_dictionary = {}
empty_set = set()

print(type(empty_dictionary))  # dict
print(type(empty_set))         # set
```

## 8.3 Adding elements

```python
numbers = {10, 20}

numbers.add(30)          # Adds one element
numbers.update([40, 50]) # Adds multiple elements

print(numbers)
```

## 8.4 Removing elements

```python
numbers = {10, 20, 30, 40}

numbers.remove(20)  # Error if 20 is absent
numbers.discard(99) # No error if 99 is absent

value = numbers.pop()  # Removes and returns an arbitrary element
print("Removed:", value)

numbers.clear()  # Removes all elements
```

| Method | Behaviour |
|---|---|
| `add(x)` | Adds one element |
| `update(iterable)` | Adds multiple elements |
| `remove(x)` | Removes `x`; raises `KeyError` if absent |
| `discard(x)` | Removes `x` if present; otherwise does nothing |
| `pop()` | Removes and returns an arbitrary element |
| `clear()` | Removes all elements |

## 8.5 Membership checking

```python
languages = {"Python", "Java", "C"}

print("Python" in languages)         # True
print("JavaScript" not in languages) # True
```

Sets are especially useful for membership checks and removing duplicates.

---

# 🔗 9. Set operations

Suppose:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

## 9.1 Union

Union combines all unique elements from both sets.

```python
print(A | B)
print(A.union(B))

# {1, 2, 3, 4, 5, 6}
```

## 9.2 Intersection

Intersection returns elements common to both sets.

```python
print(A & B)
print(A.intersection(B))

# {3, 4}
```

## 9.3 Difference

Difference returns elements present in the first set but not in the second.

```python
print(A - B)  # {1, 2}
print(B - A)  # {5, 6}
```

## 9.4 Symmetric difference

Returns elements that are in either set, but not in both.

```python
print(A ^ B)
print(A.symmetric_difference(B))

# {1, 2, 5, 6}
```

## 9.5 Subset and superset

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))   # True
print(B.issuperset(A)) # True
```

## 9.6 Disjoint sets

Two sets are disjoint when they have no common elements.

```python
A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))  # True
```

## 9.7 Set operation reference

| Operation | Symbol | Method |
|---|---|---|
| Union | `A \| B` | `A.union(B)` |
| Intersection | `A & B` | `A.intersection(B)` |
| Difference | `A - B` | `A.difference(B)` |
| Symmetric difference | `A ^ B` | `A.symmetric_difference(B)` |
| Subset | `A <= B` | `A.issubset(B)` |
| Superset | `A >= B` | `A.issuperset(B)` |
| Disjoint | — | `A.isdisjoint(B)` |

---

# ⚖️ 10. List vs Tuple vs Set

| Feature | List | Tuple | Set |
|---|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
| Ordered | Yes | Yes | No guaranteed positional order |
| Mutable | Yes | No | Yes |
| Duplicates | Allowed | Allowed | Not allowed |
| Indexing | Yes | Yes | No |
| Slicing | Yes | Yes | No |
| Add items | Yes | No | Yes |
| Remove items | Yes | No | Yes |
| Main use | Changeable sequence | Fixed sequence | Unique values and set logic |

### Which one should you choose?

| Requirement | Best choice | Reason |
|---|---|---|
| Store marks that may change | List | Items can be updated |
| Store fixed coordinates | Tuple | Values should stay fixed |
| Remove duplicates | Set | Only unique elements remain |
| Preserve insertion order and remove duplicates | List + membership set | List stores order; set tracks seen values |
| Find common values | Set | Use intersection |
| Access item by position | List or tuple | Both support indexing |

---

# 🧠 11. Problem-solving patterns

These patterns are useful in many collection problems.

## 11.1 Find largest and smallest without built-ins

**Logic:** Assume the first element is both the largest and smallest. Compare every remaining element and update the values.

```python
numbers = [12, 5, 30, 8, 20]

largest = numbers[0]
smallest = numbers[0]

for value in numbers:
    if value > largest:
        largest = value

    if value < smallest:
        smallest = value

print("Largest:", largest)
print("Smallest:", smallest)
```

## 11.2 Remove duplicates while preserving order

**Logic:** Visit each item from left to right. Add it to the result only if it has not appeared before.

```python
numbers = [10, 20, 10, 30, 20, 40]

result = []

for value in numbers:
    if value not in result:
        result.append(value)

print(result)  # [10, 20, 30, 40]
```

For larger inputs, use a set to track seen values while keeping a list for output order:

```python
numbers = [10, 20, 10, 30, 20, 40]

seen = set()
result = []

for value in numbers:
    if value not in seen:
        seen.add(value)
        result.append(value)

print(result)
```

## 11.3 Count occurrences

```python
numbers = [10, 20, 10, 30, 10, 20]
target = 10

count = 0

for value in numbers:
    if value == target:
        count += 1

print(count)  # 3
```

Or use `numbers.count(target)`.

## 11.4 Linear search

**Logic:** Check each item from the beginning. If it matches the target, return its index. If the loop finishes, the target is absent.

```python
numbers = [10, 20, 30, 40]
target = 30

position = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        position = i
        break

print(position)  # 2
```

## 11.5 Binary search

**Important:** Binary search requires a sorted list.

**Logic:** Check the middle element. If it is smaller than the target, search the right half. If it is larger, search the left half.

```python
numbers = [10, 20, 30, 40, 50, 60]
target = 40

left = 0
right = len(numbers) - 1
position = -1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        position = mid
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(position)  # 3
```

## 11.6 Rotate a list left by K

For `[1, 2, 3, 4, 5]` and `K = 2`, the result is `[3, 4, 5, 1, 2]`.

```python
numbers = [1, 2, 3, 4, 5]
k = 2

if numbers:
    k = k % len(numbers)
    result = numbers[k:] + numbers[:k]
else:
    result = []

print(result)
```

## 11.7 Rotate a list right by K

For `[1, 2, 3, 4, 5]` and `K = 2`, the result is `[4, 5, 1, 2, 3]`.

```python
numbers = [1, 2, 3, 4, 5]
k = 2

if numbers:
    k = k % len(numbers)
    result = numbers[-k:] + numbers[:-k] if k else numbers[:]
else:
    result = []

print(result)
```

## 11.8 Move zeros to the end

**Logic:** First collect non-zero values in their original order. Then add enough zeros to reach the original length.

```python
numbers = [0, 1, 0, 3, 12]

result = []

for value in numbers:
    if value != 0:
        result.append(value)

zero_count = len(numbers) - len(result)
result.extend([0] * zero_count)

print(result)  # [1, 3, 12, 0, 0]
```

## 11.9 Find common elements

```python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = list(set(a) & set(b))
print(common)
```

If you need to preserve the order from the first list:

```python
common = []

for value in a:
    if value in b and value not in common:
        common.append(value)

print(common)  # [3, 4]
```

## 11.10 Matrix representation

A matrix can be stored as a nested list: each inner list represents one row.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])  # 2
```

Matrix addition requires the two matrices to have the same dimensions.

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print(result)  # [[6, 8], [10, 12]]
```

---

# ⚠️ 12. Common mistakes

| Mistake | Why it is wrong | Correct approach |
|---|---|---|
| `a = (5)` for a one-item tuple | This is an integer | Use `a = (5,)` |
| `s = {}` for an empty set | This creates a dictionary | Use `s = set()` |
| `a[0]` on a set | Sets do not support indexing | Use a loop or convert to a list if order is not important |
| `a.sort()` assigned to a variable | `sort()` returns `None` | Use `a.sort()` separately or `sorted(a)` |
| Modifying a tuple item | Tuples are immutable | Create a new tuple |
| Assuming set display order | Sets have no positional order | Do not rely on printed order |
| Binary search on unsorted data | Binary search needs sorted data | Sort first if changing order is allowed |
| Dividing by list length without checking | Empty list causes division/modulo errors | Check `if len(a) > 0` |
| Using `remove()` for a missing value | It raises `ValueError` | Check membership first or use another approach |

## ⏱️ Quick complexity reference

Typical average-case time complexities:

| Operation | List | Tuple | Set |
|---|---:|---:|---:|
| Access by index | O(1) | O(1) | Not supported |
| Search by value | O(n) | O(n) | O(1) average |
| Append / add | O(1) amortized | Not supported | O(1) average |
| Insert at beginning | O(n) | Not supported | Not applicable |
| Remove by value | O(n) | Not supported | O(1) average |
| Membership (`in`) | O(n) | O(n) | O(1) average |

*These are typical complexities; exact performance depends on the operation and data.*

---

# 🧪 13. Practice questions 76–99

Solve these in order. First write the **logic and algorithm**, then write the Python code, test it with sample inputs, and check edge cases.

**Suggested status values:** `Not Started`, `Working`, `Completed`.

| No. | Problem | Difficulty | Topic | Status |
|---:|---|---|---|---|
| 76 | Insert at a position | Easy | Lists | Not Started |
| 77 | Largest and smallest list elements | Easy | Lists | Not Started |
| 78 | Second-largest distinct element | Easy | Lists | Not Started |
| 79 | Count occurrences | Easy | Lists | Not Started |
| 80 | Reverse without `reverse()` | Easy | Lists | Not Started |
| 81 | Remove duplicates preserving order | Easy | Lists | Not Started |
| 82 | Common elements of two lists | Easy | Lists | Not Started |
| 83 | Union and intersection of lists | Easy | Lists / Sets | Not Started |
| 84 | Rotate list left by K | Easy | Lists | Not Started |
| 85 | Rotate list right by K | Easy | Lists | Not Started |
| 86 | Move zeros to the end | Easy | Lists | Not Started |
| 87 | Separate even and odd numbers | Easy | Lists | Not Started |
| 88 | Find missing number in a sequence | Easy | Lists | Not Started |
| 89 | Find duplicate and unique elements | Easy | Lists / Sets | Not Started |
| 90 | Linear search | Easy | Lists | Not Started |
| 91 | Binary search | Easy | Lists | Not Started |
| 92 | Flatten a nested list one level | Easy | Lists | Not Started |
| 93 | Add two matrices | Easy | Lists / Matrices | Not Started |
| 94 | Multiply two matrices | Easy | Lists / Matrices | Not Started |
| 95 | Transpose a matrix | Easy | Lists / Matrices | Not Started |
| 96 | Main and secondary diagonal sums | Easy | Lists / Matrices | Not Started |
| 97 | Tuple packing and unpacking | Easy | Tuples | Not Started |
| 98 | Set union, intersection and difference | Easy | Sets | Not Started |
| 99 | Check subset and disjoint sets | Easy | Sets | Not Started |

## 🎯 Practice rules

For every question:

1. 🧠 Understand the problem statement.
2. ✍️ Write the logic in simple English.
3. 🪜 Write the algorithm step by step.
4. 💻 Implement the solution in Python.
5. 🔍 Dry-run the code with a small example.
6. 🧪 Test normal, empty, single-element and duplicate-value cases where relevant.
7. ✅ Update the status in your tracker.

---

# 🚀 14. Final revision checklist

- [ ] I can create a list and take list input.
- [ ] I understand positive and negative indexing.
- [ ] I can use slicing to access and reverse elements.
- [ ] I know the difference between `append()`, `extend()` and `insert()`.
- [ ] I know the difference between `remove()`, `pop()` and `del`.
- [ ] I can sort a list using `sort()` and `sorted()`.
- [ ] I understand list mutability and copying.
- [ ] I can create and access tuples.
- [ ] I understand why a one-element tuple needs a comma.
- [ ] I can pack and unpack tuples.
- [ ] I can create a set and remove duplicates.
- [ ] I can perform union, intersection and difference.
- [ ] I understand subset, superset and disjoint sets.
- [ ] I know when to use a list, tuple or set.
- [ ] I have attempted all 24 practice questions.

## 💡 Pro tips

- Start with loops before using shortcuts. This helps you understand the logic.
- Learn built-in methods after you understand how the operation works.
- For duplicate-removal problems, decide whether the output must preserve order.
- For rotation problems, remember `K % len(list)` and handle an empty list.
- For binary search, confirm that the input is sorted.
- For matrix problems, draw rows and columns before coding.
- Do not memorise code blindly. Understand why every line is needed.

---

⭐ **Keep practising!** Strong knowledge of lists, tuples and sets will help you solve array problems, DSA questions, data-processing tasks and real Python projects.
