def flatten(data):
	result = []
	for i in data:
		if type(i) == list:
			result.extend(flatten(i))
		else:
			result.append(i)
	return result
		

print(flatten([1, 2, [3, 4, [5, 6]], 7]))