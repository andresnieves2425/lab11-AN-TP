"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a): math.sqrt(a)# raise ValueError if a < 0

def hypotenuse(a, b): math.hypot(a, b) # can have negative nums

def add(a, b): a + b

def subtract(a, b): a - b

def multiply(a, b): a * b

def divide(a, b): b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b): loga(b)# use math library/raise ValueError

def exponent(a, b): ab