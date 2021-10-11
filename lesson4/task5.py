# -*- coding: utf-8 -*-
'''
Задание: 5
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти чётные числа от 100 до 1000 (включая границы). 
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce

# проверка результата :)
# print(sum([x for x in range(100, 1001, 2)]))

print(reduce(lambda x, y: x + y,  [x for x in range(100, 1001, 2)]))