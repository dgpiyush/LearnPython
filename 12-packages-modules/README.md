<!-- python modules -->

# What is a Module?

A module is a file containing Python definitions and statements. A module can contain functions, classes, and variables. Modules are imported and used in other Python programs.


# Types of Modules


- Built-in Modules
- User-defined Modules
- Third-party Modules


## 1. Built-in Modules

Built-in modules are pre-defined modules in Python that are available for use.


<!-- some built-in modules -->

List of built-in modules:

- os
- sys
- math
- random
- datetime
- json


## 2. User-defined Modules

A user-defined module is a module that you write by yourself.


## 3. Third-party Modules

Third-party modules are modules that are not pre-defined in Python. You can download and install third-party modules from the Python Package Index (PyPI).
with using `pip`.

pip is a package manager for Python. it is used to install and manage third-party packages.


##  Import Modules


```python
import <module_name>
```


```python
from <module_name> import <function_name>

# eg: 
# single function
from math import pi

# more than one function
from math import sin, cos
```


```python
from <module_name> import *

# eg:

# all functions
from math import *
```


<!-- module name alias -->


```python
import <module_name> as <module_alias>


# eg: 
import math as m
```








<!-- python packages -->

# What is a Package?

A package is a collection of modules that are related to each other. They can contain functions, classes, and variables. 




# __init__.py

This file is used to indicate that the directory containing this file is a package. This file 

When a package is imported, Python looks for a file named __init__.py in the package directory. If it exists, it is imported as a module.
this file is executed first when the package is imported.

Having an __init__.py file in a directory is what signals to Python that the directory should be treated as a package.
Without this file, Python will not recognize the directory as a package, and you won't be able to use relative imports or perform other package-related operations.




  

