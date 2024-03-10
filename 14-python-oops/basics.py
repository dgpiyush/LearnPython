

# # class attributes and instance attributes
# # class Student:
# #     # class attributes
# #     college = "ABC"
# #     def __init__(self, name, age):
# #         # instance attributes
# #         self.name = name
# #         self.age = age
    
# # s = Student('john', 28)
# # s1 = Student('mike', 29)

# # print(s.age, s.college)
# # print(s1.age, s.college)



# # instance method , class method , static method
# # class Student:
# #     # class attributes
# #     college = "ABC"
# #     def __init__(self, name, age):
# #         # instance attributes
# #         self.name = name
# #         self.age = age
# #     # instance method
# #     def getName(self):
# #         return self.name
# #     @classmethod
# #     def getCollege(cls):
# #         print(cls.college)
# #     @staticmethod
# #     def sayHello():
# #         print("hello")
    

# #     def __eq__(self, other):

# #         if self.name == other.name and self.age == other.age:
# #             return True
# #         else:
# #             return False

    



# # s1 = Student('john', 28)
# # s2 = Student('john', 29)



# # print(s1 != s2)

# # print(s.getName())
# # s.getCollege()
# # Student.getCollege()
# # Student.sayHello()




# class A:
#     a = 5
#     def display(self):
#         print("in A class")

# class B(A):
#     b = 10
#     def display(self):
#         print("in B class")

# class C(B): # order matters
#     # def display(self):
#     #     print("in C class")
#     pass


# obj = C()


# class Pet:
#     pass


# # print(dir(object))


# # print(isinstance(obj, B))

# # print(issubclass(B, object))




# # encapsolutions


# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self._age = age

#     @property
#     def name(self):
#         print("getting the name")
#         return self.__name
    

#     @name.setter
#     def name(self, name):
#         print('setting the name')
#         self.__name = name
    

# s = Student('john', 28)


# s.name = 'mike'
# print(s.name)








# # print(s.get_name())




# inheritance
# encapsulations
# abstractions
# polymorphism


from abc import ABC, abstractmethod


class TV(ABC):
        @abstractmethod
        def turn_on(self):
            pass

        @abstractmethod
        def turn_off(self):
            pass

        @abstractmethod
        def change_channel(self, channel):
            pass

# Concrete implementation of the TV class
# class SamsungTV(TV):
#     def turn_on(self):
#         print("Samsung TV is turning on.")

#     def turn_off(self):
#         print("Samsung TV is turning off.")

#     def change_channel(self, channel):
#         print(f"Changing channel to {channel} on Samsung TV.")

# # Concrete implementation of the TV class
        

# class SonyTV():
#     def turn_on(self):
#         print("Sony TV is turning on.")

#     def turn_off(self):
#         print("Sony TV is turning off.")

#     def change_channel(self, channel):
#         print(f"Changing channel to {channel} on Sony TV.")


# class MiTV(TV):
    
#     def turn_on(self):
#         print("Mi TV is turning on.")
    
#     def turn_off(self):
#         print("Mi TV is turning off.")






# tvobj = MiTV()
# tvobj.turn_on()



# polymorphism
        
        # compile time (overloading) X
        # runtime (overriding) 

class Animal:
        def eat(self):
            print("I can eat")

class Dog(Animal):
    def eat(self):
        print("I can eat and bark")

class Cat(Animal):
    def eat(self):
        print("I can eat and meow")

def animal_eat(animal):
    animal.eat()

# Example
# my_dog = Dog()
# my_cat = Cat()

# animal_eat(my_dog)
# animal_eat(my_cat)





# def demo(a,b=0):
#      print(a,b)




# demo(3,5)

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary


# class Developer(Employee):
#     def __init__(self, name, age, salary, language):
#         super().__init__(name, age, salary)
#         self.language = language



# d1 = Developer('john', 29, 1000, 'python')


# print(isinstance(d1, Developer))