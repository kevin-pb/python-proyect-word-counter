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

# Collections module

This module implements specialized container data types that provide alternatives to Python's general-purpose built-in containers, dict, list, set, and tuple.

[namedtuple()](https://docs.python.org/es/3.13/library/collections.html#collections.namedtuple) Factory function to create subclasses of tuples with named fields

[Deque](https://docs.python.org/es/3.13/library/collections.html#collections.deque) List-like container with quick appends and pops at both ends

[ChainMap](https://docs.python.org/es/3.13/library/collections.html#collections.ChainMap) Dict-like class to create a single view of multiple mappings

[Counter](https://docs.python.org/es/3.13/library/collections.html#collections.Counter) subclass to count hashable objects

[OrderedDict](https://docs.python.org/es/3.13/library/collections.html#collections.OrderedDict) Dict subclass that remembers which order entries were added

[defaultdict](https://docs.python.org/es/3.13/library/collections.html#collections.defaultdict) Dict subclass that calls a factory function to supply missing values

[UserDict](https://docs.python.org/es/3.13/library/collections.html#collections.UserDict) Wrapper around dictionary objects to facilitate dict subclassing

[UserList](https://docs.python.org/es/3.13/library/collections.html#collections.UserDict) Wrapper around list objects to facilitate subclassing a list

[UserString](https://docs.python.org/es/3.13/library/collections.html#collections.UserString) Wrapper around string objects to facilitate string subclassing

Objects ChainMap

A ChainMap class is provided to quickly link a series of mappings together so that they can be treated as a single unit. This is often much faster than creating a new dictionary and running multiple update() calls.

The class can be used to simulate nested scopes and is useful for creating templates.

class collections.ChainMap(*maps)


A ChainMap combines multiple dictionaries or mappings into a single updatable view. If no mappings are specified, an empty dictionary is created by default.

- Lookups: Traverse dictionaries in order until the key is found.

- Writes, updates, and deletes: Affect only the first dictionary.

- Direct reference: Changes to underlying dictionaries are automatically reflected in the ChainMap.

Main features:

- maps: Public, editable list of underlying dictionaries, ordered by lookup priority. Always contains at least one dictionary.

- Dictionary methods: Supports the usual dictionary methods.

- Flexibility: Allows you to create subcontexts or exclude the first dictionary when accessing other mappings.