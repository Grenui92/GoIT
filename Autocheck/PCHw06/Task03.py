def read_employees_from_file(path):
	file = open(path, 'r')
	result = [i.strip() for i in file.readlines()]
	file.close()
	return result


print(read_employees_from_file('Task03.txt'))