'''
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
'''
A = int(input('Введите число больше 1: '))
n1, n2 = 0, 1
counter = 2
while n2 < A:
    n1, n2 = n2, n1 + n2
    counter += 1
if n2 == A:
    print(f'{A} - число Фиббоначи №{counter}')
else:
    print('-1')
