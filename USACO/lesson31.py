# 1. Function
# 1.1 define a function and call it
# def hello():
#     print('Hello World')
# hello()

# 1.2 return values
# def my_func():
#     return 5 * 5
# my_func()
# print(my_func())
#
# def my_func():
#     return 5 * 5
#     # The following statement will not be executed
#     print(6)
# my_func()

# In fact, every function in Python must return a value.
# If you don't write the "return" statement, the function will return None automatically.

# def my_func():
#     print(5 * 5)
#     return None
# my_func()

# To let a function return multiple values as a tuple, use the return statement.
# def my_func(n, m):
#     quotient = n // m
#     remainder = n % m
#     return quotient, remainder
#
# a, b = my_func(5, 2)
# c = my_func(5, 2)
# print(a, b, type(a), type(b))
# print(c, type(c))

# 1.3 parameters
# Parameter:
# The variable listed inside the parentheses in a function definition
# (also called a "formal parameter", which only occupies a position without a specific value).
#
# Argument:
# The actual value passed inside the parentheses when a function is called
# (also called an "actual parameter", which has a concrete value).

# You can add as many parameters as you want, just separate them with a comma.

# def add(a, b, c):
#     return a + b + c
# print(add(1, 2, 3))

# default parameter value
# Default parameters must be placed after regular positional parameters.
# def my_func(name = 'Bessie'):
#     print('my name is', name)
# my_func('Max')
# my_func()

# # Rule 1: Default parameters follow positional parameters
def greet(name, greeting="Hello"):  # name: positional parameter; greeting: default parameter
    print(greeting, name)

# Rule 2: Keyword arguments allow reordering parameters
# Call function with keyword arguments (order doesn't matter)
# greet(greeting='Hi', name='Max')
# greet('Alice')

# Variable-length parameters (*args/**kwargs)
# *args(arguments): Accepts an arbitrary number of positional arguments and packs them into a tuple.
# **kwargs(keyword arguments): Accepts an arbitrary number of keyword arguments and packs them into a dictionary.
def my_sum(*args):
    print(args, type(args))
    total = 0
    for i in args:
        total += i
    return total
# print(my_sum(1, 2, 3, 4, 5))

def print_info(**kwargs):
    print(kwargs, type(kwargs))
    for i in kwargs.items():
        print(i, type(i))
# print_info(name='Maximuz', age=18, height=180)

# Function nesting:
# a function can be placed into the parameters of another function and passed as an argument.
# def my_func(x):
#     return x * x
#
# print(my_func(2))
# print(my_func(my_func(2)))
# print(my_func(my_func(my_func(2))))

# lambda (anonymous functions)
# One-line minimalistic functions used for simple operations, avoiding the overhead of defining a full def function
# add = lambda a, b: a + b
# print(add(2, 3))
#
# nums = [(1,3), (2,1), (4,2)]
# nums.sort()
# print(nums)
# nums.sort(key=lambda x: x[1])
# print(nums)

# 1.4 Variable Scope (Local/Global)
# Local Variable
# A variable defined inside a function, which takes effect only within the function.

# Global Variable
# A variable defined outside a function, which takes effect throughout the entire program.
# global Keyword
# Declare the use of a global variable inside a function (enables modification of the global variable).

# total = 0
# def print_total():
#     print('global total:', total)
# print_total()
#
# def modify_total():
#     global total
#     total += 1
# modify_total()
# print_total()
#
# def local_var():
#     total = 10
#     total += 1
#     print('local total:', total)
# local_var()
# print_total()

# Reference
# Pass value when parameters are immutable
# Pass reference when parameters are mutable
# def change_int(a):
#     print(a, id(a))
#     a = 10
#     print(a, id(a))
# a = 1
# change_int(a)
# print(a)
#
# a = [1, 2, 3]
# def change_list(lst):
#     lst.append(4)
# change_list(a)
# print(a)
#
# b = 1
# print(b, id(b))
# b = 2
# print(b, id(b))

# Exercise 1
# Enter any positive integer n (via input()).
# Create a function to check if n is a prime number and print the result.
# A prime is a positive integer > 1 that can only be divided evenly by 1 and itself.
# You can use math.sqrt()
# test_cases = [-2, 0, 1, 2, 4, 7, 9, 19]

import math
def is_prime(n):
    if n <= 1:
        return False

    ret = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ret = False
            break
    return ret

# test_cases = [-2, 0, 1, 2, 4, 7, 9, 19]
# for i in test_cases:
#     print(is_prime(i), end=' ')

# Exercise 2
# Use the input() function to enter a positive integer n.
# Print all prime numbers from 1 to n.
# For the output requirement, use print(i, end=' ') to display all results in a single line.
# n = int(input('n: '))
# for i in range(2, n + 1):
#     if is_prime(i):
#         print(i, end=' ')

# Exercise 3
# Given a list lst = [23, 10, 3, 63, 100, 201, 71]
# Define a function get_min_index(nums, start, stop) that returns the index of the minimum value from start to stop (excluding stop, following the logic of range).
# Use this function to implement selection sort.

# def get_min_index(nums, start, stop):
#     min_index = start
#     for j in range(start + 1, stop):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     return min_index
#
# lst = [23, 10, 3, 63, 100, 201, 71]
# for i in range(len(lst)):
#     index = get_min_index(lst, i, len(lst))
#     lst[index], lst[i] = lst[i], lst[index]
# print(lst)

########################################################
# 2. class
# Class name
class Person:
    # Class attribute, shared by all instances of the class
    species = 'human'
    count = 0

    # Constructor, optional but commonly used in classes for initialization during instantiation
    def __init__(self, name, age):
        # Instance attribute, unique to each object
        self.name = name
        self.age = age
        # Modify class attribute, the class name must be added before the attribute
        Person.count += 1

    # Class function/method
    def introduce(self):
        print(f'my name is {self.name}, and {self.age} years old ')

    def grow_up(self, age):
        self.age = age
        print(f'now i am {self.age} years old')

# Class instantiation
# p = Person('Maximuz', 18)
# p.introduce()
# p.grow_up(20)
# p.introduce()
#
# p1 = Person('Alice', 22)
# p1.introduce()
# Person.species = 'god'
# print(Person.count, Person.species)

# Inherit the parent class Person
class Student(Person):
    # Subclass constructor
    def __init__(self, name, age, score, course=None):
        # Execute the parent class's constructor first
        # This is not mandatory, but omitting it will cause the parent class's attributes to not be assigned,
        # leading to errors if used
        super().__init__(name, age)
        self.score = score
        self.course = course

    def study(self, course):
        self.course = course
        print(f'{self.name} is studying {self.course}')

# Instantiate the subclass, which has all attributes/methods of the parent class + subclass
# s1 = Student('Max', 15, 95)
# s1.introduce()
# s1.study('USACO')
#
# s2 = Student('Rose', 14, 96)
# s2.introduce()
# s2.study('Math')
#
# print(Person.count)

# Method overriding and polymorphism
# The subclass overrides the method of the parent class, making the "same method name" have different implementations in different subclasses;
# when calling, the corresponding method is automatically matched according to the type of the instance (core: inheritance + method overriding)
class Boy(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def introduce(self):
        print(f'i am a boy, my name is {self.name}, and {self.age} years old')

class Girl(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    # Method overriding
    def introduce(self):
        print(f'i am a girl, my name is {self.name}, and {self.age} years old')

def introduce(p):
    p.introduce()

# boy = Boy('Max', 18)
# girl = Girl('Lucy', 16)
#
# introduce(boy)
# introduce(girl)

# Static method, no instantiation required, usually used for tool classes
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0

# print(MathUtils.add(2, 3))
# print(MathUtils.is_even(13))

# 3 Module/Package
# Single .py file
# 3.1 Import the entire module
# import module_name
# import module_name as alias  # Simplify the module name

# import math
# import random as rd
#
# print(math.sqrt(16))
# print(rd.randint(1, 10))

# 3.2 Import specified content from a module
# from module_name import function / class / attribute
# from module_name import function / class as alias

# from math import pi, pow
# from random import randint as rint
# # from math import * # Not recommended, poor readability and prone to conflicts
# print(pi)
# print(pow(2, 3))
# print(rint(1, 10))

# 3.3 Package, import modules from a package
# A folder containing __init__.py (e.g., my_package/), which can store multiple module files
# import package_name.module_name
# from package_name import module_name
# from package_name.module_name import function/class

# 3.4 Use custom modules and packages
# Method 1
# import my_tools
# print(my_tools.add(3, 5))
# c = my_tools.Calculator()
# print(c.multiply(3, 5))
# print(my_tools.PI)

# Method 2
# from my_tools import add, Calculator
# print(add(3, 5))
# c = Calculator()
# print(c.multiply(3, 5))

# Method 3
# from my_tools import PI as pi
# print(pi)

# from my_package import math_tools, str_tools
# print(math_tools.my_sum(1, 2, 3, 4, 5))
# c = math_tools.Circle(5)
# print(c.area())
#
# print(str_tools.reverse_str('12345'))
# print(str_tools.upper_str('abcde'))










