## Exception Handling in Python

Exception handling in Python is a way to catch and handle errors and exceptions that occur during the execution of a program. Python uses a special form of handling called 'Exception Handling' to deal with such errors.

**Exceptions**: Exceptions are errors or unexpected conditions that occur during the execution of a program. Examples of exceptions include `ZeroDivisionError`, `NameError`, `TypeError`, etc.

```python
try:
    # Some Code that may raise an exception.... 
except:
    # optional block
    # Handling of exception (if required)

else:
    # execute if no exception

finally:
    # Some code .....(always executed)
```


### Types of Exceptions in Python


1. SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
2. TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
3. NameError: This exception is raised when a variable or function name is not found in the current scope.
4. IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
5. KeyError: This exception is raised when a key is not found in a dictionary.
6. ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
7. AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
8. IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
9. ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
10. ModuleNotFoundError: This exception is raised when an import statement fails to find or load a module.



### how to rais an exception in python

```python
raise ValueError("Invalid value")
```


### How to create a custom exception in Python

1. Create a new file named `custom_exception.py` in the same directory as your Python script.
2. Add the following code to the file:
```python
class CustomException(Exception):
    pass
```