<!-- python operators and its use -->

# Python Operators and its use

<!-- operator list -->

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators


## Arithmetic operators

- -  ( + ) -> Addition
- -  ( - ) -> Subtraction
- -  ( * ) -> Multiplication
- -  ( / ) -> Division
- -  ( % ) -> Modulus
- -  ( ** ) -> Exponentiation
- -  ( // ) -> Floor division

### Example:

```python
x = 10
y = 5
print(x + y)  # Output: 15
print(x - y)  # Output: 5
print(x * y)  # Output: 50
print(x / y)  # Output: 2.0
print(x % y)  # Output: 0
print(x ** y)  # Output: 1000
print(x // y)  # Output: 2
```

## Assignment operators

- -  ( = ) -> Simple assignment
- -  ( += ) -> Augmented assignment
- -  ( -= ) -> Augmented assignment
- -  ( *= ) -> Augmented assignment
- -  ( /= ) -> Augmented assignment
- -  ( %= ) -> Augmented assignment
- -  ( //= ) -> Augmented assignment
- -  ( **= ) -> Augmented assignment
- -  ( &= ) -> Augmented assignment
- -  ( |= ) -> Augmented assignment
- -  ( ^= ) -> Augmented assignment
- -  ( >>= ) -> Augmented assignment
- -  ( <<= ) -> Augmented assignment


### Example:

```python
x = 10
x += 5
print(x)  # Output: 15
```


## Comparison operators

- -  ( == ) -> Equal to
- -  ( != ) -> Not equal to
- -  ( > ) -> Greater than
- -  ( < ) -> Less than
- -  ( >= ) -> Greater than or equal to
- -  ( <= ) -> Less than or equal to


### Example:

```python
x = 10
y = 5
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)  # Output: True
print(x < y)  # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False
```

## Logical operators

- -  ( and ) -> Logical AND
- -  ( or ) -> Logical OR
- -  ( not ) -> Logical NOT


### Example:

```python
x = True
y = False
print(x and y)  # Output: False
print(x or y)  # Output: True
print(not x)  # Output: False
```

## Identity operators

- -  ( is ) -> Identity
- -  ( is not ) -> Identity


### Example:

```python
x = 10
y = 5
print(x is y)  # Output: False
print(x is not y)  # Output: True
```


## Membership operators

- -  ( in ) -> Membership
- -  ( not in ) -> Membership


### Example:

```python
x = 10
y = 5
print(x in y)  # Output: False
print(x not in y)  # Output: True
```


## Bitwise operators

- -  ( & ) -> Bitwise AND
- -  ( | ) -> Bitwise OR
- -  ( ^ ) -> Bitwise XOR
- -  ( ~ ) -> Bitwise NOT
- -  ( << ) -> Bitwise left shift
- -  ( >> ) -> Bitwise right shift


### Example:

```python
x = 10
y = 5
print(x & y)  # Output: 0
print(x | y)  # Output: 15
print(x ^ y)  # Output: 15
print(~x)  # Output: -11
print(x << y)  # Output: 100
print(x >> y)  # Output: 0
```





# Operator Precedence in Python

Operator precedence defines the order in which operators are applied in an expression. Understanding precedence is crucial for writing accurate and predictable code.

## Precedence Order:


| Precedence | Operators                          | Description                                   |
|------------|------------------------------------|-----------------------------------------------|
| 1          | `()`                               | Parentheses (grouping)                        |
| 2          | `**`                               | Exponentiation                                |
| 3          | `+x`, `-x`, `~x`                   | Unary plus, Unary minus, Bitwise NOT          |
| 4          | `*, /, //, %`                      | Multiplication, Division, Floor division, Modulus |
| 5          | `+, -`                             | Addition, Subtraction                         |
| 6          | `<<, >>`                           | Bitwise shift operators                       |
| 7          | `&`                                | Bitwise AND                                   |
| 8          | `^`                                | Bitwise XOR                                   |
| 9          | `\|`                               | Bitwise OR                                    |
| 10         | `==, !=, >, >=, <, <=, is, is not, in, not in` | Comparisons, Identity, Membership operators |
| 11         | `not`                              | Logical NOT                                   |
| 12         | `and`                              | Logical AND                                   |
| 13         | `or`                               | Logical OR      


## Example of Operator Precedence:


<!-- Example of arithmetic operator precedence -->

```python


#expression one 

expression = (2 + 3) * 4 
print(expression)  # Output: 20

#explain 
## used operators *,+ 
## * have more priority than +  so first * will be executed and then + 
## but we can use parenthesis to change the order of operation, parenthesis have highest priority


#expression two

expression = 2 + 3 * 4 
print(expression)  # Output: 14

#explain 
## used operators *,+ 
## * have more priority than +  so first * will be executed and then +



#expression three

expression = (2 + 3) * 4 - 5 
print(expression)  # Output: 15

#explain 
## used operators *,+,- 
## 2 + 3 is in parenthesis so it will be executed first then * and then - 


# expression four

expression = 2 + (3 * 4) - 5 
print(expression)  # Output: 14

#explain 
## used operators *,+,- 
## 3 * 4 is in parenthesis so it will be executed first then * and then -









```



