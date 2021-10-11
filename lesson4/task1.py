'''
Задание: 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. 
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. 
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
'''
import sys

def calc_salary(hours, rate, premium):
	return hours * rate + premium

if __name__ == "__main__":
	try:
		hours, rate, premium = sys.argv[1:]
	except:
		print("Передайте три параметра: часы, ставка, премия\nНапример: task1.py 25 1000 3000")
		exit()
	try:
		hours = int(hours)
		rate = int(rate)
		premium = int(premium)
	except:
		print("Ошибка - параметры должны быть целыми числами!")
		exit()

	print("Расчитанная ЗП:", calc_salary(hours, rate, premium))