<div align=center>
<h1><img src="https://img.icons8.com/fluency/30/000000/python.png"/> PYTHON</h1> </div>

Python is a High level, Object Oriented Dynamically typed and Interpreted Programming  and Scripting Language. It is a general purpose programming language and is used for a wide variety of applications like Web Development, Data Science, Machine Learning, Artificial Intelligence, etc.

<br>

> Dynamic Typing: In Python, we don't need to declare the type of the variable. The type of the variable is determined at runtime.

> Interpreted Language: Python is an interpreted language. It means that the code is not compiled into machine language. Instead, it is converted into bytecode and then interpreted by the Python Virtual Machine (PVM).

> Object Oriented: Python is an Object Oriented Programming Language. It supports Object Oriented Programming features like Inheritance, Encapsulation, Polymorphism, etc.

<br>

## Table of Contents
- variables
- data types
- operators
- conditional statements (if-else, switch-case)
- loops (for, while)
- iterators
- Collections (List, Tuple, Set, Dictionary)
- list comprehension
- Strings
- functions
- lambda functions
- classes
- OOPs
- modules
- exceptions
- files
- regular expressions
- decorators
- generators
- map, filter, reduce
- multithreading
- multiprocessing
- socket programming
- web scraping
- web development
- database
- GUI
- data science
- machine learning
- artificial intelligence
- cryptography
- image processing
- game development
- web automation


<br>

## Variables
Variables are used to store data. In Python, we don't need to declare the data type of the variable. The type of the variable is determined at runtime.

>variables are the name given to the memory location where the data is stored.

>syntax: variable_name = value
```python
# variable declaration
a = 10
b = 20
print(a, b) # o/p: 10 20
```

<br>

## Data Types
Python has 5 data types:
- int
- float
- complex
- bool
- str

> int: It is used to store integer values. It is a signed integer. It can store values from -2^31 to 2^31-1.

> float: It is used to store floating point values. It is a signed floating point. It can store values from -2^31 to 2^31-1.

> complex: It is used to store complex numbers. It is a signed complex number. It can store values from -2^31 to 2^31-1.

> bool: It is used to store boolean values. It can store either True or False.

> str: It is used to store string values. It is a sequence of characters.

```python
# int
a = 10
print(type(a)) # o/p: <class 'int'>

# float
a = 10.5
print(type(a)) # o/p: <class 'float'>

# complex
a = 10 + 5j
print(type(a)) # o/p: <class 'complex'>

# bool
a = True
print(type(a)) # o/p: <class 'bool'>

# str
a = "Hello World"
print(type(a)) # o/p: <class 'str'>
```
> Note: In Python, we can use single quotes or double quotes to declare a string.

> type() is a built-in function which is used to get the type of the variable.

<br>

## Operators
Python has 7 types of operators:
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Bitwise Operators
- Assignment Operators
- Identity Operators
- Membership Operators

### Arithmetic Operators
| Operator | Description | Example |
| --- | --- | --- |
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| % | Modulus | a % b |
| // | Floor Division | a // b |
| ** | Exponentiation | a ** b |

> +: It is used to add two numbers. It can also be used to concatenate two strings. It can also be used to concatenate two lists. It can also be used to concatenate two tuples. It can also be used to concatenate two sets. It can also be used to concatenate two dictionaries. It can also be used to concatenate two range objects. It can also be used to concatenate two bytes objects. It can also be used to concatenate two bytearray objects. It can also be used to concatenate two memoryview objects. It can also be used to concatenate two frozenset objects. 

> -: It is used to subtract two numbers. 

> *: It is used to multiply two numbers. It can also be used to repeat a string. It can also be used to repeat a list. It can also be used to repeat a tuple. It can also be used to repeat a set. It can also be used to repeat a dictionary. It can also be used to repeat a range object. It can also be used to repeat a bytes object. It can also be used to repeat a bytearray object. It can also be used to repeat a memoryview object. It can also be used to repeat a frozenset object.

> /: It is used to divide two numbers. It returns a float value.

> %: It is used to get the remainder of two numbers. It returns an int value.

> //: It is used to divide two numbers and returns the floor value. It returns an int value.

> **: It is used to get the power of a number. It returns an int value.

```python

# addition
a = 10
b = 20
print(a + b) # o/p: 30

# subtraction
a = 10
b = 20
print(a - b) # o/p: -10

# multiplication
a = 10
b = 20
print(a * b) # o/p: 200

# division
a = 10
b = 20
print(a / b) # o/p: 0.5

# modulus
a = 10
b = 20
print(a % b) # o/p: 10

# floor division
a = 10
b = 20
print(a // b) # o/p: 0

# exponentiation
a = 10
b = 20
print(a ** b) # o/p: 100000000000000000000

# concatenation
a = "Hello"
b = "World"
print(a + b) # o/p: HelloWorld

# repeat
a = "Hello"
print(a * 3) # o/p: HelloHelloHello
```

### Comparison Operators
| Operator | Description | Example |
| --- | --- | --- |
| == | Equal to | a == b |
| != | Not equal to | a != b |
| > | Greater than | a > b |
| < | Less than | a < b |
| >= | Greater than or equal to | a >= b |
| <= | Less than or equal to | a <= b |

### Logical Operators
| Operator | Description | Example |
| --- | --- | --- |
| and | Returns True if both statements are true | a and b |
| or | Returns True if one of the statements is true | a or b |
| not | Reverse the result, returns False if the result is true | not(a and b) |

### Bitwise Operators
| Operator | Description | Example |
| --- | --- | --- |
| & | AND | a & b |
| \| | OR | a \| b |
| ^ | XOR | a ^ b |
| ~ | NOT | ~a |
| << | Zero fill left shift | a << 2 |
| >> | Signed right shift | a >> 2 |

### Assignment Operators
| Operator | Description | Example |
| --- | --- | --- |
| = | Assigns values from right side operands to left side operand | c = a + b assigns value of a + b into c |
| += | Add AND | c += a is equivalent to c = c + a |
| -= | Subtract AND | c -= a is equivalent to c = c - a |
| *= | Multiply AND | c *= a is equivalent to c = c * a |
| /= | Divide AND | c /= a is equivalent to c = c / a |
| %= | Modulus AND | c %= a is equivalent to c = c % a |
| //= | Floor Division | c //= a is equivalent to c = c // a |
| **= | Exponent AND | c **= a is equivalent to c = c ** a |
| &= | Bitwise AND | c &= a is equivalent to c = c & a |
| \|= | Bitwise OR | c \|= a is equivalent to c = c \| a |
| ^= | Bitwise XOR | c ^= a is equivalent to c = c ^ a |
| >>= | Bitwise right shift | c >>= a is equivalent to c = c >> a |
| <<= | Bitwise left shift | c <<= a is equivalent to c = c << a |

### Identity Operators
| Operator | Description | Example |
| --- | --- | --- |
| is | Returns True if both variables are the same object | a is b |
| is not | Returns True if both variables are not the same object | a is not b |

### Membership Operators
| Operator | Description | Example |
| --- | --- | --- |
| in | Returns True if a sequence with the specified value is present in the object | x in y |
| not in | Returns True if a sequence with the specified value is not present in the object | x not in y |

<br>

## Conditional Statements
Python has 3 types of conditional statements:
