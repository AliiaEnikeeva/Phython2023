'''
Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
'''
def factorial(n):
    counter = 1
    res = 1
    while counter <= n:
        res *= counter
        counter +=1
    return res    

a = int(input('Введите число: '))
print(f'Факториал числа {a}: {factorial(a)}')