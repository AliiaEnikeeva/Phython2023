'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

Пример:

5
1 2 3 4 5
6
-> 5
'''
import random
list_1 = []
n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите какое число надо найти в массиве: '))
for i in range(1, n+1):
    list_1.append(random.randint(1,n))
print(list_1)
dif = 0
if x > max(list_1):
    print(max(list_1))
elif x < min(list_1):
    print(min(list_1))
else:    
    while True:
        if x - dif in list_1 and x + dif in list_1 and x - dif != x + dif:
            print(x - dif, x + dif)
            break
        elif x - dif in list_1:
            print(x - dif)
            break
        elif x + dif in list_1:
            print(x + dif)
            break
        else:
            dif += 1