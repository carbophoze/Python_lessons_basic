import random
__author__ = 'Шкрет Павел Александрович'
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз", "апельсин", "мандарин", "папайя", "виноград", "манго", "дыня", "слива"]
max_len = 0
num = 0
for item in fruits:
    if len(item) > max_len:
        max_len = len(item)

num = 1
max_len += len(str(len(fruits)))
for item in fruits:
    print('{1}.{0:>{2}}'.format(item, num, max_len - len(str(num))))
    num += 1
'''
1.   яблоко
2.    банан
3.     киви
4.    арбуз
5. апельсин
6. мандарин
7.   папайя
8. виноград
9.    манго
10.    дыня
11.   слива
'''

print('\n')
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

arr1 = [random.randint(0, 10) for x in range(1, 10)]
arr2 = [random.randint(0, 10) for x in range(1, 10)]
print(arr1)
print(arr2)

for item in arr2:
    while item in arr1:
        print('Looking for {0} in {1} position is {2}'.format(item, arr1, arr1.index(item)))
        arr1.pop(arr1.index(item))

print('Result : {0}'.format(arr1))

'''
[8, 1, 4, 7, 1, 7, 8, 8, 9]
[8, 8, 1, 0, 4, 4, 7, 0, 1]
Looking for 8 in [8, 1, 4, 7, 1, 7, 8, 8, 9] position is 0
Looking for 8 in [1, 4, 7, 1, 7, 8, 8, 9] position is 5
Looking for 8 in [1, 4, 7, 1, 7, 8, 9] position is 5
Looking for 1 in [1, 4, 7, 1, 7, 9] position is 0
Looking for 1 in [4, 7, 1, 7, 9] position is 2
Looking for 4 in [4, 7, 7, 9] position is 0
Looking for 7 in [7, 7, 9] position is 0
Looking for 7 in [7, 9] position is 0
[9]
'''

print('\n')
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
arr1 = [random.randint(0, 10) for x in range(1, 10)]
arr2 = []
print(arr1)
for item in arr1:
    if item % 2 == 0:
        arr2.append(item / 4)
    else:
        arr2.append(item * 2)

print(arr2)
