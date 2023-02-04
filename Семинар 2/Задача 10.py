'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

Пример:

Input 5 -> 1 0 1 1 0
Output 2
'''
from random import randint

k = 5
list_coins = []
for i in range(k):
    list_coins.append(randint(0, 1))
print(list_coins)
zero = list_coins.count(0) # посчитать сколько нулей
one = len(list_coins) - zero # посчитать сколько единиц
# print(zero)
# print(one)
if one < zero:
    print(one)
else:
    print(zero)
