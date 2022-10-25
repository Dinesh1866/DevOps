<div align=center>
<h1><img src="https://img.icons8.com/fluency/30/000000/python.png"/> PYTHON</h1> </div>

Python is a High level, Object Oriented Dynamically typed and Interpreted Programming  and Scripting Language. It is a general purpose programming language and is used for a wide variety of applications like Web Development, Data Science, Machine Learning, Artificial Intelligence, etc.

<br>

> Dynamic Typing: In Python, we don't need to declare the type of the variable. The type of the variable is determined at runtime.

> Interpreted Language: Python is an interpreted language. It means that the code is not compiled into machine language. Instead, it is converted into bytecode and then interpreted by the Python Virtual Machine (PVM).

> Object Oriented: Python is an Object Oriented Programming Language. It supports Object Oriented Programming features like Inheritance, Encapsulation, Polymorphism, etc.

<br>

## Table of Contents
- [variables](#variables)
- [data types](#data-types)
- [operators](#operators)
- [conditional statements](#conditional-statements) (if-else, switch-case)
- [loops](#loops) (for, while)
- [iterators](#iterators)
- [Collections](#collections) (List, Tuple, Set, Dictionary)
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

> ==: It is used to check if two values are equal or not. It returns a boolean value.

> !=: It is used to check if two values are not equal or not. It returns a boolean value.

> (>): It is used to check if the first value is greater than the second value or not. It returns a boolean value.

> <: It is used to check if the first value is less than the second value or not. It returns a boolean value.

> (>=): It is used to check if the first value is greater than or equal to the second value or not. It returns a boolean value.

> <=: It is used to check if the first value is less than or equal to the second value or not. It returns a boolean value.

```python
# equal to
a = 10
b = 20
print(a == b) # o/p: False

# not equal to
a = 10
b = 20
print(a != b) # o/p: True

# greater than
a = 10
b = 20
print(a > b) # o/p: False

# less than
a = 10
b = 20
print(a < b) # o/p: True

# greater than or equal to
a = 10
b = 20
print(a >= b) # o/p: False

# less than or equal to
a = 10
b = 20
print(a <= b) # o/p: True
```


### Logical Operators
| Operator | Description | Example |
| --- | --- | --- |
| and | Returns True if both statements are true | a and b |
| or | Returns True if one of the statements is true | a or b |
| not | Reverse the result, returns False if the result is true | not(a and b) |

> and: It is used to check if both the statements are true or not. It returns a boolean value.

> or: It is used to check if one of the statements is true or not. It returns a boolean value.

> not: It is used to reverse the result. It returns a boolean value.

```python
# and
a = 10
b = 20
print(a == 10 and b == 20) # o/p: True

# or
a = 10
b = 20
print(a == 10 or b == 20) # o/p: True

# not
a = 10
b = 20
print(not(a == 10 and b == 20)) # o/p: False
```


### Bitwise Operators
| Operator | Description | Example |
| --- | --- | --- |
| & | AND | a & b |
| \| | OR | a \| b |
| ^ | XOR | a ^ b |
| ~ | NOT | ~a |
| << | Zero fill left shift | a << 2 |
| >> | Signed right shift | a >> 2 |

> &: It is used to perform bitwise AND operation. It returns an int value.

> |: It is used to perform bitwise OR operation. It returns an int value.

> ^: It is used to perform bitwise XOR operation. It returns an int value.

> ~: It is used to perform bitwise NOT operation. It returns an int value.

> <<: It is used to perform bitwise left shift operation. It returns an int value.

> >>: It is used to perform bitwise right shift operation. It returns an int value.

```python
# bitwise AND
a = 10
b = 20
print(a & b) # o/p: 0

# bitwise OR
a = 10
b = 20
print(a | b) # o/p: 30

# bitwise XOR
a = 10
b = 20
print(a ^ b) # o/p: 30

# bitwise NOT
a = 10
print(~a) # o/p: -11

# bitwise left shift
a = 10
print(a << 2) # o/p: 40

# bitwise right shift
a = 10
print(a >> 2) # o/p: 2
```


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

> =: It is used to assign values from right side operands to left side operand.

> +=: It is used to add AND. It is equivalent to c = c + a.

> -=: It is used to subtract AND. It is equivalent to c = c - a.

> \*=: It is used to multiply AND. It is equivalent to c = c * a.

> /=: It is used to divide AND. It is equivalent to c = c / a.

> %=: It is used to modulus AND. It is equivalent to c = c % a.

> //=: It is used to floor division AND. It is equivalent to c = c // a.

> \*\*=: It is used to exponent AND. It is equivalent to c = c \*\* a.

> &=: It is used to bitwise AND. It is equivalent to c = c & a.

> \|=: It is used to bitwise OR. It is equivalent to c = c \| a.

> ^=: It is used to bitwise XOR. It is equivalent to c = c ^ a.

> >>=: It is used to bitwise right shift. It is equivalent to c = c >> a.

> <<=: It is used to bitwise left shift. It is equivalent to c = c << a.

```python
# assignment
a = 10
b = 20
c = a + b
print(c) # o/p: 30

# add AND
a = 10
b = 20
c = 0

c += a
print(c) # o/p: 10

c += b
print(c) # o/p: 30

# subtract AND
a = 10
b = 20
c = 0

c -= a
print(c) # o/p: -10

c -= b
print(c) # o/p: -30

# multiply AND
a = 10
b = 20
c = 0

c *= a
print(c) # o/p: 0

c *= b
print(c) # o/p: 0

# divide AND
a = 10
b = 20
c = 0

c /= a
print(c) # o/p: 0.0

c /= b
print(c) # o/p: 0.0

# modulus AND
a = 10
b = 20
c = 0

c %= a
print(c) # o/p: 0

c %= b
print(c) # o/p: 0

# floor division AND
a = 10
b = 20
c = 0

c //= a
print(c) # o/p: 0

c //= b
print(c) # o/p: 0

# exponent AND
a = 10
b = 20
c = 0

c **= a
print(c) # o/p: 0

c **= b
print(c) # o/p: 0

# bitwise AND
a = 10
b = 20
c = 0

c &= a
print(c) # o/p: 0

c &= b
print(c) # o/p: 0

# bitwise OR
a = 10
b = 20
c = 0

c |= a
print(c) # o/p: 10

c |= b
print(c) # o/p: 30

# bitwise XOR
a = 10
b = 20
c = 0

c ^= a
print(c) # o/p: 10

c ^= b
print(c) # o/p: 30

# bitwise right shift
a = 10
b = 20
c = 0

c >>= a
print(c) # o/p: 0

c >>= b
print(c) # o/p: 0

# bitwise left shift
a = 10
b = 20
c = 0

c <<= a
print(c) # o/p: 0

c <<= b
print(c) # o/p: 0
```


### Identity Operators
| Operator | Description | Example |
| --- | --- | --- |
| is | Returns True if both variables are the same object | a is b |
| is not | Returns True if both variables are not the same object | a is not b |

> is: It is used to check if both variables are the same object.

> is not: It is used to check if both variables are not the same object.

```python
# identity
a = 10
b = 20
c = a

print(a is b) # o/p: False
print(a is c) # o/p: True

print(a is not b) # o/p: True
print(a is not c) # o/p: False
```

### Membership Operators
| Operator | Description | Example |
| --- | --- | --- |
| in | Returns True if a sequence with the specified value is present in the object | x in y |
| not in | Returns True if a sequence with the specified value is not present in the object | x not in y |

> in: It is used to check if a sequence with the specified value is present in the object.

> not in: It is used to check if a sequence with the specified value is not present in the object.

```python
# membership
a = 10
b = 20
c = [10, 20, 30, 40, 50]

print(a in c) # o/p: True
print(b in c) # o/p: True

print(a not in c) # o/p: False
print(b not in c) # o/p: False
```

<br>

## Conditional Statements
Python has 3 types of conditional statements:

1. if
2. if-else
3. if-elif-else
4. nested if
5. nested if-else
6. nested if-elif-else
7. switch-case

### if
> if: It is used to check if the given condition is true or not. If the condition is true, then it executes the statements inside the if block.

```python
# if
a = 10
b = 20

if a < b:
    print("a is less than b")
```

### if-else
> if-else: It is used to check if the given condition is true or not. If the condition is true, then it executes the statements inside the if block. If the condition is false, then it executes the statements inside the else block.

```python
# if-else
a = 10
b = 20

if a < b:
    print("a is less than b")
else:
    print("a is greater than b")
```

### if-elif-else
> if-elif-else: It is used to check if the given condition is true or not. If the condition is true, then it executes the statements inside the if block. If the condition is false, then it checks the next condition. If the next condition is true, then it executes the statements inside the elif block. If the next condition is false, then it executes the statements inside the else block.

```python
# if-elif-else
a = 10
b = 20

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")
```

### nested if
> nested if: It is used to check if the given condition is true or not. If the condition is true, then it executes the statements inside the if block. If the condition is false, then it executes the statements inside the else block.

```python
# nested if
a = 10
b = 20

if a < b:
    if a == 10:
        print("a is less than b and a is equal to 10")
    else:
        print("a is less than b and a is not equal to 10")
else:
    print("a is greater than b")
```

### nested if-else
> nested if-else: It is used to check if the given condition is true or not. If the condition is true, then it executes the statements inside the if block. If the condition is false, then it executes the statements inside the else block.

```python
# nested if-else
a = 10
b = 20

if a < b:
    if a == 10:
        print("a is less than b and a is equal to 10")
    else:
        print("a is less than b and a is not equal to 10")
else:
    if a == 10:
        print("a is greater than b and a is equal to 10")
    else:
        print("a is greater than b and a is not equal to 10")
```

### match-case

> match-case: It is used to check if the given condition is true or not. If the condition is true, then it executes the statements inside the if block. If the condition is false, then it executes the statements inside the else block.

```python
# match-case
a = 10

match a:
    case 10:
        print("a is equal to 10")
    case 20:
        print("a is equal to 20")
    case 30:
        print("a is equal to 30")
    case _:
        print("a is not equal to 10, 20 or 30")
```

<br>

## Loops
Python has 3 types of loops:

1. for
2. while
3. nested
      - nested for
      - nested while
      - nested for-while
      - nested while-for

### for
> for: It is used to iterate over a sequence (list, tuple, string) or other iterable objects.

```python
# for
a = [10, 20, 30, 40, 50]

for i in a:
    print(i)
```

### while
> while: It is used to iterate over a block of code as long as the test expression (condition) is true.

```python
# while
a = 0

while a < 5:
    print(a)
    a += 1
```

### nested
> nested: It is used to iterate over a block of code as long as the test expression (condition) is true.

```python
# nested
a = 0

while a < 5:
    print(a)
    a += 1

    for i in range(5):
        print(i)
```

<br>

## Collections
Python has 4 types of collections:

1. list
2. tuple
3. set
4. dictionary

### list
> list: It is a collection which is ordered and changeable. Allows duplicate members.

```python
# list
a = [10, 20, 30, 40, 50]
print(a)

a = [10, 20, 30, 40, 50, 10, "python", 3.14]
print(a)
```

### tuple
> tuple: It is a collection which is ordered and unchangeable. Allows duplicate members.

```python
# tuple
a = (10, 20, 30, 40, 50)
print(a)

a = (10, 20, 30, 40, 50, 10, "python", 3.14)
print(a)
```

### set
> set: It is a collection which is unordered and unindexed. No duplicate members.

```python
# set
a = {10, 20, 30, 40, 50}
print(a)

a = {10, 20, 30, 40, 50, 10, "python", 3.14}
print(a)
```

### dictionary
> dictionary: It is a collection which is unordered, changeable and indexed. No duplicate members.

```python
# dictionary
a = {
    "name": "python",
    "version": 3.9
}
print(a)

a = {
    "name": "python",
    "version": 3.9,
    "name": "python",
    "version": 3.9
}
print(a)
```

<br>

## Collections Methods

### list

#### 1. append
> append: It is used to add an item to the end of the list.

```python
# append
a = [10, 20, 30, 40, 50]
print(a)

a.append(60)
print(a) # [10, 20, 30, 40, 50, 60]
```

#### 2. clear
> clear: It is used to remove all items from the list.

```python
# clear
a = [10, 20, 30, 40, 50]
print(a)

a.clear()
print(a) # []
```

#### 3. copy
> copy: It is used to return a copy of the list.

```python
# copy
a = [10, 20, 30, 40, 50]
print(a)

b = a.copy()
print(b) # [10, 20, 30, 40, 50]
```

#### 4. count
> count: It is used to return the number of times the value appears in the list.

```python
# count
a = [10, 20, 30, 40, 50, 10, 20, 30, 40]
print(a)

print(a.count(10)) # 2
print(a.count(50)) # 1
```

#### 5. extend
> extend: It is used to add the elements of a list (or any iterable), to the end of the current list.

```python
# extend
a = [10, 20, 30, 40, 50]
print(a)

a.extend([60, 70, 80, 90, 100])
print(a) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

#### 6. index
> index: It is used to return the index of the first element with the specified value.

```python
# index
a = [10, 20, 30, 40, 50, 10, 20, 30, 40]
print(a)

print(a.index(10)) # 0
print(a.index(50)) # 4
```

#### 7. insert
> insert: It is used to add an item at the specified index.

```python
# insert
a = [10, 20, 30, 40, 50]
print(a)

a.insert(2, 60)
print(a) # [10, 20, 60, 30, 40, 50]
```

#### 8. pop
> pop: It is used to remove the item at the specified index.

```python
# pop
a = [10, 20, 30, 40, 50]
print(a)

a.pop(2)
print(a) # [10, 20, 40, 50]
```

#### 9. remove
> remove: It is used to remove the first item with the specified value.

```python
# remove
a = [10, 20, 30, 40, 50, 10, 20, 30, 40]
print(a)

a.remove(10)
print(a) # [20, 30, 40, 50, 10, 20, 30, 40]
```

#### 10. reverse
> reverse: It is used to reverse the order of the list.

```python
# reverse
a = [10, 20, 30, 40, 50]
print(a)

a.reverse()
print(a) # [50, 40, 30, 20, 10]
```

#### 11. sort
> sort: It is used to sort the list.

```python
# sort
a = [10, 20, 30, 40, 50]
print(a)

a.sort()
print(a) # [10, 20, 30, 40, 50]
```

### tuple

#### 1. count
> count: It is used to return the number of times the value appears in the tuple.

```python
# count
a = (10, 20, 30, 40, 50, 10, 20, 30, 40)
print(a)

print(a.count(10)) # 2
print(a.count(50)) # 1
```


#### 2. index

> index: It is used to return the index of the first element with the specified value.

```python
# index
a = (10, 20, 30, 40, 50, 10, 20, 30, 40)
print(a)

print(a.index(10)) # 0
print(a.index(50)) # 4
```

### set

#### 1. add
> add: It is used to add an element to the set.

```python
# add
a = {10, 20, 30, 40, 50}
print(a)

a.add(60)
print(a) # {40, 10, 50, 20, 60, 30}
```




## Functions