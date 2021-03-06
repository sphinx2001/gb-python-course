# -*- coding: utf-8 -*-
"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

data_dict = {}
with open("task6-input.txt", encoding="utf8") as file_input:
	for line in file_input.readlines():
		subject, *hours = line.split()
		subject = subject[:-1]
		total = 0
		for item in hours:
			hour = int("".join([x for x in item if x.isdigit()]))
			total += hour
		data_dict[subject] = total

	print(data_dict)