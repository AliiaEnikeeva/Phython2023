# ВАРИАНТ 1
'''
чтобы импортировать функцию из другого файла надо указать название модуля (который создали в отдельном файле) через коману import
надо импортировать 

import modul1

# затем обратиться к функции указав/ передавая переменные/значения

print(modul1.max1(5, 9)) 
'''
# ВАРИАНТ 2
'''
from modul1 import max1

print(max(10, 15))
'''

# ВАРИАНТ 3 можно сократить
import modul1 as m1

print(m1.max1(10, 15))