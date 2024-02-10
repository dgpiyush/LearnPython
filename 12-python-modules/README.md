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



