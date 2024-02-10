<!-- Python String Notes in Detail -->


## What is a String?

A string is a sequence of characters. It can be created using single or double quotes. Strings are immutable in Python. They cannot be changed once created.

```python
my_string = "Hello, World!"
```

### Types of Strings

- Single-quoted
- Double-quoted
- Triple-quoted
- Raw strings
- Format strings



* Single-quoted


```python
my_string = 'Hello, World!'
```


* Double-quoted

```python
my_string = "Hello, World!"
```


* Triple-quoted

Triple-quoted strings are used to create strings that contain multiple lines of text. They are enclosed in triple quotes.

```python
my_string = '''Hello, World!'''
```


* Raw strings

Raw strings are used to prevent special characters from being interpreted as formatting codes.

```python
my_string = r'Hello, World!'
```


* Format strings

Format strings are used to insert values into strings. They are enclosed in curly braces and contain placeholders for values.

```python
my_string = f'Hello, {name}!'
```




## String Slicing

String slicing is the process of extracting a substring from a string. It is done using the syntax `string[start:stop:step]`.


```python
my_string = "Hello, World!"
substring = my_string[0:5]
print(substring)
```


## String Methods

String methods are functions that are used to manipulate strings. They are used to perform various operations on strings.

* some most common string methods

0. format() -> formats a string with specified values `string.format(value1, value2, value3)`
1. upper()  -> converts the string to uppercase `string.upper()`
2. lower() -> converts the string to lowercase `string.lower()`
3. capitalize() -> converts the first character of the string to uppercase `string.capitalize()`
4. title() -> converts the first character of each word to uppercase `string.title()`
5. swapcase() -> converts the string to uppercase if it is lowercase and vice versa `string.swapcase()`
6. count() -> counts the number of occurrences of a substring in the string `string.count(substring)`
7. find() -> returns the index of the first occurrence of a substring if it is found else returns -1 `string.find(substring)`
8. index() -> returns the index of the first occurrence of a substring if it is found else raises an error `string.index(substring)`
9. rfind() -> returns the index of the last occurrence of a substring if it is found else returns -1 `string.rfind(substring)`
10. rindex() -> returns the index of the last occurrence of a substring if it is found else raises an error `string.rindex(substring)`
11. startswith() -> returns True if the string starts with the specified substring `string.startswith(substring)`
12. endswith() -> returns True if the string ends with the specified substring `string.endswith(substring)`
13. strip() -> removes all the leading and trailing whitespace from the string `string.strip()`
14. lstrip() -> removes all the leading whitespace from the string `string.lstrip()`
15. rstrip() -> removes all the trailing whitespace from the string `string.rstrip()`
16. replace() -> replaces all occurrences of a substring with another substring `string.replace(substring, new_substring)`
17. split() -> splits the string into a list of substrings `string.split(separator)`
18. join() -> joins the list of substrings into a string `string.join(list_of_substrings)`
19. isalpha() -> returns True if the string contains only alphabetic characters `string.isalpha()`
20. isdigit() -> returns True if the string contains only digits `string.isdigit()`
21. isalnum() -> returns True if the string contains only alphanumeric characters `string.isalnum()`







