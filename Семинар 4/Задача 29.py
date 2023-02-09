
'''
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих
слайдах
'''
# код Ваня
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#     max_number = n
# print(max_number)

# Исправленный код Вани
# n = int(input())
# max_number = n
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

# код Петя
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n) 

# Исправленный код Пети
n = int(input())
max_number = n
while n > 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number) 
