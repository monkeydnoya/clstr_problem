import csv


_list = [] # Текущий кластер
_list_clstr = []
result_list = [] 
_new_claster = [] # Новый кластер

unique_id = set()

# Переборка уникальных id из кластера
with open('clstr.csv', 'r') as data:
	for row in csv.reader(data):
		if row[0] == 'user1' or row[2] == 'user2':
			continue

		unique_id.add(int(row[0]))
		unique_id.add(int(row[2]))

list_unique = sorted(list(unique_id))
list_unique.pop(0)

inCluster = False
isAdd = False

# Алгоритм разделения кластеров
with open('clstr.csv', 'r') as data:
	for i in range(len(list_unique)):
		inCluster = False
		isAdd = False
		_list_clstr = []

		with open('clstr.csv', 'r') as data:
			for row in csv.reader(data):
				if i == 0:
					if row[0] == 'user1' or row[2] == 'user2':
						continue

					if int(row[0]) == list_unique[i]:	
						_list_clstr = [int(row[0]), int(row[2])]
						_list.append(_list_clstr)
						isAdd = True
				else:
					if row[0] == 'user1' or row[2] == 'user2':
						continue

					if int(row[0]) == list_unique[i]:
						# Проверка на пренадлежность к кластеру
						for element in result_list:
							for el in element:
								for m in range(len(element)):
									for n in range(len(el)):
										if int(row[0]) == element[m][n]:
											inCluster = True
											# Если id пренадлижет кластеру то текущий класстер меняется на кластер где найден обьект
											_list = element
											break

						if inCluster:
							# Если id найден в кластере то он добавляется в текщий кластер
							_list_clstr = [int(row[0]), int(row[2])]
							_list.append(_list_clstr)
							isAdd = True


						else:
							# Если id не найден то создается новый кластер
							_list_clstr = [int(row[0]), int(row[2])]
							_new_claster.append(_list_clstr)


		if isAdd:
			result_list.append(_list)

		else:
			result_list.append(_list)
			result_list.append(_new_claster)
			_new_claster = []

del _list
del _new_claster
del _list_clstr

# Очистка от повторяющихся кластеров
unique_result_list = []

for i in result_list:
	if i not in unique_result_list:
		if not len(i) == 0:
			unique_result_list.append(i)

del result_list
print(unique_result_list)