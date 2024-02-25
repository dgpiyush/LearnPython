# Data Types in Python

## Data Types

### 1. Numeric Types
- **int**: Whole numbers, positive or negative, without decimals.
- **float**: Numbers containing one or more decimals.
- **complex**: Numbers with a real and imaginary part.

### 2. Sequence Types
- **list**: Ordered, changeable collection with duplicate elements.
- **tuple**: Ordered, immutable collection with duplicate elements.
- **range**: Immutable sequence of numbers.
- **string**: Ordered collection of characters.

### 3. Boolean Types
- **bool**: Represents truth values `True` or `False`.

### 4. Set Types
- **set**: Unordered, mutable collection with no duplicate elements.
- **frozenset**: Immutable variant of a set.

### 5. Mapping Types
- **dictionary**: Unordered, mutable collection of key-value pairs.

### 6. Binary Types
- **bytes**: Immutable sequence of bytes.
- **bytearray**: Mutable sequence of bytes.
- **memoryview**: Memory view into a bytes or bytearray object.

---

## Comparison of Sequence Types
| Type   | Syntax  | Ordered | Mutable | Duplicates | Example            |
|--------|---------|---------|---------|------------|--------------------|
| List   | `[]`    | Yes     | Yes     | Allowed    | `[1, 2, 2, 3]`    |
| Tuple  | `()`    | Yes     | No      | Allowed    | `(1, 2, 2, 3)`     |
| Range  | -       | Yes     | No      | Not applicable | `range(5)`       |
| String | -       | Yes     | No      | Allowed    | `'Hello, World!'` |

## Comparison of Mapping and Set Types
| Type      | Syntax  | Ordered | Mutable | Duplicates | Example                                          |
|-----------|---------|---------|---------|------------|--------------------------------------------------|
| Dictionary| `{}`    | As of Python 3.7, Yes | Yes | No keys, but values can be duplicated | `{'key1': 1, 'key2': 2, 'key3': 3}` |
| Set       | `{}`    | No      | Yes     | Not allowed| `{1, 2, 3}`                                      |

---

### Key Differences
- **Performance**:
  - List and Tuple: Accessing elements is fast. Tuple can be slightly faster than List due to immutability.
  - Dictionary: Optimized for retrieving values when the key is known. Slower for ordered operations.
  - Set: Optimized for membership tests, union, intersection, and difference operations.
- **Use Cases**:
  - List: Ordered, modifiable collections.
  - Tuple: Ordered collections that should not change.
  - Dictionary: Key-value pairs for efficient data retrieval.
  - Set: Collections ensuring unique elements with no specific order.
- **Methods**:
  - List: `append()`, `extend()`, `insert()`, `remove()`, `pop()`
  - Tuple: `count()`, `index()`
  - Dictionary: `keys()`, `values()`, `items()`, `get()`, `update()`
  - Set: `add()`, `remove()`, `discard()`, `pop()`, `union()`, `intersection()`, `difference()`
