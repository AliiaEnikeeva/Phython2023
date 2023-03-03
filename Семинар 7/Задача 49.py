'''
Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
ВВод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
'''
# import math
# def find_farthest_orbit(x):
#     spis = []
#     for i in x:
#         if i[0] != i[1]:
#             spis.append(round(math.pi * i[0] * i[1], 2))
#     return filter(lambda l: round(math.pi * l[0] * l[1], 2) == max(spis), x)

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# print(*find_farthest_orbit(orbits))

# ВАРИАНТ ИРИНЫ
from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(list_of_orbits: list):
    for orbit in list_of_orbits: # если площадь текущей орбиты = максимальной (максимальную находим в списке всех орбит, кроме круговых)
        if orbit[0] * orbit[1] * pi == max(map(lambda lst: lst[0] * lst[1] * pi, filter(lambda lst: lst[0] != lst[1], list_of_orbits))):
            return orbit
    
print(*find_farthest_orbit(orbits))