# Найдите сумму цифр трехзначного числа. 
# Input 123
# Output 6 (1+2+3)

'''
var 1
n = int(input('Введите трехзначное число: ')) 
a1 = n % 10
a2 = n // 10 % 10
a3 = n // 100
print('Сумма трех цифр = ', a1 + a2 + a3)
'''
# Коммент Марата - Можно добавить проверку, что число 3-значное.

# var 2
num = input('Введите трехзначное число: ')
res = 0
if len(num) == 3:
    for i in num:
        res += int(i)
    print(res)
else:
    print('Вы ввели не трехзначное число')



