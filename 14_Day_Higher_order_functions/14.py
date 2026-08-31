countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

from functools import reduce
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 10

def apply_twice(func, value):
    return func(func(value))

print(apply_twice(lambda x: x + 3, 10))  # 16

def make_multiplier(factor):
    def multiplier(x):
        return x * factor   # 'factor' is remembered from the enclosing scope
    return multiplier
double = make_multiplier(2)
print(double(5))  # 10 — 'factor' (2) is still accessible here

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)
        print("After the function runs")
        return result
    return wrapper
@my_decorator
def greet(name):
    print(f"Hello, {name}")
greet("Ball")
# Before the function runs
# Hello, Ball
# After the function runs