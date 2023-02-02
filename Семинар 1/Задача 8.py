'''
Требуется определить, можно ли от шоколадки размером n
× m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
Input 324
Output yes
Input 321 
Output no
'''
'''
var 1
n = int(input())
m = int(input())
k = int(input())
if k < (n * m) and (k % n == 0 or k % m ==0):
    print('yes')
else:
    print('no')
'''
# var 2
n = int(input('Введите число n: '))
m = int(input('Введите число m: '))
k = int(input('Введите число k: '))
if k < n * m and (k % n == 0 or k % m == 0):
    print(f'{n} {m} {k} -> yes')
else:
    print(f'{n} {m} {k} -> no')
