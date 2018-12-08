__author__ = 'Шкрет Павел Александрович'
import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    if (n < 1) or (n >= m):
        print('Error')
        return
    fl = [0, 1]
    counter = 1
    while counter < n:
        fl[1] = fl[0] + fl[1]
        fl[0] = fl[1] - fl[0]
        counter += 1
    while counter <= m:
        fl[1] = fl[0] + fl[1]
        fl[0] = fl[1] - fl[0]
        counter += 1
        print(fl[0])

    pass


fibonacci(1, 10)
''''''
1
1
2
3
5
8
13
21
34
55
''''''
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    right = len(origin_list)
    left = 0
    while left < right:
        minx = left
        for x in range(left, right):
            if origin_list[x] < origin_list[minx]:
                minx = x
        t = origin_list[left]
        origin_list[left] = origin_list[minx]
        origin_list[minx] = t
        left += 1
    print(origin_list)
    pass


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
#           [-12, -11, 0, 2, 2.5, 4, 4, 10, 20]
print('\n')
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, lst):
    for item in lst:
        if func(item):
            yield item
    pass


print(list(my_filter(lambda x: x > 0, [1, -2, 3, -1, 2, -3])))
print(list(filter(lambda x: x > 0, [1, -2, 3, -1, 2, -3])))

# [1, 3, 2]
# [1, 3, 2]
print('\n')
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def line_length(a, b): # Длина вектора

    return math.sqrt((b[0] - a[0])**2 + (a[1] - b[1])**2)


def is_plgrm(_points):
    # Перебираем если вершины указаны не по порядку
    if line_length(_points[0], _points[1]) == line_length(_points[2], _points[3]) and \
            line_length(_points[0], _points[1]) > 0:
        return True

    if line_length(_points[0], _points[2]) == line_length(_points[1], _points[3]) and \
            line_length(_points[0], _points[2]) > 0:
        return True

    if line_length(_points[0], _points[3]) == line_length(_points[1], _points[2]) and \
            line_length(_points[0], _points[3]) > 0:
        return True
    return False
    pass


a1 = [0, 0]
a2 = [5, 1]
a3 = [4, 2]
a4 = [-1, 1]
points = [a1, a2, a3, a4]
print(is_plgrm(points))




