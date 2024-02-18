# creating a list


fruits = ["apple", "apple", "banana", "cherry"]


# append  -> takes value as parameter and insert it at the end
# fruits.append('mango') 

# insert -> takes index and value as parameter and insert it at that index
# print(fruits)

# fruits.insert(0, 'pineapple')

# print(fruits)


# pop -> takes index as parameter and removes the element at that index
# print(fruits)
# print(fruits.pop(3))
# print(fruits)

# remove ->  remove the first occurence of the value and if value is not present then it will raise an error
# print(fruits)
# fruits.remove('app')
# print(fruits)

# index -> returns the index of the first occurence of the value
# print(fruits.index('apple'))


# list slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# positive slicing
# print(numbers[0:6])
# print(numbers[::-1])

# list comprehansion 

# duplicat_numbers = [v*v for v in ]

# print(duplicat_numbers)

# for  v in numbers:
    
#     duplicat_numbers.append(v+v)

# print(duplicat_numbers)



# even_list = [num for num in range(1,11)]

# # print((even_list))

# # for num in range(1,11):
# #     if num%2 == 0:
# #         even_list.append(num)

# print(even_list)







# Basic questions on list comprehension in Python

# 1. What is list comprehension in Python?
#    Answer: List comprehension is a concise way to create lists in Python. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

# 2. How do you square every number in a list using list comprehension?
#    Example: squares = [x**2 for x in range(10)]

# 3. How can list comprehension be used to filter items in a list?
#    Example: evens = [x for x in range(20) if x % 2 == 0]

# 4. Can list comprehensions replace nested loops?
#    Answer: Yes, list comprehensions can replace nested loops to create a flattened list.
#    Example: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#             flattened = [num for row in matrix for num in row]

# 5. What is the syntax to add an else clause in a list comprehension?
#    Example: [x if x > 0 else -x for x in range(-5, 5)]
