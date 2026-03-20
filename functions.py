# Functions in Python

# Basic Function
def greet():
    print("Hello, World!")

greet()

# Function with Parameter
def add(a, b):
    return a + b

print(add(5, 3))
print(add(10, 20))

# Function with Default Parameter
def power(base, exp=2):
    return base ** exp

print(power(3))
print(power(2, 10))

# Function with Multiple Returns
def calculator(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

a, s, m, d = calculator(10, 2)
print(f"Add: {a}")
print(f"Sub: {s}")
print(f"Mul: {m}")
print(f"Div: {d}")

# Lambda Function
square = lambda x: x ** 2
cube = lambda x: x ** 3

print(square(4))
print(cube(3))

# Recursive Function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

