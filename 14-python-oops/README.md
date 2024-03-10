# Python OOPS (Object Oriented Programming)

### Definition
- OOPS is a programming paradigm that uses objects, classes, and inheritance to represent and manipulate concepts in a computer program.

### Key Concepts
- **Class**: A blueprint or template for creating objects.
- **Object**: An instance of a class.
- **Inheritance**: The process by which one class acquires the properties and methods of another class.
- **Encapsulation**: The practice of bundling data and methods that operate on that data within one unit or class.
- **Abstraction**: The process of hiding unnecessary details and showing only the required details.
- **Polymorphism**: The ability of an object to take on many forms.



### Class

A class is a blueprint or template for creating objects. It defines the properties and methods that an object of that class will have.

### Syntax

```python
class MyClass:
    pass

class MyClass():
    pass 
```


### Objects in Python

- **Creating an Object**: An object is created by calling a class and assigning the result to a variable.
- **Accessing Attributes**: An attribute of an object can be accessed using dot notation, `object.attribute`.
- **Changing Attributes**: An attribute of an object can be changed by assigning a new value to the attribute.
- **Calling Methods**: A method of an object can be called by invoking it with dot notation, `object.method()`.


### Example

```python
class MyClass:
    pass

my_object = MyClass()
```

#### isinstance()

```python
isinstance(my_object, MyClass)
```



### Constructor

A constructor is a special method of a class that is called automatically whenever an object of the class is created. It is used to initialize objects.

#### Syntax

```python
class MyClass:
    def __init__(self):
        pass
```


### Instance Attributes and Class Attributes

- **Instance Attributes**: Attributes that are unique to each instance of a class. They are not shared among instances. They are created when an object of a class is created.
- **Class Attributes**: Attributes that are shared among all instances of a class. They are created when a class is defined.


#### Syntax

```python
class MyClass:
    class_attribute = 0
    def __init__(self):
        self.instance_attribute = 0
```




### Instance Methods  Class Methods and Static Methods

- **Instance Methods**: Methods that are specific to each instance of a class. They use instance attributes and are unique to each object.
- **Class Methods**: Methods that are shared among all instances of a class. They use class attributes and are common to all objects.

- **Static Methods**: They are methods that do not access any instance attributes or methods. They are not bound to any particular instance of a class, and are called directly on the class. They are used to perform operations that are not related to any instance of a class.


#### Syntax

```python
class MyClass:
    class_attribute = 0
    def __init__(self):
        self.instance_attribute = 0
    def instance_method(self):
        pass
    @classmethod
    def class_method(cls):
        pass
    @staticmethod
    def static_method():
        pass
```




### Magic Methods

Python provides several magic methods that can be used to customize the behavior of a class. These are special methods that are defined by prefixing a double underscore (`__`) to the method name.

Here are some commonly used magic methods:

- `__init__`: Constructor method.
- `__str__`: Method to define string representation of an object.
- `__repr__`: Method to define representation of an object for debugging.
- `__len__`: Method to define length of the object.
- `__getitem__`: Method to define behavior of `[]` (indexing) operator.
- `__setitem__`: Method to define behavior of `[]` (assignment) operator.
- `__delitem__`: Method to define behavior of `del` operator.
- `__iter__`: Method to define behavior of `iter()` function.
- `__next__`: Method to define behavior of `next()` function.
- `__add__`: Method to define behavior of `+` operator.
- `__sub__`: Method to define behavior of `-` operator.
- `__mul__`: Method to define behavior of `*` operator.
- `__truediv__`: Method to define behavior of `/` operator.
- `__floordiv__`: Method to define behavior of `//` operator.
- `__mod__`: Method to define behavior of `%` operator.
- `__pow__`: Method to define behavior of `**` operator.

Note: There are more magic methods available in Python.
Docs : [link](https://rszalski.github.io/magicmethods/)








## Inheritance

Inheritance is the process by which one class acquires the properties and methods of another class.

#### Syntax

```python

class BaseClass:
    # parent class
    pass

class DerivedClass(BaseClass):
    # child class
    pass
```


### Types of Inheritance in Python

Python supports three types of inheritance:

1. **Single Inheritance**: A class can inherit attributes and methods from one single parent class.
2. **Multiple Inheritance**: A class can inherit attributes and methods from multiple parent classes.
3. **Multilevel Inheritance**: A class inherits from another derived class, forming a chain of inheritance.


- **Single Inheritance**:
```python

class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def make_sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def __init__(self, name, weight, breed):
        super().__init__(name, weight)
        self.breed = breed

    def make_sound(self):
        print("Dog says 'Woof'")



dog = Dog("Buddy", 25, "Golden Retriever")
print(dog.name)
print(dog.breed)
dog.make_sound()

```

- **Multiple Inheritance**:
```python

class Engine:
    def start(self):
        print("Engine started")

class ElectricMotor:
    def power(self):
        print("Electric power")

class HybridCar(Engine, ElectricMotor):
    pass

# Example
my_hybrid_car = HybridCar()
my_hybrid_car.start()  # Inherited from Engine class
my_hybrid_car.power()  # Inherited from ElectricMotor class
```

- **Multilevel Inheritance**:
```python
class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class SportsCar(Car):
    def race(self):
        print("Sports car is racing")

# Example
my_sports_car = SportsCar()
my_sports_car.move()  # Inherited from Vehicle class
my_sports_car.drive()  # Inherited from Car class
my_sports_car.race()   # Specific to SportsCar class
```


### object class

The `object` class is the root class of all classes in Python. It is the parent class of all other classes.


### Built-in functions:

- `super()`: Returns a proxy object that allows you to call methods of a parent class from within a child class.


### Important  functions:

- `isinstance()`: Returns `True` if the object is an instance of the given class, `False` otherwise.
- `issubclass()`: Returns `True` if the class is a subclass of the given class, `False` otherwise.



    


## Encapsulation

Encapsulation is like putting data and its actions together in a box (class) and only letting others interact with it in a specific way, hiding how it works inside.

### Access Modifiers : 
    private, protected, and public

#### Syntax
```python
class MyClass:
    def __init__(self):
        self.__private_attribute = 0
        self._protected_attribute = 1
        self.public_attribute = 2

    def public_method(self):
        pass

    def _protected_method(self):
        pass

    def __private_method(self):
        pass
```

#### Example
```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # private attribute
        self.__model = model  # private attribute

    def get_info(self):
        return f"{self.__brand} {self.__model}"

# Example of encapsulation
my_car = Car("Toyota", "Camry")
print(my_car.get_info()) 
```

### Getters and Setters

getters and setters are used to access and modify the private attributes of a class.

#### Syntax
```python
class MyClass:
    def __init__(self):
        self.__private_attribute = 0

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        self.__private_attribute = value
```

#### property method and decorator

```python

# Example of property method
class MyClass:
    def __init__(self):
        self.__private_attribute = 0


    def get_private_attribute(self):
        return self.__private_attribute

   
    def set_private_attribute(self, value):
        self.__private_attribute = value
    
    private_attribute = property(get_private_attribute, set_private_attribute)

# Example of property decorator
class MyClass:
    def __init__(self):
        self.__private_attribute = 0

    @property
    def private_attribute(self):
        return self.__private_attribute

    @private_attribute.setter
    def private_attribute(self, value):
        self.__private_attribute = value
```





## Abstraction

Abstraction is the process of hiding unnecessary details and showing only the required information.

Imagine abstraction like using a TV remote without delving into its internal workings; it enables interaction without the need to comprehend complex intricacies.

- Example:
    ```python
    from abc import ABC, abstractmethod

    # Abstract class representing a TV
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
    class SamsungTV(TV):
        def turn_on(self):
            print("Samsung TV is turning on.")

        def turn_off(self):
            print("Samsung TV is turning off.")

        def change_channel(self, channel):
            print(f"Changing channel to {channel} on Samsung TV.")

    # Concrete implementation of the TV class
    class SonyTV(TV):
        def turn_on(self):
            print("Sony TV is turning on.")

        def turn_off(self):
            print("Sony TV is turning off.")

        def change_channel(self, channel):
            print(f"Changing channel to {channel} on Sony TV.")

    # Example usage of abstraction
    samsung_tv = SamsungTV()
    samsung_tv.turn_on()
    samsung_tv.change_channel(5)
    samsung_tv.turn_off()

    sony_tv = SonyTV()
    sony_tv.turn_on()
    sony_tv.change_channel(8)
    sony_tv.turn_off()
    ```
## Polymorphism
Polymorphism is the ability of an object to take on many forms. In other words, polymorphism means the same thing in different ways.

### Types of Polymorphism

- **Method Overloading:**
  - Involves having two or more methods with the same name but different parameters.
  - Python does not support traditional method overloading, but achieves similar functionality through default arguments and variable-length argument lists.
  
    Example of method overloading in Python:
    ```python
    def add(a, b=0, c=0):
        return a + b + c
    # Example
    add(1, 2)
    add(1, 2, 3)
    ```
- **Method Overriding:**
  - Involves a method in a derived class that has the same name as the method in the base class.
  - Python fully supports method overriding.
  
    Example of method overriding in Python:
    ```python
    class Animal:
        def eat(self):
            print("I can eat")

    class Dog(Animal):
        def eat(self):
            print("I can eat and bark")
    # Example
    my_dog = Dog()
    my_dog.eat()
    ```

### Duck Typing

Duck typing is a concept in programming where the concept of polymorphism is hidden.

"it its walk like a duck and quack like a duck. it is a duck."

- Example of duck typing in Python:
    ```python
    class Animal:
        def walk(self):
            print("I can walk")

    class Dog(Animal):
        def walk(self):
            print("I can walk and bark")
    class Cat(Animal):
        def walk(self):
            print("I can walk and meow")
    # Example

    def walk_animal(animal):
        animal.walk()

        
    my_dog = Dog()
    my_cat = Cat()

    walk_animal(my_dog)
    walk_animal(my_cat)
    ```

