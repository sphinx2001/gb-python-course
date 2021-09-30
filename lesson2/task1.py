'''
1. Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''
data = [1.2, True, 234, "String", 323, {1, 2, 3}, [1, 2, 3, 4], 33.22, {'key1': 1, 'key2': 3}, False]

for element in data:
	if type(element) == type(float()):
		print(f"Element '{element}' is float")
	elif type(element) == type(bool()):
		print(f"Element '{element}' is bool")
	elif type(element) == type(int()):
		print(f"Element '{element}' is int")
	elif type(element) == type(str()):
		print(f"Element '{element}' is str")
	elif type(element) == type(set()):
		print(f"Element '{element}' is set")
	elif type(element) == type(list()):
		print(f"Element '{element}' is list")
	elif type(element) == type(dict()):
		print(f"Element '{element}' is dict")
	else:
		print(f"Element '{element}' has unknown type")