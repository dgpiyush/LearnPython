## Python Set Details

### Overview
- A set is a collection which is unordered, mutable, and does not allow duplicate elements.
- Sets are written with curly braces `{}`.

### Creating a Set
- A set can be created by placing all the items (elements) inside curly braces `{}`, separated by commas.
- Alternatively, the `set()` constructor can be used to create a set.

### Accessing Elements
- As sets are unordered, you cannot access items by index.
- You can loop through the set using a `for` loop to access its elements.

### Adding Elements
- Use the `.add(element)` method to add a single element to a set.
- Use the `.update([element1, element2, ...])` method to add multiple elements to a set.

### Removing Elements
- The `.remove(element)` method removes the specified element from the set but raises a KeyError if the element is not found.
- The `.discard(element)` method removes the specified element from the set without raising an error if the element is not found.
- The `.pop()` method removes and returns an arbitrary element from the set. If the set is empty, a KeyError is raised.
- The `.clear()` method empties the set.


### Operations
- Set union can be performed with `set1 | set2` or `set1.union(set2)`.
- Set intersection can be performed with `set1 & set2` or `set1.intersection(set2)`.
- Set difference can be performed with `set1 - set2` or `set1.difference(set2)`.
- Symmetric difference (elements in either set, but not in both) can be performed with `set1 ^ set2` or `set1.symmetric_difference(set2)`.

### Checking Membership
- To check if an item is in a set, use the `in` keyword.

### Set Comprehension
- Set comprehension is a concise way to create sets. The syntax is `{expression for item in iterable if condition}`.

### Built-in Set Functions
- `len(set)`: Gives the total number of elements in a set.
- `max(set)`: Returns the largest element of the set.
- `min(set)`: Returns the smallest element of the set.
