'''
: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
Input 4 -> 1 2 3 4
Output 9
'''
from random import randint
n = int(input('Введите кол-во кустов: '))
list_1 = [randint(0, n) for i in range(n)]
print(list_1)
print(len(list_1))
max_1 = 0
for i in range(len(list_1)):
    if i == len(list_1) - 1:
        summa = list_1[i - 1] + list_1[i] + list_1[0] # если последний куст
        # print(summa)
    else:
        summa = list_1[i - 1] + list_1[i] + list_1[i + 1]
    max_1 = summa if summa > max_1 else max_1
print(max_1)

# var 2 ИРИНЫ
# from random import randint
# berry_num = [randint(0, 20) for i in range(int(input('Введите количество кустов: ')))]
# print(*berry_num)
# max_berries = 0
# for i in range(len(berry_num)):
#     if i == len(berry_num) - 1:
#         total_berries = berry_num[i - 1] + berry_num[i] + berry_num[0]
#     else:
#         total_berries = berry_num[i - 1] + berry_num[i] + berry_num[i + 1]
#     max_berries = total_berries if total_berries > max_berries else max_berries
# print(max_berries)