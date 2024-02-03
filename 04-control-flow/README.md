<!-- control flow in python  -->

<!-- if else and elif and loops -> for and while -->


# Conditional Statements in Python

Conditional statements allow you to control the flow of your program based on certain conditions. In Python, you can use `if`, `else`, and `elif` statements to implement conditional logic.

## 1. `if` Statement

The `if` statement is used to execute a block of code only if a specified condition is true.

```python
if condition:
    # Code to be executed if the condition is true

```

## 2. `else` Statement

The `else` statement is used to execute a block of code only if the condition is not true.

```python
if condition:
    # Code to be executed if the condition is true
else:
    # Code to be executed if the condition is false

```


## 3. `elif` Statement

The `elif` statement is used to execute a block of code if the previous conditions were not true.

```python
if condition:
    # Code to be executed if the condition is true
elif condition:
    # Code to be executed if the condition is true
else:
    # Code to be executed if all conditions are false

```

## Ternary Operator

The ternary operator is a shorthand way of writing an if-else statement. It allows you to write a single line if-else statement.


```python
condition_if_true if condition else condition_if_false
```



## 4. `for` Loop

The `for` loop is used to iterate over a sequence (such as a list or a string) and execute a block of code for each element.

```python
for item in sequence:
    # Code to be executed for each element in the sequence
```

## 5. `while` Loop

The `while` loop is used to execute a block of code while a specified condition is true.

```python
while condition:
    # Code to be executed while the condition is true
```


## 6. `break` Statement

The `break` statement is used to exit a loop immediately when a specified condition is met.

```python
while condition:
    # Code to be executed while the condition is true
    if condition:
        break
    # Code to be executed if the condition is false
```

## 7. `continue` Statement

The `continue` statement is used to skip the rest of the current iteration of a loop when a specified condition is met.

```python
while condition:
    # Code to be executed while the condition is true
    if condition:
        continue
    # Code to be executed if the condition is false
```




## 8. `pass` Statement

The `pass` statement is used to create a placeholder for future code.

```python
while condition:
    # Code to be executed while the condition is true
    if condition:
        pass
    # Code to be executed if the condition is false
```


## 9. Nesting in Control Flow

Nesting is when you have a block of code inside another block of code.
it can be any block either if else or loops or even functions.


<!-- if else nesting -->

```python
if condition:
    # Code to be executed if the condition is true
    if condition:
        # Code to be executed if the condition is true
    else:
        # Code to be executed if the condition is false
else:
    # Code to be executed if the condition is false
```

<!-- loop nesting -->

```python
while condition:
    # Code to be executed while the condition is true
    while condition:
        # Code to be executed while the condition is true
    else:
        # Code to be executed if the condition is false
else:
    # Code to be executed if the condition is false
```

<!-- for loop nesting -->

```python
for item in sequence:
    # Code to be executed for each element in the sequence
    for item in sequence:
        # Code to be executed for each element in the sequence
    else:
        # Code to be executed if the condition is false
else:
    # Code to be executed if the condition is false
```




