'''
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

Пример:

5
1 2 3 4 5
3
-> 1
'''
import random
list_1 = []
n = int(input('Введите количество элементов в массиве: '))
x = int(input("Введите какое число надо найти и посчитать в массиве: "))
for i in range(1, n+1):
    list_1.append(random.randint(1,n))
print(list_1)
c = list_1.count(x)
print(f'В массиве число {x} встречается {c} раз')

# var 2 (на уроке)
# from random import randint
# n = 5
# # list_2 = []
# # for i in range(n):
# #     list_2.append(randint(1, n)) # или эти три строчки с циклом можно записать в одну list_2 = [randint(1, n) for i in range(n)]
# list_2 = [randint(1, n) for i in range(n)]
# print(list)