# Word counter

# Description

**Word Frequency Counter**

**Description**

Develop a program that counts the frequency of each word in a given text.

**Requirements**

- The program should take a string of text as input.

- It should return a dictionary with words as keys and their frequencies as values.

**Example**

![Example](./rsc/Captura.JPG)

**Libraries and Tools**

Collections module for Counter.

**Topics to Study**

- String methods

- Collections module

- Dictionary data structure

**Methodological Steps**

**Read the text:** Use input() or read from a file.
**Normalize the text:** Convert to lowercase and remove punctuation.
**Split into words:** Use split() to break the text into words.
**Count frequencies:** Use Counter from the collections module.
**Display results:** Print the word frequencies.

**Best Practices**

**Use libraries:** Leverage Counter for simplicity and efficiency.
**Normalize text:** Ensure consistent results by handling case and punctuation.
**Handle large inputs:** Be mindful of memory usage with large texts.

# Project
This project calculate how many times a word is repeted in a word

# Architecture

The "collections" library is imported to use the "counter" method (we will use it later). The user is asked to enter a phrase and it is saved in a variable, the string is converted into a list and the "counter" method is used to check how many times each word is repeated in the passed phrase and the number of times each word is repeated is returned


# Collections module:

1. **namedtuple**

**Description:**
Creates tuple-like classes with named fields, allowing access by name instead of index.

**Example:**

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20
```

2. **deque**

**Description:**
Provides a double-ended queue for efficient appends and pops from both ends.

**Example:**
```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)        # Add to the end
dq.appendleft(0)    # Add to the beginning
print(dq)           # Output: deque([0, 1, 2, 3, 4])

```

3. **Counter**

**Description:**
A specialized dictionary for counting hashable objects.

**Example:**

from collections import Counter

```python
counts = Counter('abracadabra')
print(counts)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

4. **OrderedDict**

**Description:**
A dictionary that maintains insertion order (note: starting with Python 3.7, regular dictionaries also guarantee order).

**Example:**

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)  # Output: OrderedDict([('a', 1), ('b', 2)])
```

5. **defaultdict**

**Description:**
A dictionary that provides default values for non-existent keys.

**Example:**

```python
from collections import defaultdict

dd = defaultdict(int)
dd['a'] += 1
print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1})
```

6. **ChainMap**

**Description:**
Combines multiple dictionaries or mappings, searching through them as a single unit.

**Example:**

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
cm = ChainMap(dict1, dict2)
print(cm['b'])  # Output: 2 (first match found)
```

7. **UserDict, UserList, UserString**

**Description:**
Base classes for creating custom dictionary, list, or string-like objects by inheritance.

**Example:**

```python
from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Only integers are allowed")
        super().__setitem__(key, value)

md = MyDict()
md['a'] = 10  # Works
# md['b'] = 'text'  # Raises ValueError
```

The collections module is especially useful for advanced data structures and optimizing code for specific tasks. Would you like to explore any of these in detail