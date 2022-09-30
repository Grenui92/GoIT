def total_salary(path):
	file = open(path, 'r')
	file.seek(0)
	result = 0
	while True:
		line = file.readline()
		if not line:
			break
		zp = line.split(',')[1]
		result += float(zp)
	file.close()
	return result
		
		
print(total_salary())