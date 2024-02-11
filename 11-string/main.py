# What is String?

# A string in Python is a sequence of characters. Strings are immutable, meaning they cannot be changed after they are created.
# Strings can be enclosed in single quotes ('...') or double quotes ("...") with the same result. \ can be used to escape quotes.

# Examples of string definitions:
# my_string = "Hello, \ World!"
# single_quoted_string = 'This is a single quoted s string.'
# double_quoted_string = "This is a double quoted string."
# escaped_quotes_string = "He said, \"Python is awesome!\""
# multi_line_string = '''This is a multi-line string.
# It can span multiple lines.
# '''

# # Strings can also be created with the str class:
# empty_string = str()
# converted_string = str(123)  # Converts an integer to a string

# # Printing strings
# print(my_string)  # Output: Hello, World!
# print(single_quoted_string)  # Output: This is a single quoted string.
# print(double_quoted_string)  # Output: This is a double quoted string.
# print(escaped_quotes_string)  # Output: He said, "Python is awesome!"
# print(multi_line_string)  # Output: This is a multi-line string...


# i = 1
# for method in dir(str):
#     if '__' not in method:
#         print(i, method)
#         i += 1

s5 = str(5)

# Basic questions on string in Python

# 1. What are strings in Python?
#    Answer: Strings in Python are sequences of characters enclosed in quotes. They are immutable.

# 2. How can you create a multi-line string in Python?
#    Answer: You can create a multi-line string using triple quotes (''' or """).

# 3. Can you give an example of string concatenation?
#    Answer: Yes, for example: "Hello, " + "world!" results in "Hello, world!".

# 4. How do you access the character at index 3 in a string?
#    Answer: You can access it using square brackets: string[3].

# 5. What is the result of slicing a string with [1:4]?
#    Answer: It will return the substring from index 1 to 3, excluding index 4.

# 6. How can you convert a number to a string in Python?
#    Answer: You can convert a number to a string using the str() function, like str(123).

# 7. What is string interpolation and how can it be done in Python?
#    Answer: String interpolation is a method to insert values into a string. 
#            It can be done using the format() method or f-strings 
#            (e.g., f"Value: {value}").
# 8. How do you check if a string contains a particular substring?
#    Answer: You can use the in operator, like "sub" in "substring".

# 9. What is the purpose of the str.strip() method?
#    Answer: The str.strip() method is used to remove leading and trailing whitespace from a string.

# 10. How do you replace parts of a string with another string?
#     Answer: You can use the str.replace() method, like "Hello World".replace("World", "Python").

# 11. How can you iterate over each character in a string?
#     Answer: You can use a for loop: for char in string: print(char)

# 12. What method is used to convert a string to uppercase?
#     Answer: The str.upper() method is used to convert a string to uppercase, like "hello".upper()

# 13. How do you find the length of a string?
#     Answer: You can find the length of a string using the len() function, like len("hello").

# 14. What is the difference between str.find() and str.index()?
#     Answer: The str.find() method returns the lowest index of the substring if it is found, or -1 if it is not. The str.index() method is similar, but raises a ValueError if the substring is not found.

# 15. How can you check if a string starts with a specific substring?
#     Answer: You can use the str.startswith() method, like "hello".startswith("he").







# reverce a string





s = "Hello"  # length is 5
# for loop 

# def reverse(s):
#     rs = ""

#     for i in range(len(s)-1, -1, -1):
#         rs = rs + s[i]

#     print(rs)

# reverse(s)


# using recursion

s = "Hello"

def rec_reverse(s):
    if s == '':
        return s
    return  rec_reverse(s[1:])  + s[0]

print(rec_reverse(s))

'''

1. rec_reverse(s = 'hello')  exclude o
2. rec_reverse(s='hell') exlude l
3. rec_reverse(s = 'hel') eclude l
4. rec_reverse(s = 'he') exlude e
5. rec_reverse(s = 'h') exlude h
6. rec_reverse(s = '' ) return 



'''



s = 2 + 3 + 6 +3 + 6 # 


jan = 24
feb = 12


print(s+jan+feb)