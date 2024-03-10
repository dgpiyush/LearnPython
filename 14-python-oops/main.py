# class Person:
#     # properties
#     age = None
#     name = None
#     income = 0
#     # methods
#     def speak(self,msg):
#         print("speaking..", msg)
#     def printAge(self):
#         print(self.age)
#     def addInome(self,income):
#         self.income = income


# ansaf =  Person()
# amit  = Person()
# # ansaf.age = 25
# # amit.age = 20
# # print(ansaf.age)
# # # print(amit.age)
# # ansaf.printAge()
# ansaf.speak("hello")
# print(ansaf.income)
# ansaf.addInome(500)
# print(ansaf.income)
# print(amit.income)




# class Shap:
#     height = None
#     width = None
#     def area(self):
#         print("calculate area")
    
#     def parameter(self):
#         print("parameter")
# # overiding
# class Triangle(Shap):
#     pass
#     def area(self):
#         print('calculating traingle area')
#     def print_height_width(self):
#         print(self.height, self.width)
# t1 = Triangle()

# t1.print_height_width('d')

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"My name is {self.name} and age is {self.age}")

# # p1 = Person('john', 29)
# # p1.display()


# class Manager(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)


#     def work(self):
#         print("tention dene ka kam")
# class Developer(Person):
#     def __init__(self, name, age,  role):
#         super().__init__(name, age)
#         self.role =  role
    
#     def work(self):
#         print("tention jhelne ka kam")
    
#     def display(self):
#         print(f"My name is {self.name} and age is {self.age}, my role is {self.role}")
        

# d1 = Developer('john', 29, 'FD')

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def display(self):
#         print(f"My name is {self.__name} and age is {self.__age}")
#     def get_name(self):
#         return self.__name
#     def set_name(self, name):
      
#         print("name can not be numaric")
#         return
    
#     def __add__(self, other):
#         # print(self.__age)
#         # print(other.__age)
#         return self.__age + other.__age

#     def __sub__(self, other):
#         return self.__age - other.__age
    
#     def __eq__(self, other):

#         return self.__age ==  other.__age
    
#     def __str__(self) -> str:
#          return self.__name

# p1 = Person('user name',30)
# p2 = Person('dlf',90)

# p3 = Person('dlf',30)

# print(str(p1))

# print(p1.get_name())
# p1.set_name("9")
# p1.display()

# s = ''
# s.isdigit


# d = 5

# tye







class mylist(list):
    def change(self):
        self[:] = []
    

l = mylist([4,5])

print(l)
l.change()
print(l)


