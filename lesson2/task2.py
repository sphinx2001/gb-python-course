'''
2. Для списка реализовать обмен значений соседних элементов, 
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
'''
print("Введите список элементов разделенных пробелами, например: 1 2 4 5 55 34 523 5456")
data = input().split()
print(f"Получен список:\n{data}")
length = len(data)
if length % 2 != 0:
	length -= 1
for i in range(0, length, 2):
	data[i], data[i+1] = data[i+1], data[i]

print(f"Список после обработки:\n{data}")