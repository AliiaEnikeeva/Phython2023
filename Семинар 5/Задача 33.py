'''
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

from random import randint
''''
def change_my_marks(marks):
    max_mark = max(marks)
    min_mark = min(marks)
    marks = [str(i) for i in marks]
    # marks = list(map(str, marks)) # аналог 16 строки
    return ' '.join(marks).replace(str(max_mark), str(min_mark))

marks_list = [randint(1, 5) for _ in range(int(input('Введите количество оценок: ')))]
print(*marks_list)
print(change_my_marks(marks_list))

'''
#ВАРИАНТ 2
def change_my_marks(marks):
    max_mark = max(marks)
    min_mark = min(marks)
    for i in range(len(marks)):
        if marks[i] == max_mark:
            marks[i] = min_mark
    return marks

marks_list = [randint(1, 5) for _ in range(int(input('Введите количество оценок: ')))]
print(*marks_list)
print(*change_my_marks(marks_list))