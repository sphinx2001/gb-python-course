# -*- coding: utf-8 -*-
"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("task2-data.txt") as file_text:
	data = file_text.readlines()
	print(f"Количество строк: {len(data)}")
	print("Количество слов в строках:")
	for idx, line in enumerate(data, 1):
		print(f"{idx} - {len(line.split())}")
