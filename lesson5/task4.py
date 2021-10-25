# -*- coding: utf-8 -*-
"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, 
открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""
dict_replace = {
	"One": "Один",
	"Two": "Два",
	"Three": "Три",
	"Four": "Четыре",
}

with open("task4-input.txt", encoding="utf8") as file_input:
	with open("task4-output.txt", "wt", encoding="utf8") as file_output:
		for line in file_input:
			line = line.strip()
			for word, new_word in dict_replace.items():
				line = line.replace(word, new_word)
			print(line, file=file_output)
