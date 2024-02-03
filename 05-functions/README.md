# Functions in Python

Functions are blocks of reusable code that perform a specific task. They help organize and modularize your code, making it more readable and maintainable.

### Types of Functions in Python

- Built-in Functions
- User-defined Functions
- Anonymous Functions

## 1. Function Definition

To define a function in Python, use the `def` keyword, followed by the function name and parameters (if any).

```python
def my_function(parameter1, parameter2):
    # Code to be executed
    return result
```


## 2. Function Call

To call a function, use the function name followed by parentheses.

```python
my_function(parameter1, parameter2)
```



## 3. Parameters & Arguments

Parameters are the variables that are used in the function definition. Arguments are the values that are passed to the function when it is called.


```python
def my_function(parameter1, parameter2):
    print(parameter1, parameter2)
```


## 4. Return Statement

Return statement is used to return a value from a function.


```python
def my_function(parameter1, parameter2):
    return result
```


## 5. Default Parameters

Default parameters are used to set a default value for a parameter if it is not provided when the function is called.

```python
def my_function(parameter1, parameter2=10):
    print(parameter1, parameter2)
```


## 6. Keyword Arguments

Keyword arguments are arguments that are passed to a function in the order they are defined.


```python
def my_function(parameter1, parameter2):
    print(parameter1, parameter2)
```


```python
my_function(parameter2=10, parameter1="Hello")
```


## 7. Variable Scope

a variable is only available from inside the region it is created. This is called as variable scope.

```python
def my_function(parameter1, parameter2):
    local_variable = 10

```



## 8. Docstrings

Docstrings are used to document functions, classes, and modules.

```python
def my_function(parameter1, parameter2):
    """
    Brief description of the function.

    Parameters:
    - parameter: Description of the parameter.

    Returns:
    Description of the return value.

    """
```


## 9. Recursion

A recursive function is a function that calls itself.


```python
def my_function(parameter1, parameter2):
    if condition:
        return result
    else:
        return my_function(parameter1, parameter2)
```

## 10. Lambda Functions / Anonymous Functions

Lambda functions are anonymous functions that can be created without a name. They are used to create short, one-line functions that can be passed as arguments.


```python
lambda parameter1, parameter2: result
```

