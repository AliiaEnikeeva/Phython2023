"""
def calc1(a):
    return a + a

def calk2(a):
    return a * a

def math(op, x):
    print(op(x))

math(calc1, 5) # первая переменная - функция, вторая переменная - значение
"""

# Можно с несколькими переменными
def calc1(a, b):
    return a + b

def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calc1, 5, 45) # первая переменная - функция, вторая переменная - значение
