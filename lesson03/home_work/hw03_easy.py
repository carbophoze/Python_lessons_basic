__author__ = 'Шкрет Павел Александрович'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    p2len = len(str(int(str(number).split('.')[1])))  # Длина дробной части
    k = p2len  # Коэффициент преобразования
    x = number * (10 ** k)
    while k > ndigits:
        if x % 10 > 4:
            x += 10
        x //= 10
        k -= 1
    x = x / (10 ** ndigits)
    if ndigits == 0:
        return int(x)
    return x


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(0.0, 3))

# 2.12346
# 2.2
# 3.0
# 0.0
#

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    t = [int(x) for x in str(ticket_number)]
    if not(len(t) == 6):
        return 'Invalid number'
    if sum(t[:3]) == sum(t[3:]):
        return 'Lucky ticket!'
    return 'Nolucky ticket!'
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

# Lucky ticket!
# Invalid number
# Lucky ticket!