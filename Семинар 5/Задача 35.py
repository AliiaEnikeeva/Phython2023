'''
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
'''
def num_is_prime(x):
    for f in range(2, x):
        print(f'{f = }')
        if x % f == 0:
            return 'No'
    return 'Yes'


print(num_is_prime(int(input('Введите число: '))))