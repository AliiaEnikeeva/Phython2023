'''
Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
Input 6
Output 1 4 1
'''
s = int(input('Введите общее кол-во журавликов: '))
a1 = s / 6 # сделал Петя
a2 = a1 # сделал Сережа
a3 = (a1 + a2) * 2 # сделала Катя
print('Петя сделал - ', int(a1))
print('Сережа сделал - ', int(a2))
print('Катя сделала - ', int(a3))
