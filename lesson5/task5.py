# -*- coding: utf-8 -*-
"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

print("Генерация данных...")
numbers = random.randint(10, 10000)
data = [str(random.randint(1, 100)) for _ in range(numbers)]
with open("task5-output.txt", "wt") as file_output:
	file_output.write(" ".join(data))

print("Чтение и подсчет чисел из файла...")
with open("task5-output.txt") as file_input:
	amount = sum([int(x) for x in file_input.read().split()])
	print(f"Сумма чисел: {amount}")
