'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''
# не совсем понял данное задание, но попытаюсь реализовать как понял :(

rating = []
user_input = None
while user_input != 'quit':
	user_input = input("Введите целое число или команду quit для выхода\n")
	try:
		num = int(user_input)
		rating.append(num)
		rating = sorted(rating, reverse=True)
	except Exception as e:
		print("Введены некорректные данные")
print(f"Текущий рейтинг:\n{rating}")