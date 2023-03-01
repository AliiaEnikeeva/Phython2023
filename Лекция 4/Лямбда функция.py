def calk2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

def calc1(a, b):
    return a + b

#calk1 = lambda a,b: a + b # форма сокращения def calc1 (в одну строчку)

#math(calc1, 5, 45) # сократить еще короче. вставить вместо calk1 - знание переменной (функцию лямбда)

math(lambda a,b: a + b, 5, 45)