# -*- coding: utf-8 -*-
'''
1. Создать программно файл в текстовом формате, 
записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
'''

with open("output-task1.txt", "wt") as file_text:
	while True:
		answer = input("output-task1.txt < ")
		if answer == "":
			print("quit...")
			break
		print(answer, file=file_text)