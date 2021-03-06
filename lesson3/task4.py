'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
** Подсказка:** попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''
def my_func(x, y):
	# Для вычисление отрицательной степени используем формулу: X в -n = 1 / X в n
	result = 1
	for _ in range(-y):
		result *= x
	return 1 / result

try:
	x = float(input("Введите действительное положительное число:"))
	y = int(input("Введите целое отрицательное число:"))
	if not (y < 0 and x > 0):
		raise("Ошибка ввода")
	
	print(my_func(x, y))
	print("Проверка:", x**y)
except:
	print("Ошибка ввода")

