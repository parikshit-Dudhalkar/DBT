Its a high level language
Dynamically typed - data type is based on value assigned

Dont need to declare data type , it will automatically take datatype - int , float, char, string , boolean


Typecasting - num=int(input())
Multiple input - x,y,z=input().split()
		 List Comprehension - x,y,z=[ int(x) for x in input().split()]
		 
Operator - Arithmatic, comparison, Logical, Bitwise, Assignment, Identity, Membership, Ternary, Division

String - Array of bytes representing unicode char 
String, reverse string, slicing, delete/update string 

DS- List, Set, Tuple, Dict 

List:- [] - can have duplicate values - allow duplicate -Mutable - Ordered - append, insert, extend, reverse, remove, pop, slicing 

Tuple:- () - Immutable - ordered - Allow Duplicate - concat, slicing 

Set:- {}  - Immutable - Unordered - No duplicate - add, update , remove, pop, clear 

Dict:- {key:value} - 3.7 ordered , below 3.6 unordered , Mutable, Duplicate keys not allowed.

pass, continue, break , yield
Generator, Lambda, Local, global, OOP, self __init__(default and parameterized constructor), 
Instance, Exception Handling, Error Handling , Try Except, Else, Finally, Else 

File Handling - open()

Regular Expression

loc is label-based, meaning you access elements using the actual labels (index names or column names).
iloc is position-based, meaning you access elements using the integer positions (0-based indices).md
==========================================================================
==========================================================================
==========================================================================
==========================================================================
==========================================================================
==========================================================================
1. Control Structures
Conditional Statements (if, elif, else)
Definition: Conditional statements allow the execution of certain code blocks based on the evaluation of conditions.

Examples:

Basic Conditional Statements:

python
Copy code
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
Nested Conditional Statements:

python
Copy code
age = 20
has_ticket = True

if has_ticket:
    if age >= 18:
        print("You are an adult and can enter.")
    else:
        print("You are a minor and need parental guidance.")
else:
    print("You need a ticket to enter.")
Loops (for, while)
Definition: Loops are used to execute a block of code repeatedly based on a condition or over a sequence.

Examples:

For Loop:

python
Copy code
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range function
for i in range(5):
    print(i)
While Loop:

python
Copy code
count = 0
while count < 5:
    print(count)
    count += 1
Loop Control Statements (break, continue):

python
Copy code
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
Comprehensions
Definition: Comprehensions provide a concise way to create lists, dictionaries, or sets. They are a more readable and expressive way to generate these collections.

Examples:

List Comprehensions:

python
Copy code
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]
Dictionary Comprehensions:

python
Copy code
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_comprehension = {k: v for k, v in zip(keys, values)}
print(dict_comprehension)  # Output: {'a': 1, 'b': 2, 'c': 3}
Set Comprehensions:

python
Copy code
numbers = [1, 2, 2, 3, 4, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)  # Output: {1, 4, 9, 16}
2. Functions
Defining Functions
Definition: Functions are reusable blocks of code that perform a specific task and can be called with arguments.

Examples:

Defining and Calling Functions:

python
Copy code
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Output: Hello, Alice!
Function Arguments and Return Values
Definition: Functions can accept parameters (arguments) and return values. They can have default values and variable numbers of arguments.

Examples:

Default Arguments:

python
Copy code
def multiply(a, b=2):
    return a * b

print(multiply(5))    # Output: 10 (b is default)
print(multiply(5, 3)) # Output: 15
Keyword Arguments and Variable-Length Arguments:

python
Copy code
def describe_person(name, age, **kwargs):
    description = f"{name} is {age} years old."
    for key, value in kwargs.items():
        description += f" {key}: {value}."
    return description

print(describe_person("Alice", 30, city="New York", job="Engineer"))
# Output: Alice is 30 years old. city: New York. job: Engineer.

===Lambda Functions===
Definition: Lambda functions are small anonymous functions defined using the lambda keyword.
They are often used for short, simple operations.

Examples:

Basic Lambda Function:

python
Copy code
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
Using Lambda with Higher-Order Functions:

python
Copy code
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]


3. Modules and Packages
Importing Modules
Definition: Modules are files containing Python code.
You can import these modules into your code to use their functions, classes, or variables.

Examples:

Importing a Module:

python
Copy code
import math
print(math.sqrt(16))  # Output: 4.0
Importing Specific Functions:

python
Copy code
from math import pi, sqrt
print(pi)  # Output: 3.141592653589793
print(sqrt(25))  # Output: 5.0
Importing with Aliases:

python
Copy code
import numpy as np
array = np.array([1, 2, 3])
print(array)  # Output: [1 2 3]
Standard Library Overview
Definition: The Python Standard Library is a collection of modules and packages that come with Python and provide a wide range of functionalities.

Examples:

Common Standard Library Modules:

python
Copy code
import datetime
now = datetime.datetime.now()
print(now)  # Output: Current date and time

import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)  # Output: {"name": "Alice", "age": 30}
Creating and Using Packages
Definition: Packages are directories containing multiple modules and an __init__.py file. 
They help in organizing related modules and code.

Examples:

Creating a Package Structure:

markdown
Copy code
my_package/
├── __init__.py
├── module1.py
└── module2.py
Using a Package:

python
Copy code
# In module1.py
def func1():
    return "Function 1"

# In module2.py
def func2():
    return "Function 2"

# In a script
from my_package import module1, module2
print(module1.func1())  # Output: Function 1
print(module2.func2())  # Output: Function 2
Creating and Using a Package with __init__.py:

__init__.py File:

python
Copy code
# In my_package/__init__.py
from .module1 import func1
from .module2 import func2
Using the Package:

python
Copy code
from my_package import func1, func2
print(func1())  # Output: Function 1
print(func2())  # Output: Function 2
These explanations and examples should help solidify your understanding of core Python concepts, 
including control structures, functions, and modules and packages.




==========================================================================
==========================================================================
==========================================================================
==========================================================================


























-------------------------------------==========================================================================
==========================================================================
==========================================================================
==========================================================================
==========================================================================


 Lists, Tuples, and Sets
Definitions:

Lists: Ordered, mutable collections of items. Lists allow duplicate elements and can contain different data types.
Tuples: Ordered, immutable collections of items. Tuples allow duplicate elements and can contain different data types.
Sets: Unordered collections of unique items. Sets do not allow duplicate elements.
Examples:
==========================================================================
====Lists:====

Create a List:

python
Copy code
empty_list = []
single_value_list = [1]
my_list = [1, 2, 3, 4]
Insert Data:

python
Copy code
my_list.append(5)            # Adds 5 to the end
my_list.insert(2, 2.5)       # Inserts 2.5 at index 2
Update Data:

python
Copy code
my_list[1] = 10              # Updates the value at index 1 to 10
Example:

python
Copy code
my_list = [1, 2, 3, 4]
my_list.append(5)
my_list.insert(2, 2.5)
my_list[1] = 10
print(my_list)  # Output: [1, 10, 2.5, 3, 4, 5]
Tuples:

==========================================================================
===Create a Tuple:===

python
Copy code
empty_tuple = ()
empty_tuple = tuple()
single_value_tuple = (1,)
my_tuple = (1, 2, 3, 4)
Insert Data: (Tuples are immutable, so you can't directly insert or update. You need to create a new tuple.)

python
Copy code
my_tuple = my_tuple + (5,)  # Adds 5 as a new tuple
Update Data: (Tuples are immutable; you need to create a new tuple with the updated values.)
    
python
Copy code
my_tuple = (1, 10, 2.5, 3, 4)
Example:

python
Copy code
my_tuple = (1, 2, 3, 4)
my_tuple = my_tuple + (5,)
my_tuple = (1, 10, 2.5, 3, 4)
print(my_tuple)  # Output: (1, 10, 2.5, 3, 4)
Sets:

==========================================================================
===Create a Set:===

python
Copy code
empty_set = set()
single_value_set = {1}
my_set = {1, 2, 3, 4}
Insert Data:

python
Copy code
my_set.add(5)           # Adds 5 to the set
Update Data: (Update involves adding/removing elements as sets are mutable but do not have index-based updates.)

python
Copy code
my_set.remove(2)        # Removes 2 from the set
Example:

python
Copy code
my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}


==========================================================================
==Dictionaries====

Definition: Dictionaries are unordered collections of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples).

Examples:

Create a Dictionary:

python
Copy code
my_dict = {'name': 'Alice', 'age': 25}
Insert Data:

python
Copy code
my_dict['city'] = 'New York'  # Adds a new key-value pair
Update Data:

python
Copy code
my_dict['age'] = 26           # Updates the value for the key 'age'
Example:

python
Copy code
my_dict = {'name': 'Alice', 'age': 25}
my_dict['city'] = 'New York'
my_dict['age'] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}
3. Collections Module
The collections module provides alternatives to built-in types with additional functionality.

Examples:

NamedTuples: Provide a way to define simple classes with named fields.

Create a NamedTuple:

python
Copy code
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
p = Person(name='Alice', age=25)
Access and Update Data:

python
Copy code
# NamedTuples are immutable, so you can't update fields directly.
p = p._replace(age=26)  # Create a new NamedTuple with updated age
print(p)  # Output: Person(name='Alice', age=26)
DefaultDict: A dictionary that returns a default value if the key is not found.

Create a DefaultDict:

python
Copy code
from collections import defaultdict

d = defaultdict(int)  # Default value is 0
d['a'] += 1
Access Data:

python
Copy code
print(d['a'])  # Output: 1
print(d['b'])  # Output: 0 (default value)
Counter: A dictionary subclass for counting hashable objects.

Create and Use a Counter:

python
Copy code
from collections import Counter

c = Counter(['apple', 'banana', 'apple', 'orange'])
Access and Update Data:

python
Copy code
c['apple'] += 1
print(c)  # Output: Counter({'apple': 3, 'banana': 1, 'orange': 1})
These examples illustrate how to create, insert, and update data in lists, tuples, sets, dictionaries, and using the collections module.

==========================================================================
==========================================================================
==========================================================================
===========================================================================
==========================================================================
1. Reading and Writing Files
Definition: File handling involves operations such as reading from and writing to files on the filesystem. This is crucial for data persistence and file-based data manipulation.

Examples:

Reading Files:

Read Entire File:

python
Copy code
with open('example.txt', 'r') as file:
    content = file.read()
print(content)
Read Line by Line:

python
Copy code
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
Writing Files:

Write to a File (Overwrite):

python
Copy code
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
Append to a File:

python
Copy code
with open('example.txt', 'a') as file:
    file.write("Appending a new line.\n")
Example File Handling:

python
Copy code
# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)

# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Overwriting the file content.\n")

# Appending to the file
with open('example.txt', 'a') as file:
    file.write("Appending another line.\n")
2. Working with CSV and JSON
Definition: CSV and JSON are common data formats used for storing and exchanging data. CSV (Comma-Separated Values) is a simple text format, while JSON (JavaScript Object Notation) is a lightweight data interchange format.

Examples:

CSV (Comma-Separated Values):

Reading CSV Files:

python
Copy code
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
Writing CSV Files:

python
Copy code
import csv

data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
JSON (JavaScript Object Notation):

Reading JSON Files:

python
Copy code
import json

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
Writing JSON Files:

python
Copy code
import json

data = {'name': 'Alice', 'age': 30}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
Example File Handling with CSV and JSON:

python
Copy code
import csv
import json

# CSV Handling
csv_data = [['Name', 'Age'], ['Alice', 30], ['Bob', 25]]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# JSON Handling
json_data = {'name': 'Alice', 'age': 30}
with open('data.json', 'w') as file:
    json.dump(json_data, file, indent=4)

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
3. Context Managers
Definition: Context managers are used to handle resources (e.g., files, network connections) 
efficiently by ensuring they are properly cleaned up after use, typically using the with statement.

Examples:

Using Context Managers for File Handling:

python
Copy code
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed after exiting the block
Creating a Custom Context Manager:

Using a Class:

python
Copy code
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileOpener('example.txt', 'w') as file:
    file.write('Hello, Context Manager!\n')
Using a Generator Function:

python
Copy code
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with open_file('example.txt', 'r') as file:
    content = file.read()
    print(content)
Example Using Context Managers:

python
Copy code
# Using built-in context manager for file handling
with open('example.txt', 'w') as file:
    file.write('Using context manager.\n')

# Using custom context manager
class CustomContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with CustomContext() as context:
    print("Inside the context")
These examples demonstrate how to handle file operations, work with CSV and JSON data formats, and utilize context managers for efficient resource management in Python.



==========================================================================
==========================================================================
==========================================================================
==========================================================================
==========================================================================
1. Exceptions
Definition: Exceptions are errors that occur during program execution. 
Python provides a way to handle these errors using exception handling mechanisms to prevent the program 
from crashing and to provide meaningful error messages.

Examples:

Basic Exception Handling:

python
Copy code
try:
    x = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero!")
Handling Multiple Exceptions:

python
Copy code
try:
    x = int("hello")  # This will raise a ValueError
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")
2. Try, Except, Finally
Definition: The try block contains code that might raise an exception, the except block contains code to handle the exception, and the finally block contains code that will always execute regardless of whether an exception was raised or not.

Examples:

Using Try, Except, Finally:

python
Copy code
try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()
    print("File is closed.")
Handling Exceptions with a Clean-up Operation:

python
Copy code
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Execution completed.")
    return result

print(divide(10, 2))  # No error
print(divide(10, 0))  # Division by zero
3. Custom Exceptions
Definition: Custom exceptions are user-defined exception classes that allow for more specific error handling tailored to the application's needs.

Examples:

Creating and Using Custom Exceptions:

Define a Custom Exception:

python
Copy code
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"CustomError: {self.message}"
Raise and Handle Custom Exceptions:

python
Copy code
def check_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative!")
    elif age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")

try:
    check_age(-5)
except CustomError as e:
    print(e)
Custom Exception with Additional Attributes:

python
Copy code
class DetailedError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        return f"DetailedError (code {self.code}): {self.message}"

def process_data(data):
    if data < 0:
        raise DetailedError("Data cannot be negative", 400)
    return data * 2

try:
    result = process_data(-10)
except DetailedError as e:
    print(e)
Example:

python
Copy code
# Basic Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Try, Except, Finally
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("File operation is complete.")

# Custom Exception
class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value error: {value}")

def check_value(value):
    if value < 0:
        raise NegativeValueError(value)

try:
    check_value(-5)
except NegativeValueError as e:
    print(e)
These examples demonstrate how to handle exceptions, use try, except, and finally blocks for error management, 
and create custom exceptions to address specific error conditions in your Python programs.

==========================================================================
==========================================================================
==========================================================================
1. OOP Basics
Definition: Object-Oriented Programming is a programming paradigm that uses objects and classes to structure code. It helps in organizing and modeling complex systems using objects that combine data and functionality.

Classes and Objects
Definition:

Classes are blueprints for creating objects. They encapsulate data and methods that operate on that data.
Objects are instances of classes. They are created based on the class blueprint.
Examples:

Creating a Class and Object:

python
Copy code
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Create an object of the Dog class
my_dog = Dog(name="Buddy", age=3)
print(my_dog.bark())  # Output: Buddy says woof!
Attributes and Methods
Definition:

Attributes are variables that belong to a class and represent the state of an object.
Methods are functions defined within a class that describe the behaviors of an object.
Examples:

Defining Attributes and Methods:

python
Copy code
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"The {self.make} {self.model}'s engine is starting."

my_car = Car(make="Toyota", model="Corolla", year=2020)
print(my_car.start_engine())  # Output: The Toyota Corolla's engine is starting.
Inheritance
Definition: Inheritance allows a class to inherit attributes and methods from another class. This promotes code reuse and establishes a relationship between classes.

Examples:

Basic Inheritance:

python
Copy code
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

my_cat = Cat(name="Whiskers")
print(my_cat.speak())  # Output: Whiskers says meow!
2. Advanced OOP
Polymorphism
Definition: Polymorphism allows methods to do different things based on the object calling them. 
It enables objects of different classes to be treated as objects of a common superclass.

Examples:

Polymorphism with Method Overriding:

python
Copy code
class Bird:
    def fly(self):
        return "Bird is flying"

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly"

def make_bird_fly(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()

make_bird_fly(sparrow)  # Output: Bird is flying
make_bird_fly(penguin)  # Output: Penguins cannot fly
Encapsulation
Definition: Encapsulation is the concept of restricting access to certain details of an object and exposing only what is necessary. 
It helps in hiding the internal state of the object and protects it from unintended modifications.

Examples:

Encapsulation with Private Attributes:

python
Copy code
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(owner="Alice", balance=1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
Magic Methods and Operator Overloading
Definition: Magic methods are special methods with double underscores that allow classes to implement or customize behaviors for built-in operations (e.g., arithmetic operations, comparisons).

Examples:

Operator Overloading:

python
Copy code
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
print(v3)  # Output: Vector(6, 4)
3. Design Patterns
Definition: Design patterns are standard solutions to common problems in software design. They provide templates for solving issues in a way that is both efficient and easy to understand.

Singleton
Definition: The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.

Examples:

Implementing Singleton Pattern:

python
Copy code
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True (both variables refer to the same instance)
Factory
Definition: The Factory pattern provides a method for creating objects without specifying the exact class of object that will be created. It encapsulates object creation logic.

Examples:

Implementing Factory Pattern:

python
Copy code
class Car:
    def __init__(self, make):
        self.make = make

    def __repr__(self):
        return f"Car({self.make})"

class CarFactory:
    @staticmethod
    def create_car(make):
        return Car(make)

car = CarFactory.create_car("Toyota")
print(car)  # Output: Car(Toyota)
Observer
Definition: The Observer pattern defines a one-to-many dependency between objects, where a change in one object results in updates to dependent objects.

Examples:

Implementing Observer Pattern:

python
Copy code
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Observer received message: {message}")

subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("Hello Observers!")  
# Output:
# Observer received message: Hello Observers!
# Observer received message: Hello Observers!
These examples cover the fundamental and advanced aspects of Object-Oriented Programming, 
as well as design patterns, demonstrating how to apply these concepts in practical scenarios.

==========================================================================
==========================================================================
==========================================================================
==========================================================================

         Drops rows where less than 2 non-NaN values exist.