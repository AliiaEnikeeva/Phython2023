'''Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
ВВод 300
Вывод 220 284
'''
def sum_of_div(n):
    sum_div = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum_div += i
    return sum_div


# print(sum_of_div(220))
# print(sum_of_div(284))

num = int(input('Введите число k: '))
skip = None
for j in range(2, num):
    if j == skip:
        continue
    sum_j = sum_of_div(j)
    for k in range(2, num):
        if k == j:
            continue
        if k == sum_j:
            if j == sum_of_div(k):
                print(j, k)
                skip = k





# ВАРИАНТ МАРАТА
# def sum_divisors(num):
#     summ = 0
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             # print(f'{i = }')
#             summ += i
#     return summ


# def friends_num(number):
#     for i in range(1, number):
#         j = sum_divisors(i)
#         if i < j <= number and i == sum_divisors(j):
#             print(i, j)
