'''
2. Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
'''

def my_output(first_name="Иван", 
				last_name="Иванов", 
				year="1965", 
				city="Уфа", 
				email="ivanov_ivan@ufa.ru", 
				phone="+79270000001"):
	print(f"{first_name} {last_name}, {year}, {city}, {email}, {phone}")

my_output(first_name="Вася", year=1980, phone="+79810011111", email="vasy@mail.ru", city="Москва", last_name="Петров")