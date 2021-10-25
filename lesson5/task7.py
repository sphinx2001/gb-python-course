# -*- coding: utf-8 -*-
"""
7. Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и 
их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""

# with open("task7-input.txt", 'wt', encoding="utf8") as fi:
# 	import random
# 	forms = ['ООО', 'ИП', 'ОАО', 'ЗАО']
# 	for i in range(1, random.randint(10, 30)):
# 		form = random.choice(forms)
# 		revenue = random.randint(10000, 1000000)
#  		costs = random.randint(int(revenue * 0.5), int(revenue * 1.5))
# 		print(f"firm_{i} {form} {revenue} {costs}", file=fi)


import json

data = [{}, {"average_profit": 0}]
average_count = 0
with open('task7-input.txt', 'rt', encoding='utf8') as file_input:
	for line in file_input.readlines():
		name, form, revenue, costs = line.split()
		revenue = int(revenue)
		costs = int(costs)
		income = revenue - costs
		data[0][name] = income
		if income > 0:
			average_count += 1
			data[1]['average_profit'] += income

	data[1]['average_profit'] = round(data[1]['average_profit'] / average_count, 2)
	with open('task7-output.txt', 'wt') as file_output:
		json.dump(data, file_output)

