<!-- Python Data Types -->

# Data Types in Python

## Data Types

* Numaric  -> int, float, complex

* Sequence  -> list, tuple, range, string

* Boolean -> True, False

* Set 

* Dictionary

* Binary -> bytes, bytearray, memoryview




### Numaric Types


<!-- explain int with example  -->


1. int  -> int is a whole number, positive or negative, without decimals, of unlimited length.

```python
x = 10
print(x)  # Output: 10
```

2. float  -> float is a number, positive or negative, containing one or more decimals.

```python
x = 10.5
print(x)  # Output: 10.5
```

3. complex -> complex numbers are written with a lowercase j as the imaginary part.

```python
x = 10 + 5j
print(x)  # Output: (10+5j)
```



### Sequence Types

1. list -> list is a collection which is ordered and changeable. Allows duplicate members.

```python
x = ["apple", "banana", "cherry"]
print(x)  # Output: ['apple', 'banana', 'cherry']
```

2. tuple -> tuple is a collection which is ordered and unchangeable. Allows duplicate members.

```python
x = ("apple", "banana", "cherry")
print(x)  # Output: ('apple', 'banana', 'cherry')
```

3. range -> range is a built-in function that returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

```python
x = range(6)
print(x)  # Output: range(0, 6)
```

4. string -> string is a collection of characters, enclosed in quotes.

```python
x = "Hello, World!"
print(x)  # Output: Hello, World!
```


### Boolean Types


1. Boolean -> Boolean is a data type that can have two possible values: True or False.

```python
x = True
print(x)  # Output: True
```

```python
x = False
print(x)  # Output: False
```




### Set Types

1. set -> set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.

```python
x = {"apple", "banana", "cherry"}
print(x)  # Output: {'apple', 'banana', 'cherry'}
```


### Dictionary Types

1. dictionary -> dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

```python
x = {"name": "John", "age": 30}
print(x)  # Output: {'name': 'John', 'age': 30}
```



### Binary Types

1. bytes -> bytes are arrays of bytes, immutable.

```python
x = b"Hello"
print(x)  # Output: b'Hello'
```

2. bytearray -> bytearray is an array of bytes. It has the same functionality as a list.

```python
x = bytearray(5)
print(x)  # Output: bytearray(b'\x00\x00\x00\x00\x00')
```

3. memoryview -> memoryview is a view into a bytes or bytearray object, and it allows for writing to and reading from it.

```python
x = memoryview(bytes(5))
print(x)  # Output: memoryview(b'\x00\x00\x00\x00\x00')
```

