'''
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
'''
def find_fibo(x, fibo_lst = [0, 1]): # обьявляем функцию и число х - число которое надо найти
     # и задаем начальный список с известными числами 0 и 1
    if len(fibo_lst) == x: # базовый
        print(fibo_lst)
        return fibo_lst[-1]
    else:
        fibo_lst.append(fibo_lst[-1] + fibo_lst[-2])
        return find_fibo(x, fibo_lst)

print(find_fibo(int(input('Введите номер числа Фиббоначи:'))))
