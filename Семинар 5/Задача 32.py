'''
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод : [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод:  [1, 9, 13, 14, 19]
'''

def create_list(x: int):
    my_list = []
    for _ in range(x):
        my_list.append(int(input('Введите число: ')))
    return my_list


def indexes_of_numbers(num_lst: list, start: int, end: int):
    indexes_list = []
    for i in range(len(num_lst)):
        if start <= num_lst[i] <= end:
            indexes_list.append(i)
    return indexes_list

num_list = create_list(int(input('Введите размер массива: ')))
left_endpoint = int(input('Введите минимум диапазона: '))
right_endpoint = int(input('Введите максимум диапазона: '))

print(*num_list)
print(*indexes_of_numbers(num_list, left_endpoint, right_endpoint))
