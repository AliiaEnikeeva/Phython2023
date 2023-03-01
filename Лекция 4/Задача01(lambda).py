'''
В списке хранятся числаю Нужно выбрать только четные числа
и составить список пар( число; квадрат числа)
'''
# VAR 1
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)

# VAR 2

def select(f, col): # возвращает список, в котором к каждому элементу применили функцию f
    return [f(x) for x in col] 

def where(f, col): # будет возвращать только те значения, которые прошли проверку f(x)
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
