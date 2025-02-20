"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


''' рекурсия медленнее '''


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


''' самое оптимальное  '''


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


''' решение с использованием встроенных функций тоже не плохо но по сравнению с предыдущем использует на одну встроенную 
 функцию больше из-за чего работает медленнее'''


def revers_5(enter_num):
    return (str(enter_num))[::-1]


enter_num = 127685378667567880

print('revers  ', (timeit('revers(enter_num)', globals=globals(), number=10000)))
print('revers_2', (timeit('revers_2(enter_num)', globals=globals(), number=10000)))
print('revers_3', (timeit('revers_3(enter_num)', globals=globals(), number=10000)))
print('revers_4', (timeit('revers_4(enter_num)', globals=globals(), number=10000)))
print('revers_5', (timeit('revers_5(enter_num)', globals=globals(), number=10000)))