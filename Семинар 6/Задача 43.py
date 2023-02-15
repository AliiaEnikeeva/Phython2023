'''
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 12323
Вывод 2
'''

#from random import randint
def number_list(x):
    list_1 = []
    for _ in range(x):
        list_1.append(int(input('Введите число: ')))
    return list_1

def count_pair(list_1: list):
    summ_pair = 0
    for i in set(list_1):
        summ_pair += list_1.count(i) // 2
    return summ_pair


# list_2 = [1, 2, 3, 2, 3, 2, 3, 5, 5]
list_2 = (number_list(int(input('Введите колво чисел: '))))
print(list_2)
print(count_pair(list_2))

# ВАРИАНТ МАРАТА
'''def count_pairs(inp_lst: list):
    return sum([inp_lst.count(i) // 2 for i in set(inp_lst)])
return sum(inp_lst.count(i) // 2 for i in set(inp_lst))
'''
