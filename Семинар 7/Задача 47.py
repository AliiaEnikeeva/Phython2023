'''
Задача №47. Решение в группах
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values
ВВод:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values))
if values == transformed_values:
 print(‘ok’)
else:
 print(‘fail’)
Вывод:
ok 
'''
# # ВАРИАНТ БЕЗ map
# def f(x):
#     return x * 2

# def f2(x, y):
#     list1 = []
#     for i in y:
#         list1.append(x(i))
#     return list1

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = list(f2(f, values))
# print(values)
# print(transformed_values)


# ВАРИАНТ 2 через map
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(lambda x: x, values))
print(values)
print(transformed_values)