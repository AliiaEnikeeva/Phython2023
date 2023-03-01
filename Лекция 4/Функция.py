def f(x):
    return x * x

#print(type(f)) # класс функция

a = f
print(type(a)) # также класс функция
print(a(5)) # переменная а хранит в себе ссылку на функцию
