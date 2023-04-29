'''Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

*Пример:*
3 2 4 -> yes
3 2 1 -> no'''

n = int(input('Введите количество долек по горизонтали: '))
m = int(input('Введите количество долек по вертикали: '))
k = int(input('Введите количество долек, которое хотите отломить: '))

if (k >= n or k >= m) and k < n * m and (k % n == 0 or k % m == 0):
    print(f'От данной шоколадки можно отломить {k} долек за один разлом')
else:
    print(f'От данной шоколадки нельзя отломить {k} долек за один разлом')