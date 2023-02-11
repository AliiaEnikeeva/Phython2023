# ВАРИАНТ 1
# def sum_numbers(n): # создали функцию
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     print(summa)

# sum_numbers(5) # вызвали функцию

# ВАРИАНТ 2
# def sum_numbers(n): # создали функцию
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# print(sum_numbers(5))

# ВАРИАНТ 3
# def sum_numbers(n): # создали функцию
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa  
# a = sum_numbers(5)
# print(a)


# def sum_numbers(n, y = 'Hello'): # создали функцию
#     print(y) # выводит по умочанию, если не задаем при выводе
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
    
# a = sum_numbers(5)
# print(a)

def sum_numbers(n, y = 'Hello'): # создали функцию
    print(y) # выводит по умочанию, если не задаем при выводе
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
    
a = sum_numbers(5, 'qwerty') # выведет заданную переменную
print(a)
