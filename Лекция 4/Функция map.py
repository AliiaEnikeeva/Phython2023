'''
list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1)) # Применяет функцию ко все объектам
print(list_1)

'''
#VAR 2

def where(f, col): # будет возвращать только те значения, которые прошли проверку f(x)
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)